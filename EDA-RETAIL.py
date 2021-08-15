#!/usr/bin/env python
# coding: utf-8

# ## THE SPARKS FOUNDATION #GRIPAUGUST21 
# ###  Name- Ishan Tyagi , DATA SCIENCE & BUSINESS ANALYTICS INTERN(AUG 21)
# ### TASK-3 EXPLORATORY DATA ANALYSIS -RETAIL 
#      Level-Beginner
#      Perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’
#      Dataset sample :https://bit.ly/3i4rbWl
# 

# In[32]:


#Importing Libraries

import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns


# In[33]:


#Reading dataset

store_df=pd.read_csv('SampleSuperstore.csv')


# In[34]:


type(store_df)


# In[35]:


store_df


# In[36]:


store_df.head()


# In[37]:


store_df.tail()


# In[38]:


# Finding duplicate values
dup_r=store_df[store_df.duplicated()]


# In[39]:


dup_r


# In[40]:


#Checking for missing values if exist in dataset
store_df.notnull()


# In[41]:


store_df.isnull()


# In[42]:


# sum of null values if found
store_df.isnull().sum()


# In[43]:


store_df.isna().sum()


# In[44]:


# Dropping the duplicates found in dataset
stores_df=store_df.drop_duplicates()


# In[45]:


# After dropping the duplicates rows became 9977 from 9994
stores_df


# In[46]:


# Checking unique values 
stores_df.nunique()


# In[47]:


# defining rows and coloumns for dataset
stores_df.shape


# In[48]:


#Statistical table for numeric attributes
stores_df.describe()


# In[49]:


#grouping only numeric attributes to new dataframe
sca_df=stores_df[['Postal Code','Sales','Quantity','Discount','Profit']]


# In[50]:


sca_df


# In[51]:


stores_df.columns


# In[52]:


# Extracting region coloumn from stores_df dataset
tstores_df=stores_df['Region'].unique()


# In[53]:


tstores_df


# In[54]:


# Grouping region according to total quantity, sales, profit. 
stores_reg_df = stores_df.groupby('Region')[['Quantity','Sales','Profit']].sum()


# In[55]:


stores_reg_df


# In[56]:


stores_reg_df.Quantity


# In[57]:


stores_df.Category.unique()


# In[58]:


data = {'Central':8768, 'East':10609, 'South':6209,
        'West':12234}
region = list(data.keys())
quant= list(data.values())
fig = plt.figure(figsize = (10, 5))
plt.bar(region, quant, color ='maroon',
        width = 0.4)
 
plt.xlabel("Region types")
plt.ylabel("count of total no of quantities in total sales transaction for each region")
plt.title("REGION VS TOTAL QUANTITY")
plt.show()


# In[59]:


stores_df.Category.unique()


# ##### VISUALIZING  CATEGORY COLOUMN 

# In[60]:


plt.figure(figsize = (12,6))
sns.countplot(x = 'Category', data = stores_df, palette= ["#a31830","#07e053", "#e37500"])
plt.title('Category types')
plt.xticks(rotation = 90);


# #### The most ordered category is Office Supplies and least is Technology

# In[61]:


#sales vs profit
fig, ax = plt.subplots(figsize = (10 , 6))
ax.scatter(stores_df["Sales"] , stores_df["Profit"])
ax.set_xlabel('Sales')
ax.set_ylabel('Profit')
plt.show()


# #### VISUALIZING SEGMENT COLUMN

# In[62]:


s_df=list(stores_df['Segment'].value_counts())


# In[63]:


s_df


# In[64]:


l_df=list(stores_df['Segment'].value_counts().keys())


# In[65]:


l_df


# In[66]:


plt.pie(s_df,labels=l_df,radius=1.5,autopct='%0.2f%%')
plt.show()


# #### From the above chart Consumer segment has the highest purchases with 51.95%  and Home office has the least with 17.83% 

# In[67]:


#total sum of sales coloumn
sum(stores_df['Sales'])


# In[68]:


#count of each subcategory item
stores_df.Subcategory.value_counts()


# In[69]:


stores_df.Subcategory.unique()


# In[70]:


#total count of each item sold using graph
plt.figure(figsize = (10,5))
sns.countplot(x = 'Subcategory', data = stores_df,palette= ["#a31830","#07e053", "#e37500"])
plt.title('Types of Subcategory')
plt.xticks(rotation = 90);


# #### Max no of items sold were binders and least  are Copiers

# #### Total Profit Made by each of subcategories

# In[71]:


stores_dfBinder = stores_df[stores_df['Subcategory']=='Binders']
binder_df=sum(stores_dfBinder['Profit'])


# In[72]:


binder_df


# In[73]:


