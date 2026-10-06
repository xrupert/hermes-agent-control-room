from pathlib import Path
import urllib.request,json,concurrent.futures,datetime
r=Path(__file__).parent/'source'
tasks={}
for e in json.load(open(r/'nfl-week4.json'))['events']:tasks['nfl-summary-'+e['id']+'.json']='https://site.api.espn.com/apis/site/v2/sports/football/nfl/summary?event='+e['id']
for w in range(1,4):tasks[f'nfl-week{w}.json']=f'https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?dates=2026&seasontype=2&week={w}&limit=100'
for w in range(1,5):tasks[f'cfb-week{w}.json']=f'https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=2026&seasontype=2&week={w}&groups=80&limit=1000'
def f(x):
 k,u=x
 try:
  with urllib.request.urlopen(u,timeout=25) as a:b=a.read()
  (r/k).write_bytes(b);return {'file':k,'url':u,'bytes':len(b),'retrieved':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 except Exception as e:return {'file':k,'url':u,'error':str(e)}
res=list(concurrent.futures.ThreadPoolExecutor(6).map(f,tasks.items()));(r/'checks-retrieval.json').write_text(json.dumps(res,indent=2));print('Success',sum('error' not in x for x in res),'of',len(res));print([x for x in res if 'error'in x])
