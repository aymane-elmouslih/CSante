import plotly.express as px
import pandas as pd
import data_collection
import plotly.graph_objects as go

fig=px.bar(data_collection.dep_pop(),x="Nomdép",y="Population")
#fig.show()   exemple de Bar Chart

# Pour un pie chart, on a besoin d'une dataframe prête à être utilisée
# On la récupère dans data_collection
#le code suivant donne pour chaque département un visuel sous forme de camembert de la part de la population agée de plus de 65 ans

def pie_chart(n): # n est le numéro du département souhaité. mettre 201 pour 2A et 202 pour 2B
    if n<=19:
       labels=["plus_de_65_ans","moins_de_65_ans"]
       values=[data_collection.list_pourc_agés()[n-1],100-(data_collection.list_pourc_agés()[n-1])]
       res=go.Figure(data=[go.Pie(labels=labels, values=values)])
       res.update_layout(title_text="Part de la population agée de plus/moins de 65 ans dans le département "+str(n))
       res.show()
    elif n==201:
         labels=["plus_de_65_ans","moins_de_65_ans"]
         values=[data_collection.list_pourc_agés()[19],100-(data_collection.list_pourc_agés()[19])]
         res=go.Figure(data=[go.Pie(labels=labels, values=values)])
         res.update_layout(title_text="Part de la population agée de plus/moins de 65 ans dans le département 2A")
         res.show()
    elif n==202:
         labels=["plus_de_65_ans","moins_de_65_ans"]
         values=[data_collection.list_pourc_agés()[20],100-(data_collection.list_pourc_agés()[20])]
         res=go.Figure(data=[go.Pie(labels=labels, values=values)])
         res.update_layout(title_text="Part de la population agée de plus/moins de 65 ans dans le département 2B")
         res.show()
    elif n>=21:
         labels=["plus_de_65_ans","moins_de_65_ans"]
         values=[data_collection.list_pourc_agés()[n],100-(data_collection.list_pourc_agés()[n])]
         res=go.Figure(data=[go.Pie(labels=labels, values=values)])
         res.update_layout(title_text="Part de la population agée de plus/moins de 65 ans dans le département " + str(n))
         res.show()
        
    
print(pie_chart(94))
    
    
