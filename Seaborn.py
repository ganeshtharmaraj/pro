#!/usr/bin/env python
# coding: utf-8

# ## seaborn

# In[1]:


import seaborn as sns


# In[2]:


import numpy as np
import pandas as pd
from io import StringIO,BytesIO
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


import seaborn as sns


# In[23]:


print(sns.get_dataset_names())


# In[6]:


ga=sns.load_dataset("flights")
sns.relplot(x="passengers",y="month",data=ga)


# In[10]:


ga=sns.load_dataset("flights")
sns.relplot(x="passengers",y="month",hue="year",data=ga)


# In[73]:


ga


# In[11]:


b=sns.load_dataset("tips")
sns.relplot(x="time",y="tip",data=b,kind="line")


# In[12]:


sns.catplot(x="day",y="total_bill",data=b)


# In[13]:


sns.catplot(x="day",y="total_bill",kind="violin",data=b)


# In[14]:



sns.catplot(x="day",y="total_bill",kind="boxen",data=b)


# In[15]:


from scipy import stats


# In[16]:


c=np.random.normal(loc=5,size=100,scale=2)


# In[17]:


sns.distplot(c)


# In[18]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


ma=sns.load_dataset("tips")


# In[20]:


ma.head()


# In[6]:


ma.corr()


# In[21]:


ma.dtypes


# In[22]:


sns.heatmap(ma.corr())


# ## joint plot

# In[24]:


sns.jointplot(x="tip",y="total_bill",data=ma,kind="hex")


# In[25]:


sns.jointplot(x="tip",y="total_bill",data=ma,kind="reg")


# ## pair plot

# In[26]:


sns.pairplot(ma)


# In[32]:


ga=sns.load_dataset("flights")


# In[33]:


ga


# In[34]:


sns.pairplot(ga)
plt.show()


# In[35]:


ma["smoker"].value_counts()


# In[36]:


sns.pairplot(ma,hue="smoker")


# In[37]:


sns.pairplot(ma,hue="sex")


# ## dist plot

# In[38]:


sns.distplot(ma["tip"])


# In[39]:


sns.distplot(ma["tip"],kde=False,bins=10)


# ## categorical plot

# In[40]:


sns.countplot("sex",data=ma)


# In[41]:


sns.countplot("smoker",data=ma)


# In[42]:


sns.countplot("day",data=ma)


# In[43]:


sns.countplot(y="day",data=ma)


# ## Bar plot

# In[44]:


sns.barplot(y="total_bill",x="smoker",data=ma)


# In[46]:


sns.barplot(x="sex",y="total_bill",data=ma)


# ## Box plot

# In[47]:


sns.boxplot("smoker","total_bill",data=ma)


# In[48]:


sns.boxplot(x="day",y="total_bill",data=ma,palette="rainbow")


# In[49]:


sns.boxplot(x="day",y="total_bill",data=ma)


# In[50]:


sns.boxplot(data=ma,orient="v")


# In[51]:


sns.boxplot(x="total_bill",y="day",hue="smoker",data=ma)


# ## violin plot

# In[52]:


sns.violinplot(x="total_bill",y="day",data=ma,palette="rainbow")


# In[ ]:
print("gan")





# In[ ]:





# In[ ]:




