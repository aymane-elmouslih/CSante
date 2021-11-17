import pandas as pd
import csv
 
#le code retourne une dataframe avec la population par département

def dep_pop():  
   dep_population=pd.read_excel("/Users/utilisateur/Documents/CW_WEEK2/csante/Data/estim-pop-dep-sexe-gca-1975-2021.xlsx", sheet_name="2021",usecols=[0,1,7],skiprows=[0,1,2,3,101, 102,103,104,105,106,107,108,109,110], names=["Numdép", "Nomdép", "Population"])
   return dep_population
   
    