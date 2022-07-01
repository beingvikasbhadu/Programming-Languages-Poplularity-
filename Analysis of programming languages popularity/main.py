import pandas as pd
from collections import Counter
import os

path=os.path.join(os.getcwd(),'data.csv')
# Read the csv file
data=pd.read_csv(path)
print(data)
#Using Counter object count user of each language
c=Counter()
for langs in data['LanguagesWorkedWith']:
    langs=langs.split(';')
    c.update(langs)

  
