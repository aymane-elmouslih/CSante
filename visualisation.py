import plotly.express as px
import population as popu
import data_depart
import pandas as pd
from data_depart import data as dp
import plotly.graph_objects as go
import plotly.io as pio
import json


vardp = dp()

#département selon le nombres de leurs equipements == fig1

nombre_equipement = pd.DataFrame(vardp.sum(axis=1,numeric_only=True))
nombre_equipement.columns = ["nombre d'équipement"]
fig1 = px.bar(nombre_equipement)

#Pour chaque département, la répartition de leur equipement
def equipement(numero_depart): # attention string
    vardp_dep = pd.DataFrame(vardp.loc[numero_depart]) #dfloc donne une series
    vardp_dep = vardp_dep.iloc[:-2]
    #print(vardp_dep)
    vardp_dep.columns = ['values']
    vardp_dep['équipement'] = vardp_dep.index
    return px.bar(vardp_dep, y="values", x="équipement", title='Répartition des équipements')

###Indicateur équipement par population
'''def maxcoeff():
    l = []
    for i in range(95):
        numero_dep = i
        coeff = (numero_equipement.iloc[numero_dep-1,0]/popu.data_france().iloc[numero_dep-1,2])*(10**4)
        l.append(coeff)
    return max(l)


def meancoeff():
    l = []
    for i in range(95):
        numero_dep = i
        coeff = (nombre_equipement.iloc[numero_dep-1,0]/popu.data_france().iloc[numero_dep-1,2])*(10**4)
        l.append(coeff)
    return sum(l)/len(l)
'''

max_coefficient = 33.2 #trouvé en faisant tournant l'algo ci-dessus
mean_coefficent = 8.34

def indicateur(numero_dep): #variable entree == int
    coeff = (nombre_equipement.iloc[numero_dep-1,0]/popu.data_france().iloc[numero_dep-1,2])*(10**4)
    #choix couleur indicateur
    indic_color = "orange"
    if coeff > 8.34:
        indic_color = "green"

    #indicateur
    fig3 = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = coeff,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Indicateur santé"},
        delta = {'reference': 8.34},
        gauge = {
            'axis': {'range': [None, 35]},
            'bar': {'color': indic_color},
            'steps': [
                {'range': [0, 8.34], 'color': 'lightgray'},
                {'range': [8.34, 35], 'color': 'gray'}],
                }
                ))
    return fig3

indicateur(75).show()







    

