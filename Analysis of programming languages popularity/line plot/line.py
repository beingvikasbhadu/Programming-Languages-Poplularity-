                   # Data source: stackoverflow
                   # It include total 28 languages
import sys
import os
#Adding path of main.py
sys.path.append(os.getcwd())
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter
import statistics as st
from main import *


                      # Top 10 Famous Programming Languages

#X and Y co-ordinate
top_languages=[]
user1=[]

for lang in c.most_common(10):
    top_languages.append(lang[0])
    user1.append(lang[1])

median_user=st.median(user1)

# Adding label and title
plt.style.use('ggplot')
plt.title('Top 10 Famous Programming Languages')
plt.ylabel('No. of user')
plt.plot(top_languages,user1,marker='o',linewidth='2')
plt.plot(top_languages,np.full(len(top_languages),median_user),color='black')

#Compare Number of users with median number of user
plt.fill_between(top_languages,user1,median_user,color='green',alpha=.6,where=(np.array(user1)>=median_user),label='above median no. of user',interpolate=True)
plt.fill_between(top_languages,user1,median_user,color='red',alpha=.6,where=(np.array(user1)<median_user),label='below median no. of user',interpolate=True)
plt.legend()

# To add some padding
plt.tight_layout()

plt.show()


        # Top 10 Unknown Programming Languages

# Reverse the list to get bottom languages data
l=list(c.most_common(28))
l.reverse()

#X and Y co-ordinate
unknown_langs=[]
user2=[]

for langs in l[0:11:1]:
    unknown_langs.append(langs[0])
    user2.append(langs[1])
median_user=st.median(user2)

#Adding Labels and title
plt.style.use('ggplot')
plt.title('Top 10 Unknown Programming Languages')
plt.ylabel('No. of user')

plt.plot(unknown_langs,user2,marker='o',linewidth=2)
plt.plot(unknown_langs,np.full(len(unknown_langs),median_user),color='black')

#Compare Number of users with median number of user
plt.fill_between(unknown_langs,user2,median_user,where=(np.array(user2)>=median_user),color='green',alpha=.6,label='above median no. of user',interpolate=True)
plt.fill_between(unknown_langs,user2,median_user,where=(np.array(user2)<median_user),color='red',alpha=.6,label='below median no. of user',interpolate=True)
plt.legend()

#To add some padding
plt.tight_layout()
plt.show()









