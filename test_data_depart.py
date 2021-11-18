import pandas as pd
import population as popu
from src.data_collection import data 

df = data()

assert df.loc["28", 'Département_name'] == " Drôme - Valence" #26
assert df.loc["05", 'Établissement santé court séjour'] == 6
assert df.loc["75", 'Établissement psychiatrique'] == 79
assert df.loc["75", 'Structures psychiatriques en ambulatoire'] == 70