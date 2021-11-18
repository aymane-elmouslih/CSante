import pandas as pd
import population as popu
from data_depart import data 

df = data()

assert df.loc["28", 'Département_name'] == " Drôme - Valence" #26
assert df.loc["05", 'Établissement santé court séjour'] == 6
assert df.loc["75", 'Établissement psychiatrique'] == 79
assert df.loc["75", 'Structures psychiatriques en ambulatoire'] == 70