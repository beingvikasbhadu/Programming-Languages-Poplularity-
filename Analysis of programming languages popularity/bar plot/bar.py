import os
import sys
sys.path.append(os.getcwd())
from matplotlib import pyplot as plt
import numpy as np
from main import *

        #Top 10 famous programming languages
    
# X and Y co-ordinates
languages=np.array(list())
user1=np.array(list())

for langs in c.most_common(15):
    languages=np.append(languages,langs[0])
    user1=np.append(user1,langs[1])

# Create labels and title
plt.style.use('seaborn')
plt.title('Top 10 Famous programming languages')
plt.ylabel('No. of user')

plt.bar(languages[0:11:],user1[0:11:],width=.4,color='#5a7d9a')

plt.tight_layout()
plt.show()

            #Top 15 Famous Programming Languages

# Create labels and title
plt.style.use('seaborn')
plt.title('Top 15 Famous Programming Languages')
plt.ylabel('No. of user')

# X and Y co-ordinate
languages=languages[::-1]
user1=user1[::-1]

plt.barh(languages,user1,height=.6,color='#5a7d9a')

plt.tight_layout()
plt.show()
