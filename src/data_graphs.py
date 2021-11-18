import plotly.express as px
import pandas as pd
import data_collection
import plotly.graph_objects as go
from data_collection import Df


# Pour un pie chart, on a besoin d'une dataframe prête à être utilisée
# On la récupère dans data_collection
# le code suivant donne pour chaque département un visuel sous forme de camembert de la part de la population agée de plus de 65 ans
D = Df()


def camembert(x):
    L = D['id'].tolist()
    i = L.index(x)
    x = [D['pourcentage_agées'][i], 100 - D['pourcentage_agées'][i]]
    names = ['Pourcentage des agés', 'pourcentage des jeunes']
    cam = px.pie(values=x, names=names)
    cam.show()


#camembert('09')

# n est le STRING constitué du numéro du département souhaité.


def pie_chart(n):
    if n != "2A" and n != "2B" and n != "971" and n != "972" and n != "973" and n != "974" and n != "975":
        if int(n) <= 19:
            n = int(n)
            labels = ["plus_de_65_ans", "moins_de_65_ans"]
            values = [data_collection.list_pourc_agés()[int(
                n-1)], 100-(data_collection.list_pourc_agés()[int(n-1)])]
            res = go.Figure(data=[go.Pie(labels=labels, values=values)])
            res.update_layout(
                title_text="Part de la population agée de plus/moins de 65 ans dans le département "+str(n))
            res.show()

        elif int(n) >= 21:
            labels = ["plus_de_65_ans", "moins_de_65_ans"]
            values = [data_collection.list_pourc_agés()[int(
                n)], 100-(data_collection.list_pourc_agés()[int(n)])]
            res = go.Figure(data=[go.Pie(labels=labels, values=values)])
            res.update_layout(
                title_text="Part de la population agée de plus/moins de 65 ans dans le département " + str(n))
            res.show()
    elif n == '2A':
        labels = ["plus_de_65_ans", "moins_de_65_ans"]
        values = [data_collection.list_pourc_agés()[19], 100 -
                  (data_collection.list_pourc_agés()[19])]
        res = go.Figure(data=[go.Pie(labels=labels, values=values)])
        res.update_layout(
            title_text="Part de la population agée de plus/moins de 65 ans dans le département 2A")
        res.show()
    elif n == '2B':
        labels = ["plus_de_65_ans", "moins_de_65_ans"]
        values = [data_collection.list_pourc_agés()[20], 100 -
                  (data_collection.list_pourc_agés()[20])]
        res = go.Figure(data=[go.Pie(labels=labels, values=values)])
        res.update_layout(
            title_text="Part de la population agée de plus/moins de 65 ans dans le département 2B")
        res.show()
    elif n == '971':
        labels = ["plus_de_65_ans", "moins_de_65_ans"]
        values = [data_collection.list_pourc_agés()[96], 100 -
                  (data_collection.list_pourc_agés()[96])]
        res = go.Figure(data=[go.Pie(labels=labels, values=values)])
        res.update_layout(
            title_text="Part de la population agée de plus/moins de 65 ans dans le département 971")
        res.show()
    elif n == '972':
        labels = ["plus_de_65_ans", "moins_de_65_ans"]
        values = [data_collection.list_pourc_agés()[97], 100 -
                  (data_collection.list_pourc_agés()[97])]
        res = go.Figure(data=[go.Pie(labels=labels, values=values)])
        res.update_layout(
            title_text="Part de la population agée de plus/moins de 65 ans dans le département 972")
        res.show()
    elif n == '973':
        labels = ["plus_de_65_ans", "moins_de_65_ans"]
        values = [data_collection.list_pourc_agés()[98], 100 -
                  (data_collection.list_pourc_agés()[98])]
        res = go.Figure(data=[go.Pie(labels=labels, values=values)])
        res.update_layout(
            title_text="Part de la population agée de plus/moins de 65 ans dans le département 973")
        res.show()
    elif n == '974':
        labels = ["plus_de_65_ans", "moins_de_65_ans"]
        values = [data_collection.list_pourc_agés()[99], 100 -
                  (data_collection.list_pourc_agés()[99])]
        res = go.Figure(data=[go.Pie(labels=labels, values=values)])
        res.update_layout(
            title_text="Part de la population agée de plus/moins de 65 ans dans le département 974")
        res.show()
    elif n == '975':
        labels = ["plus_de_65_ans", "moins_de_65_ans"]
        values = [data_collection.list_pourc_agés()[100], 100 -
                  (data_collection.list_pourc_agés()[100])]
        res = go.Figure(data=[go.Pie(labels=labels, values=values)])
        res.update_layout(
            title_text="Part de la population agée de plus/moins de 65 ans dans le département 975")
        res.show()


# print(pie_chart("975"))
# pie_chart("05")
print(D.columns.tolist())