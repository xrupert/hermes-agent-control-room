import pandas as pd,json
from pathlib import Path
R=Path(__file__).parent
p=pd.read_csv(R/'source/nfl.csv.gz',low_memory=False)
assert not p[['game_id','play_id']].duplicated().any()
p=p[(p.season_type=='REG')&(p.week<=4)]
g=p.groupby('game_id')[['week','game_date','home_team','away_team','home_score','away_score']].last().reset_index();g.to_csv(R/'nfl-game-coverage.csv',index=False)
alias={'WSH':'WAS','LAR':'LA'}
def ab(x):return alias.get(x['abbreviation'],x['abbreviation'])
names={};up={};checks=[];metadata={}
for e in json.load(open(R/'source/nfl-week4.json'))['events']:
 c=e['competitions'][0]['competitors'];ts={ab(x['team']):int(x['score']) for x in c}
 for x in c:names[ab(x['team'])]=x['team']['displayName'];metadata[ab(x['team'])]=x['team']
 z=g[(g.week==4)&g.home_team.isin(ts)&g.away_team.isin(ts)];assert len(z)==1 and e['status']['type']['completed'];z=z.iloc[0]
 assert ts[z.home_team]==z.home_score and ts[z.away_team]==z.away_score
 checks.append({'game':z.game_id,'espn_event':e['id'],'final_match':True})
assert len(checks)==16 and len(names)==32
j=json.load(open(R/'source/nfl-week5.json'))
for e in j['events']:
 c=e['competitions'][0]['competitors']
 for i,x in enumerate(c):up[ab(x['team'])]=c[1-i]['team']['displayName']
for t in j['week'].get('teamsOnBye',[]):up[ab(t)]='BYE — Week 5'
q=p[p.posteam.notna()&p.defteam.notna()&p.play_type.isin(['run','pass'])&p.qb_kneel.ne(1)&p.qb_spike.ne(1)&p.two_point_attempt.ne(1)].copy()
q['explosive']=((q.complete_pass.eq(1)&q.yards_gained.ge(20))|(q.play_type.eq('run')&q.yards_gained.ge(10))).astype(int)
q['success']=q.epa.gt(0).where(q.epa.notna())
rows=[]
for scope,s in [('week-4',q[q.week==4]),('season-to-date',q)]:
 for t in sorted(names):
  a=s[s.posteam==t];b=s[s.defteam==t]
  z={'team':t,'name':names[t],'scope':scope,'status':'played' if len(a) else 'not played','games':a.game_id.nunique(),'off_plays':len(a),'def_plays':len(b),'off_epa_n':a.epa.count(),'def_epa_n':b.epa.count(),'off_epa':a.epa.mean(),'allowed_epa':b.epa.mean(),'off_success':100*a.success.mean(),'allowed_success':100*b.success.mean(),'off_explosive':100*a.explosive.mean(),'allowed_explosive':100*b.explosive.mean(),'next_opponent':up.get(t,'Unverified')}
  for k in ['epa','success','explosive']:z['net_'+k]=z['off_'+k]-z['allowed_'+k]
  rows.append(z)
d=pd.DataFrame(rows)
prior=pd.read_csv(R.parent/'three-numbers-2026-09-29/nfl-all-32-metrics.csv');prior=prior[prior.scope.eq('season-to-date')].set_index('team')
for k in ['epa','success','explosive']:
 d[k+'_rank']=d.groupby('scope')['net_'+k].rank(ascending=False,method='min').astype('Int64');d[k+'_percentile']=100*(32-d[k+'_rank'])/31
 d[k+'_prior_published_rank']=d.apply(lambda r:prior.loc[r.team,k+'_rank'] if r.scope=='season-to-date' else None,axis=1)
 d[k+'_rank_change']=d[k+'_prior_published_rank']-d[k+'_rank']
d.to_csv(R/'nfl-all-32-metrics.csv',index=False)
json.dump(metadata,open(R/'source/nfl-team-metadata.json','w'),indent=2)
json.dump({'duplicate_ids':0,'games_by_week':g.groupby('week').size().to_dict(),'latest_week_score_checks':checks,'eligible_plays':len(q),'missing_epa':int(q.epa.isna().sum()),'missing_yards':int(q.yards_gained.isna().sum()),'season_dates':[g.game_date.min(),g.game_date.max()],'week_dates':[g[g.week==4].game_date.min(),g[g.week==4].game_date.max()]},open(R/'nfl-audit.json','w'),indent=2)
print(d[d.scope.eq('season-to-date')][['team','net_epa','net_success','net_explosive','epa_rank','success_rank','explosive_rank']].sort_values('epa_rank').to_string(index=False))
