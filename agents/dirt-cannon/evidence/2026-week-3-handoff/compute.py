import pandas as pd, json, sys
from pathlib import Path
R=Path(__file__).parent
p=pd.read_csv(R.parent/'pbp-2026-current.csv.gz',low_memory=False)
assert not p[['game_id','play_id']].duplicated().any()
p=p[(p.season_type=='REG')&(p.week<=3)]
games=p.groupby('game_id')[['week','game_date','home_team','away_team','home_score','away_score']].last().reset_index()
games.to_csv(R/'nfl-game-coverage.csv',index=False)
alias={'WSH':'WAS','LAR':'LA'}
def ab(t):return alias.get(t['abbreviation'],t['abbreviation'])
names={}; upcoming={}; checks=[]
for e in json.load(open(R/'source/nfl-week3.json'))['events']:
 c=e['competitions'][0]['competitors']; ts={ab(x['team']):int(x['score']) for x in c}
 for x in c:names[ab(x['team'])]=x['team']['displayName']
 g=games[(games.week==3)&games.home_team.isin(ts)&games.away_team.isin(ts)]
 assert len(g)==1 and e['status']['type']['completed']
 g=g.iloc[0];assert ts[g.home_team]==g.home_score and ts[g.away_team]==g.away_score
 checks.append({'game':g.game_id,'espn_event':e['id'],'final_score_match':True})
for e in json.load(open(R/'source/nfl-week4.json'))['events']:
 c=e['competitions'][0]['competitors']
 for i,x in enumerate(c):upcoming[ab(x['team'])]=c[1-i]['team']['displayName']
q=p[p.posteam.notna()&p.defteam.notna()&p.play_type.isin(['run','pass'])&p.qb_kneel.ne(1)&p.qb_spike.ne(1)&p.two_point_attempt.ne(1)].copy()
q['explosive']=((q.complete_pass.eq(1)&q.yards_gained.ge(20))|(q.play_type.eq('run')&q.yards_gained.ge(10))).astype(int)
q['success']=q.epa.gt(0).where(q.epa.notna())
rows=[]
for scope,s in [('week-3',q[q.week==3]),('season-to-date',q)]:
 for t in sorted(names):
  a=s[s.posteam==t];b=s[s.defteam==t]
  z={'team':t,'name':names[t],'scope':scope,'games':a.game_id.nunique(),'off_plays':len(a),'def_plays':len(b),'off_epa_n':a.epa.count(),'def_epa_n':b.epa.count(),'off_epa':a.epa.mean(),'allowed_epa':b.epa.mean(),'off_success':100*a.success.mean(),'allowed_success':100*b.success.mean(),'off_explosive':100*a.explosive.mean(),'allowed_explosive':100*b.explosive.mean(),'next_opponent':upcoming.get(t,'Unverified')}
  for k in ['epa','success','explosive']:z['net_'+k]=z['off_'+k]-z['allowed_'+k]
  rows.append(z)
df=pd.DataFrame(rows)
for k in ['epa','success','explosive']:
 df[k+'_rank']=df.groupby('scope')['net_'+k].rank(ascending=False,method='min').astype(int)
 df[k+'_percentile']=100*(32-df[k+'_rank'])/31
df.to_csv(R/'nfl-all-32-metrics.csv',index=False)
json.dump({'duplicate_ids':0,'nfl_week3_games':len(checks),'score_checks':checks,'eligible_season_plays':len(q),'missing_epa':int(q.epa.isna().sum()),'nfl_refresh':'2026-09-29T11:32:16Z','repo_commit':'e217da20e569970cd6f456ca219e879dbefff603'},open(R/'audit.json','w'),indent=2)
print(df[df.scope=='season-to-date'][['team','net_epa','net_success','net_explosive','epa_rank','success_rank','explosive_rank']].sort_values('epa_rank').to_string(index=False))
