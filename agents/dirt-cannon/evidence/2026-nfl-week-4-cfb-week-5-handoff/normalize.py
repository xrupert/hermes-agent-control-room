import pandas as pd,json
from pathlib import Path
R=Path(__file__).parent
s=pd.read_csv(R/'nfl-all-32-metrics.csv');s=s[s.scope.eq('season-to-date')]
ts={c['team']['displayName']:c['team'] for e in json.load(open(R/'source/nfl-week4.json'))['events'] for c in e['competitions'][0]['competitors']}
verdict={
'SF':'First in efficiency. First in big-play balance.\nFour games of receipts; no lifetime warranty.',
'SEA':'Top four in all three measures. A strong\nfour-game profile can still contain a loss.',
'BAL':'Top five across the board. Four games make\na convincing opening argument, not a verdict.',
'JAX':'Second in efficiency. Sixteenth in big plays.\nThe offense works without winning every\nfireworks contest.',
'KC':'The NFL’s best success-rate balance.\nRepeated small victories pay the same rent.',
'GB':'Eighth in big plays. Twenty-ninth in efficiency.\nA highlight reel is not an alibi.'}
questions={'SF':'Can the offense sustain its efficiency advantage against Denver?', 'SEA':'Can more successful snaps produce a larger efficiency margin?', 'BAL':'Can Baltimore keep all three measures moving together?', 'JAX':'Can Jacksonville improve the big-play exchange against Cincinnati?', 'KC':'Can Kansas City keep winning the ordinary snaps against Las Vegas?', 'GB':'Can Green Bay fix the ordinary snaps against Tampa Bay?'}
meanings={
'SF':['The largest net scoring-value advantage in the NFL.','Successful plays arrived more often than they were allowed.','Created far more chunk gains per snap than it surrendered.'],
'SEA':['A top-four efficiency balance through four games.','Opponents succeeded on just 35.6% of eligible plays.','Allowed explosive gains on just 4.0% of eligible snaps.'],
'BAL':['Offensive efficiency exceeded what the defense allowed.','Won the success-rate exchange by nearly 10 points.','Generated chunk gains more often than it allowed them.'],
'JAX':['Strong efficiency on both sides of the ball.','Successful plays were more frequent than opponents’ successes.','Allowed chunk gains slightly more often than it created them.'],
'KC':['Positive offensive EPA met negative EPA allowed.','The league’s largest positive-EPA success-rate advantage.','The big-play exchange also finished in Kansas City’s favor.'],
'GB':['The offense lost expected scoring value per play.','Opponents succeeded more often; the gap ranks 31st.','A positive chunk-play balance has not fixed the other two.']}
verdict={'SF':'First in efficiency. First in big-play balance.\nFour games make a strong opening argument,\nnot a lifetime warranty.','BAL':'Top four in all three measures.\nBaltimore is winning ordinary snaps\nand the chunk-play exchange.','ATL':'First in consistency. Thirteenth in efficiency.\nWinning more snaps does not mean winning\nthe most valuable ones.','ARI':'Ninth in consistency. Last in big-play balance.\nThe ordinary snaps look better than\nthe damage from the big ones.','GB':'Tenth in big plays. Twenty-sixth in efficiency.\nA highlight reel is not a repair manual.','MIA':'Last in efficiency and consistency.\nThe big-play ranking is less ugly;\nthe ordinary snaps still need repairs.'}
questions={t:'Can the team improve its weakest measure in the next game?' for t in verdict}
meanings={}
rows=[]
for _,r in s.iterrows():
 t=r.team;m=ts[r['name']];row={'team':r['name'],'team_code':t,'city':m['location'],'nickname':m['name'],'primary':'#'+m['color'],'secondary':'#'+m['alternateColor'],'period':'2026 NFL · SEASON TO DATE · W1–4 · SEP 9–OCT 5','verdict':verdict.get(t,f'Efficiency #{r.epa_rank}; consistency #{r.success_rank}; big plays #{r.explosive_rank}.\nFour games describe the start, not established talent.'),'next_test':r.next_opponent,'next_question':questions.get(t,'Can the team improve its weakest measure in the next game?'),'sample':f'SAMPLE · 4 GAMES · {r.off_plays} OFFENSIVE / {r.def_plays} DEFENSIVE PLAYS'}
 for i,(key,col) in enumerate([('efficiency','epa'),('consistency','success'),('big_play_balance','explosive')]):
  row[key]={'rank':int(r[col+'_rank']),'value':float(r['net_'+col]),'offense':float(r['off_'+col]),'allowed':float(r['allowed_'+col]),'meaning':meanings.get(t,['Net expected scoring value per play.','Positive-EPA success-rate balance.','Explosive gains generated minus allowed.'])[i]}
 row['filename']=r['name'].lower().replace(' ','-')+'-nfl-2026-week-4-three-numbers-dirt-canon.png'
 row['caption']=row['verdict'].replace('\n',' ')+f' Through NFL Week 4, 2026. Four-game sample; not opponent-adjusted. More at TheDiRTCanon.com. #NFL #TheDiRTCanon'
 rows.append(row)
json.dump(rows,open(R/'verified-nfl-input-v2.json','w'),indent=2)

json.dump([x for x in rows if x['team_code'] in verdict],open(R/'selected-six-input.json','w'),indent=2)
