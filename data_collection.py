import pandas as pd
import csv
Path="./Data/estim-pop-dep-sexe-gca-1975-2021.xlsx"
Path2="./Data/equip-serv-sante-com-2020.xlsx"

#le code retourne une dataframe avec la population par département

def dep_pop():  
   dep_population=pd.read_excel("/Users/utilisateur/Documents/CW_WEEK2/csante/Data/estim-pop-dep-sexe-gca-1975-2021.xlsx", sheet_name="2021",usecols=[0,1,7],skiprows=[0,1,2,3,101, 102,103,104,105,106,107,108,109,110], names=["Numdép", "Nomdép", "Population"])
   return dep_population
   
def df(Path,column):

    L=[]
    i=column
    df = pd.read_excel (Path,sheet_name='2021',skiprows=[0,1,2,3,108,107,106,103,104,105,111,112
    ,110,109,102,101],usecols=[i],names='A')
    for i in range(len(df['A'])):
        L.append(df['A'][i])
    return L



def list_pourc_vieux():
    dep=df(Path,0)
    nomb_vieux_1=df(Path,5)
    nomb_vieux_2=df(Path,6)
    pourc_vieux=[]
    nomb_total=df(Path,7)
    for i in range(len(nomb_vieux_1)):
        a=nomb_vieux_1[i]+nomb_vieux_2[2]
        b=(int((a*100/nomb_total[i])*100))/100
        pourc_vieux.append(b)
    return pourc_vieux




def pourc_vieux(dep):
    L=list_pourc_vieux()
    B=df(Path,0)
    i=B.index(dep)
    return L[i]

print(pourc_vieux('04'))

def data_des_agées():
    data_des_agées=pd.DataFrame({'dep':df(Path,0),'pourc_vieux':list_pourc_vieux()})
    return data_des_agées



print(data_des_agées())
