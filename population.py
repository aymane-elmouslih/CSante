import pandas as pd

def data_france():
    file = pd.read_excel('/Users/ibrah/csante/Data/estim-pop-dep-sexe-gca-1975-2021.xlsx')
    d = pd.read_excel('/Users/ibrah/csante/Data/estim-pop-dep-sexe-gca-1975-2021.xlsx', sheet_name = "2021", usecols=[0,1,7], skiprows=[i for i in range(4)]+[i for i in range(101,111)], names=["Numdep", "Nomdep","population"])
    return d


    



