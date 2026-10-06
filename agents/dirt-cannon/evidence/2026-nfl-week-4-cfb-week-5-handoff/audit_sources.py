import pandas as pd,json
from pathlib import Path
R=Path(__file__).parent;p=pd.read_csv(R/'source/nfl.csv.gz',low_memory=False);alias={'WSH':'WAS','LAR':'LA'}
rows=[]
for f in (R/'source').glob('nfl-summary-*.json'):
 j=json.load(open(f));game=j['header']['competitions'][0];cs=game['competitors'];ab=[alias.get(x['team']['abbreviation'],x['team']['abbreviation']) for x in cs];z=p[(p.week==4)&p.home_team.isin(ab)&p.away_team.isin(ab)]
 for x in j['boxscore']['teams']:
  t=alias.get(x['team']['abbreviation'],x['team']['abbreviation']);stats={v['name']:v['displayValue'] for v in x['statistics']};q=z[(z.posteam==t)&z.play_type.isin(['run','pass','qb_kneel','qb_spike'])&z.two_point_attempt.ne(1)]
  yards=q.yards_gained.sum();plays=len(q);rows.append({'team':t,'pbp_yards':yards,'box_yards':int(stats['totalYards']),'pbp_plays':plays,'box_plays':int(stats['totalOffensivePlays']),'yards_match':yards==int(stats['totalYards']),'plays_match':plays==int(stats['totalOffensivePlays'])})
d=pd.DataFrame(rows);d.to_csv(R/'nfl-boxscore-audit.csv',index=False);print('NFL mismatches',d[~d.yards_match|~d.plays_match].to_dict('records'))
checks=[]
for w in range(1,5):
 events=json.load(open(R/f'source/nfl-week{w}.json'))['events'];g=p[p.week==w].groupby('game_id').last()
 for e in events:
  ts={alias.get(x['team']['abbreviation'],x['team']['abbreviation']):int(x['score']) for x in e['competitions'][0]['competitors']};z=g[g.home_team.isin(ts)&g.away_team.isin(ts)];ok=len(z)==1 and all(int(z.iloc[0][s+'_score'])==ts[z.iloc[0][s+'_team']] for s in ['home','away']);checks.append({'week':w,'event':e['id'],'match':ok})
json.dump(checks,open(R/'nfl-season-score-audit.json','w'),indent=2);print('Season scores',sum(x['match'] for x in checks),len(checks))
c=pd.read_parquet(R/'source/cfb.parquet');c=c[c.home_team_division.eq('fbs')|c.away_team_division.eq('fbs')].copy()
c=c.drop_duplicates()
assert not c.duplicated(['game_id','game_row_number']).any()
checks=[];slate=[]
for w in range(1,6):
 for e in json.load(open(R/f'source/cfb-week{w}.json'))['events']:
  z=c[c.game_id.eq(int(e['id']))]; cs=e['competitions'][0]['competitors'];completed=e['status']['type']['completed'];item={'week':w,'event':e['id'],'matchup':e['shortName'],'date':e['date'],'status':e['status']['type']['name'],'data_rows':len(z)}
  for x in cs:
   side=x['homeAway'];name=z[side+'_team'].iloc[0] if len(z) else x['team']['location'];score=max(z.loc[z.pos_team.eq(name),'pos_team_score'].max(),z.loc[z.def_pos_team.eq(name),'def_pos_team_score'].max()) if len(z) else None
   checks.append({**item,'team':name,'score':x['score'],'pbp_score':score,'score_match':completed and score==int(x['score'])})
  slate.append(item)
pd.DataFrame(checks).to_csv(R/'college-score-audit.csv',index=False);pd.DataFrame(slate).to_csv(R/'college-slate.csv',index=False)
print('CFB',len(slate),'games',sum(x['score_match'] for x in checks),'of',len(checks),'team score checks');print('CFB missing',[(x['matchup'],x['status']) for x in slate if not x['data_rows']])
