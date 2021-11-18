from src.data_collection import dep_pop as data
import pandas as pd

df = data()

file = pd.read_excel('./Data/estim-pop-dep-sexe-gca-1975-2021.xlsx')

assert df.loc[1,"Nomdép"] == "Aisne"
assert df.loc[15,"Numdép"] == "16"

#les departements corses 2A et 2B créent un décalage

assert df.loc[28,"Nomdép"] == "Eure-et-Loir"
assert df.loc[75,"Numdép"] == "75"


