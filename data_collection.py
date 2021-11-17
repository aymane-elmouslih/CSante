import pandas as pd
Path="/Users/utilisateur/Documents/CW_WEEK2/csante/Data/estim-pop-dep-sexe-gca-1975-2021.xlsx"
Path2="./Data/equip-serv-sante-com-2020.xlsx"
#df = pd.read_excel (Path,sheet_name='2021',skiprows=[0,1,2,3],usecols=[0,1])


#for x in df:
 #   for n in df[x]:
  #      L.append(n)

#le code retourne une dataframe avec la population par département.

def dep_pop():  
   dep_population=pd.read_excel("/Users/utilisateur/Documents/CW_WEEK2/csante/Data/estim-pop-dep-sexe-gca-1975-2021.xlsx", sheet_name="2021",usecols=[0,1,7],skiprows=[0,1,2,3,101,107,108,109,110], names=["Numdép", "Nomdép", "Population"])
   return dep_population
   

def df(Path,column):

    L=[]
    i=column
    df = pd.read_excel (Path,sheet_name='2021',skiprows=[0,1,2,3,108,107,111,112
    ,110,109,101],usecols=[i],names='A')
    for i in range(len(df['A'])):
        L.append(df['A'][i])
    return L



def list_pourc_agés():
    dep=df(Path,0)
    nomb_agés_1=df(Path,5)
    nomb_agés_2=df(Path,6)
    pourc_agés=[]
    nomb_total=df(Path,7)
    for i in range(len(nomb_agés_1)):
        a=nomb_agés_1[i]+nomb_agés_2[2]
        b=(int((a*100/nomb_total[i])*100))/100
        pourc_agés.append(b)
    return pourc_agés
 
def dep_pop_et_plus65():
    dep_pop_new= dep_pop()
    part_agés= list_pourc_agés()
    dep_pop_new['part_agés']=part_agés
    return dep_pop_new
 
print(dep_pop_et_plus65())




def pourc_agés(dep):
    L=list_pourc_agés()
    B=df(Path,0)
    i=B.index(dep)
    return L[i]

#print(pourc_agés('04'))

def data_des_agées():
    data_des_agées=pd.DataFrame({'dep':df(Path,0),'pourc_agés':list_pourc_agés()})
    return data_des_agées



