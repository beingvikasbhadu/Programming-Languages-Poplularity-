import sys
import os
sys.path.append(os.getcwd())
from matplotlib import pyplot as plt
import numpy as np
from main import *
                # Top 5 Famous Programming Languages

#Create title
plt.title('Top 5 Famous Programming Languages (According to no. of user)')

# X and Y co-ordinates
languages=np.array(list())
user1=np.array(list())

for lang in c.most_common(28):
    languages=np.append(languages,lang[0])
    user1=np.append(user1,lang[1])


plt.pie(user1[:6:],wedgeprops={'edgecolor':'black'},labels=languages[:6:],autopct="%1.1f%%")

plt.tight_layout()
plt.show()


       #Top 5 Unknown Programming Languages
    
# Create Title
plt.title('Top 5 Unknown Programming Languages (According to no. of user)')

plt.pie(user1[24::],wedgeprops={'edgecolor':'black'},labels=languages[24::],autopct="%1.1f%%")

plt.tight_layout()
plt.show()