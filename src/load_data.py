import pandas as pd
import json
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"
# Grouper les données par département et supprimer
df = pd.read_excel(".\csante\Data\equip-serv-sante-com-2020.xlsx", skiprows=[0, 1, 2, 3, 5])
Df = df.groupby('Département').sum()
Df = Df.drop(['Région'], axis=1)  # les columns non utiles
Df['id'] = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2A', '2B', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
            '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '971', '972', '973', '974', '976']
map = json.load(open(".\csante\Data\contour-des-departements.geojson", 'r'))
data = Df[['Pharmacie', 'id']]

for feature in map['features']:
    feature['id'] = feature['properties']['code']

data = Df[['Pharmacie', 'id']]

fig = px.choropleth(data, locations='id', geojson=map, color='Pharmacie')
fig.update_geos(fitbounds="locations", visible=False)
fig.show()