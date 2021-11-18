import json
from data_collection import Df
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import json
import plotly.io as pio
import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
# Df = data_frame()
Df = Df()


app = dash.Dash(__name__)
map = json.load(open(".\Data\contour-des-departements.geojson", 'r'))
data = Df[['Pharmacie', 'id']]

for feature in map['features']:
    feature['id'] = feature['properties']['code']


# fig = px.choropleth_mapbox(Df, locations='id', geojson=map, color='Pharmacie', hover_name='Département_name',hover_data=['Établissement santé court séjour','Établissement santé moyen séjour','Établissement santé long séjour','Établissement psychiatrique','Centre lutte cancer','Urgences','Maternité','Centre de santé','Structures psychiatriques en ambulatoire','Centre médecine préventive','Dialyse','Hospitalisation à domicile','Maison de santé pluridisciplinaire',"Laboratoire d'analyses et de biologie médicale",'Ambulance','Transfusion sanguine','Établissement thermal','Pharmacie'],
#                           mapbox_style="carto-positron",
 #                          center={"lat": 47, "lon": 2},
  #                         zoom=5,opacity=0.8
    #                     ,color_continuous_scale="Viridis")
# fig.update_geos(fitbounds="locations", visible=False)


app.layout = html.Div(children=[

    html.H1(children="Group 'ConnectionS'"),




    # html.Div(id="style",children=[]
    #     ),





    dcc.Dropdown(id="servise",
                 options=[
                     {"label": "Pharmacie", "value": "Pharmacie"},
                     {"label": "Établissement santé court séjour",
                      "value": "Établissement santé court séjour"},
                     {"label": "Établissement santé moyen séjour",
                      "value": "Établissement santé moyen séjour"},
                     {"label": "Établissement santé long séjour",
                      "value": "Établissement santé long séjour"},
                     {"label": "Établissement psychiatrique",
                      "value": "Établissement psychiatrique"},
                     {"label": "Centre lutte cancer",
                      "value": "Centre lutte cancer"},
                     {"label": "Urgences", "value": "Urgences"},
                     {"label": "Maternité", "value": "Maternité"},
                     {"label": "Centre de santé",
                      "value": "Centre de santé"},
                     {"label": "Structures psychiatriques en ambulatoire",
                      "value": "Structures psychiatriques en ambulatoire"},
                     {"label": "Centre médecine préventive",
                      "value": "Centre médecine préventive"},
                     {"label": "Dialyse", "value": "Dialyse"},
                     {"label": "Hospitalisation à domicile",
                      "value": "Hospitalisation à domicile"},
                     {"label": "Maison de santé pluridisciplinaire",
                      "value": "Maison de santé pluridisciplinaire"},
                     {"label": "Laboratoire d'analyses et de biologie médicale",
                      "value": "Laboratoire d'analyses et de biologie médicale"},
                     {"label": "Ambulance", "value": "Ambulance"},
                     {"label": "Transfusion sanguine",
                      "value": "Transfusion sanguine"},
                     {"label": "Établissement thermal", "value": "Établissement thermal"}, ],
                 multi=False,
                 value='Pharmacie',
                 style={'width': "40%"}
                 ),


    dcc.Dropdown(id="slct_style",
                 options=[
                     {"label": "white-bg", "value": "white-bg"},
                     {"label": "open-street-map",
                      "value": "open-street-map"},
                     {"label": "carto-positron",
                      "value": "carto-positron"},
                     {"label": "carto-darkmatter",
                      "value": "carto-darkmatter"},
                     {"label": "stamen-terrain", "value": "stamen-terrain"}],
                    multi=False,
                 value='carto-positron',
                 style={'width': "40%"}
                 ),


    dcc.Dropdown(id="slct_couleure",
                 options=[
                     {"label": "px.colors.diverging.BrBG", "value": 1},
                     {"label": "px.colors.sequential.Cividis_r", "value": 2},
                     {"label": "Viridis", "value": "Viridis"}],
                    multi=False,
                 value='Viridis',
                 style={'width': "40%"}
                 ),




    dcc.Graph(
        id='map',
        figure={}),

    dcc.Graph(
        id='graphs',
        figure={}
    )








])


@ app.callback(
    [
        Output(component_id='map', component_property='figure')],
    [Input(component_id='slct_style', component_property='value'),
     Input(component_id="slct_couleure", component_property='value'),
     Input(component_id='servise', component_property='value')]
)
def update_graph(option_slctd1, option_slctd2, option_slctd3):
    if option_slctd2 == 1:
        fig = px.choropleth_mapbox(Df, locations='id', geojson=map, color=option_slctd3, hover_name='Département_name', hover_data=['Établissement santé court séjour', 'Établissement santé moyen séjour', 'Établissement santé long séjour', 'Établissement psychiatrique', 'Centre lutte cancer', 'Urgences', 'Maternité', 'Centre de santé', 'Structures psychiatriques en ambulatoire', 'Centre médecine préventive', 'Dialyse', 'Hospitalisation à domicile', 'Maison de santé pluridisciplinaire', "Laboratoire d'analyses et de biologie médicale", 'Ambulance', 'Transfusion sanguine', 'Établissement thermal', 'Pharmacie'],
                                   mapbox_style=option_slctd1,
                                   center={"lat": 47, "lon": 2},
                                   zoom=5, opacity=0.8, color_continuous_scale=px.colors.diverging.BrBG)
    elif option_slctd2 == 2:
        fig = px.choropleth_mapbox(Df, locations='id', geojson=map, color=option_slctd3, hover_name='Département_name', hover_data=['Établissement santé court séjour', 'Établissement santé moyen séjour', 'Établissement santé long séjour', 'Établissement psychiatrique', 'Centre lutte cancer', 'Urgences', 'Maternité', 'Centre de santé', 'Structures psychiatriques en ambulatoire', 'Centre médecine préventive', 'Dialyse', 'Hospitalisation à domicile', 'Maison de santé pluridisciplinaire', "Laboratoire d'analyses et de biologie médicale", 'Ambulance', 'Transfusion sanguine', 'Établissement thermal', 'Pharmacie'],
                                   mapbox_style=option_slctd1,
                                   center={"lat": 47, "lon": 2},
                                   zoom=5, opacity=0.8, color_continuous_scale=px.colors.sequential.Cividis_r)
    else:
        fig = px.choropleth_mapbox(Df, locations='id', geojson=map, color=option_slctd3, hover_name='Département_name', hover_data=['Établissement santé court séjour', 'Établissement santé moyen séjour', 'Établissement santé long séjour', 'Établissement psychiatrique', 'Centre lutte cancer', 'Urgences', 'Maternité', 'Centre de santé', 'Structures psychiatriques en ambulatoire', 'Centre médecine préventive', 'Dialyse', 'Hospitalisation à domicile', 'Maison de santé pluridisciplinaire', "Laboratoire d'analyses et de biologie médicale", 'Ambulance', 'Transfusion sanguine', 'Établissement thermal', 'Pharmacie'],
                                   mapbox_style=option_slctd1,
                                   center={"lat": 47, "lon": 2},
                                   zoom=5, opacity=0.8, color_continuous_scale='Viridis')

    fig.update_geos(fitbounds="locations", visible=False)
    return [fig]


if __name__ == '__main__':
    app.run_server(debug=True)