stores_dfSupply = stores_df[stores_df['Subcategory']=='Supplies']
supplies_df=sum(stores_dfSupply['Profit'])


# In[74]:


supplies_df


# In[75]:


stores_dfpper = stores_df[stores_df['Subcategory']=='Paper']
paper_df=sum(stores_dfpper['Profit'])


# In[76]:


paper_df


# In[77]:


stores_dfcop = stores_df[stores_df['Subcategory']=='Copiers']
cop_df=sum(stores_dfcop['Profit'])


# In[78]:


cop_df


# In[79]:


stores_dfmac = stores_df[stores_df['Subcategory']=='Machines']
mach_df=sum(stores_dfmac['Profit'])


# In[80]:


mach_df


# In[81]:


stores_dfbkc = stores_df[stores_df['Subcategory']=='Bookcases']
bkc_df=sum(stores_dfbkc['Profit'])


# In[82]:


bkc_df


# In[83]:


stores_dflb = stores_df[stores_df['Subcategory']=='Labels']
lb_df=sum(stores_dflb['Profit'])


# In[84]:


lb_df


# In[85]:


stores_dftab = stores_df[stores_df['Subcategory']=='Tables']
tab_df=sum(stores_dftab['Profit'])
tab_df


# In[86]:


stores_dfstr = stores_df[stores_df['Subcategory']=='Storage']
str_df=sum(stores_dfstr['Profit'])
str_df


# In[87]:


stores_dffur = stores_df[stores_df['Subcategory']=='Furnishings']
fur_df=sum(stores_dffur['Profit'])
fur_df


# In[88]:


stores_dfar = stores_df[stores_df['Subcategory']=='Art']
art_df=sum(stores_dfar['Profit'])
art_df


# In[89]:


stores_dfph = stores_df[stores_df['Subcategory']=='Phones']
ph_df=sum(stores_dfph['Profit'])
ph_df


# In[90]:


stores_dfch = stores_df[stores_df['Subcategory']=='Chairs']
chr_df=sum(stores_dfch['Profit'])
chr_df


# In[91]:


stores_dfen = stores_df[stores_df['Subcategory']=='Envelopes']
env_df=sum(stores_dfen['Profit'])
env_df


# In[92]:


stores_dfacc = stores_df[stores_df['Subcategory']=='Accessories']
acc_df=sum(stores_dfacc['Profit'])
acc_df


# In[93]:


stores_dffast = stores_df[stores_df['Subcategory']=='Fasteners']
fast_df=sum(stores_dffast['Profit'])
fast_df


# In[94]:


stores_dfapp = stores_df[stores_df['Subcategory']=='Appliances']
app_df=sum(stores_dfapp['Profit'])


# In[95]:


app_df


# In[96]:


#Grouping all dataframes into one
subcc_df=[app_df,fast_df,acc_df,env_df,chr_df,ph_df,art_df,fur_df,str_df,tab_df,lb_df,bkc_df,mach_df,cop_df,paper_df,supplies_df,binder_df]


# In[97]:


subcc_df


# In[98]:


data = {"Subcategories":['Appliances', 'Fasteners', 'Accessories', 'Envelopes', 'Chairs',
       'Phones', 'Art',  'Furnishings', 'Storage', 'Tables',
       'Labels', 'Bookcases', 'Machines', 'Copiers','Paper',
       'Supplies','Binders' ],

        "Profit values":[18138.005399999995,
 949.5181999999998,
 41936.63569999993,
 6964.176700000003,
 26567.127800000024,
 44515.7306,
 6524.611799999999,
 13052.722999999984,
 21278.826399999998,
 -17725.481100000008,
 5526.381999999998,
 -3472.5559999999978,
 3384.7569,
 55617.82490000001,
 33944.23949999997,
 -1189.0994999999984,
 30228.000299999996]

        };


# In[99]:


dataFrame = pd.DataFrame(data=data);
dataFrame


# #### Visualizing profit wrt to every subcategory 

# In[100]:


dataFrame.plot.bar(x="Subcategories", y="Profit values",color='#a98d19', rot=80, title="value of profit");
plt.show(block=True);


# #### Tables , Bookcases,Supplies are items which are not gaining any profit

# ## CONCLUSION

# #### ->The furniture category has been resulting in huge loss ->table and bookcases.Therefore minimizing supply of furniture can reduce the loss to an extent.

# #### ->Central region has been least profitable compared to others .

# #### ->The most ordered category is binders and least is copiers.

# #### ->South region has the least no of  ordered items and west region the most ordered.

# #### ->The sales are mostly less than US 5000 Dollars.This is because of consumer segment that buys the majority with 51.95% compared to other segment which are from corporate and home offices who buy only few times for their office needs. A number of transactions which are under USD 2.5k or around results in a loss.

# In[ ]:




