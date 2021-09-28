import requests
import json
import pandas as pd

# fetch
url = "https://data.opendatasoft.com/api/records/1.0/search/?dataset=world-population%40kapsarc&rows=2885&facet=year&facet=country_name"

r = requests.get(url)
json_data = r.json()


model = {'pais': [],
       'populacao': [],
       'year': []}

# cleaning
for i in json_data['records']:
  model['pais'].append(i['fields']['country_name'])
  model['populacao'].append(int(i['fields']['value']))
  model['year'].append(i['fields']['year'])

data = pd.DataFrame(model).sort_values(["pais", "year"])
data = data.drop_duplicates(subset=["pais"], keep="last")
data.reset_index(inplace=True)
df = data[['pais', 'populacao', 'year']]

# save
df.to_csv("populacao_global.csv", index=False)
print("finalizado com sucesso!")
