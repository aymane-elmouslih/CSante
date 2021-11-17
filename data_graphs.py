import plotly.express as px
import pandas as pd
pd.options.plotting.backend = "plotly"
import data_collection

fig=px.bar(data_collection.dep_pop(),x="Nomdép",y="Population")
#fig.show()   exemple de Bar Chart

# Pour un pie chart, on a besoin d'une dataframe prête à être utilisée



