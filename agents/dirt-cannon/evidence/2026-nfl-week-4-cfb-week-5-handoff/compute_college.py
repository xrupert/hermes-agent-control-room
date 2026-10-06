import pandas as pd,json
from pathlib import Path
R=Path(__file__).parent
p=pd.read_parquet(R/'source/cfb.parquet')
p=p[p.home_team_division.eq('fbs')|p.away_team_division.eq('fbs')].copy()
exact_duplicates=int(p.duplicated().sum());p=p.drop_duplicates()
assert not p.duplicated(['game_id','game_row_number']).any()
teams=set(p.loc[p.home_team_division.eq('fbs'),'home_team'])|set(p.loc[p.away_team_division.eq('fbs'),'away_team'])
text=p.play_text.fillna('')
eligible=(p.rush.eq(1)|p.pass_attempt.eq(1)|p.sack.eq(1))&~p.penalty_no_play.fillna(False)&~text.str.contains(r'\bkneel|\bspike|two.point|2.pt|two point',case=False,regex=True)&~p.play_type.str.contains('Two Point|Kickoff|Punt|Field Goal',case=False)
q=p[eligible].copy();q['explosive']=((q.completion.eq(1)&q.yards_gained.ge(20))|(q.rush.eq(1)&q.yards_gained.ge(10))).astype(int);q['positive']=q.EPA.gt(0).where(q.EPA.notna())
rows=[]
for scope,s in [('week-5',q[q.week.eq(5)]),('season-to-date',q)]:
 for t in sorted(teams):
  a=s[s.pos_team.eq(t)];b=s[s.def_pos_team.eq(t)]
  z={'team':t,'scope':scope,'games':a.game_id.nunique(),'off_plays':len(a),'def_plays':len(b),'off_epa_n':a.EPA.count(),'def_epa_n':b.EPA.count(),'off_epa':a.EPA.mean(),'allowed_epa':b.EPA.mean(),'off_success':100*a.positive.mean(),'allowed_success':100*b.positive.mean(),'off_explosive':100*a.explosive.mean() if len(a) else None,'allowed_explosive':100*b.explosive.mean() if len(b) else None}
  for k in ['epa','success','explosive']:z['net_'+k]=z['off_'+k]-z['allowed_'+k] if z['off_'+k] is not None and z['allowed_'+k] is not None else None
  rows.append(z)
d=pd.DataFrame(rows)
# Coverage cannot yet be fully reconciled against an independent all-FBS slate.
# Do not publish provisional full-dataset ranks as national ranks.
d.to_csv(R/'college-all-fbs-provisional-calculations.csv',index=False)
poll=json.load(open(R/'source/ap-poll.json'))['rankings'][0]
sel=[{'team':r['team']['location'],'ap_rank':r['current'],'previous_ap_rank':r.get('previous'),'poll_timestamp':poll.get('lastUpdated')} for r in poll['ranks'] if r['current']<=10 or r['team']['location']=='LSU']
s=d.merge(pd.DataFrame(sel),on='team')
for k in ['epa','success','explosive']:s[k+'_selected_cohort_rank']=s.groupby('scope')['net_'+k].rank(ascending=False,method='min')
s.to_csv(R/'college-selected-cohort-provisional.csv',index=False)
aud={'status':'PROVISIONAL - independent complete slate and play classification not fully reconciled; no public CFB cards','source_refresh':'2026-10-05T15:38:34Z','fbs_teams_in_source':len(teams),'source_games':int(p.game_id.nunique()),'week5_source_games':int(p[p.week.eq(5)].game_id.nunique()),'duplicate_float_play_ids':int(p.duplicated(['game_id','id_play']).sum()),'exact_duplicates_removed':exact_duplicates,'duplicate_game_row_ids':0,'explanation':'id_play is float64 and loses precision; unique game_id/game_row_number retained without dropping distinct plays','eligible_plays':len(q),'missing_epa':int(q.EPA.isna().sum()),'selection':sel}
json.dump(aud,open(R/'college-audit.json','w'),indent=2)
print(s[s.scope.eq('season-to-date')][['team','games','net_epa','net_success','net_explosive']].to_string(index=False))
