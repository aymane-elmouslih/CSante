from population import data_france as data
import pandas as pd

df = data()

file = pd.read_excel('/Users/ibrah/csante/Data/estim-pop-dep-sexe-gca-1975-2021.xlsx')

assert df.loc[1,"Nomdep"] == "Aisne"
assert df.loc[15,"Numdep"] == "16"

#les departements corses 2A et 2B créent un décalage

assert df.loc[28,"Nomdep"] == "Eure-et-Loir"
assert df.loc[75,"Numdep"] == "75"


