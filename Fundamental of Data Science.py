#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd 
import matplotlib.pyplot as plt 
d={'year':list(range(2010,2021)),"job postings":[150,200,300,410,566,722,823,500,44,525,66]}
df=pd.DataFrame(d)
print(df)
plt.plot(df['year'],df['job postings'],marker='o',color="red",ls="--",mfc="blue")
plt.title("trend of ds jobs.")
plt.xlabel('year')
plt.ylabel('job postings')
plt.show()


# In[51]:


import matplotlib.pyplot as plt
c=["Data Analyst","Data engineer","Data scientist"]
d=[500,300,122]
plt.bar(c,d,color="green")
plt.title("DS job analysis",color="blue")
plt.xlabel('roles',color="brown")
plt.ylabel('number of postings',color="brown")
plt.show()


# In[ ]:





# In[ ]:




