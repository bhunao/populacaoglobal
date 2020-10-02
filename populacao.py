import requests
import json
import pandas as pd

u = "https://data.opendatasoft.com/api/records/1.0/search/?dataset=world-population%40kapsarc&rows=2885&facet=year&facet=country_name"

r = requests.get(u)
u = r.text

j = json.loads(u)

dat = {'pais': [],
       'populacao': [],
       'year': []}
for i in j['records']:
  dat['pais'].append(i['fields']['country_name'])
  dat['populacao'].append(int(i['fields']['value']))
  dat['year'].append(i['fields']['year'])

dat = pd.DataFrame(dat).sort_values(["pais", "year"])
dat = dat.drop_duplicates(subset=["pais"], keep="last")
dat.reset_index(inplace=True)
df = dat[['pais', 'populacao', 'year']]
print(df)
df.to_csv("populacao.csv", index=False)
