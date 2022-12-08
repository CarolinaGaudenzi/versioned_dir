#!/usr/bin/env python
# coding: utf-8

# ![lter_penguins.png](attachment:lter_penguins.png)

# # 1. Introduction
# The palmerpenguins data contain size measurements for three penguin species – Adelie, Chinstrap, and Gentoo – observed on three islands – Torgersen, Dream, and Biscoe – in the Palmer Archipelago, Antarctica. 
# The data were collected from 2007 to 2009 by Dr. Kristen Gorman with the Palmer Station Long Term Ecological Research Program, part of the US Long Term Ecological Research Network.
# 
# Let's load the data and take a look at it.

# In[5]:


import pandas as pd
import seaborn as sns 
from palmerpenguins import load_penguins
sns.set_style('whitegrid')
penguins = load_penguins()
penguins.head()


# # 2. Descriptive analysis 
# Let's take a look at some of the characteristics of the Palmer penguin population.

# ## 2.1 How many male and female penguins are there? 

# In[50]:


penguins["sex"].value_counts(normalize=False) # how many males and females are in our dataset
penguins['sex'].isna().sum() # how many penguins were not assigned a gender
graph = sns.countplot(x=penguins['sex'],
                   order=penguins['sex'].value_counts(ascending=True).index);

abs_values = penguins['sex'].value_counts(ascending=False).values

graph.bar_label(container=graph.containers[0], labels=abs_values)
import matplotlib.pyplot as plt
plt.show()


# ## 2.2 How do population numbers change over the years?

# In[41]:


penguins["year"].value_counts(normalize=False) # identify how many datapoints there is per year
penguins['year'].isna().sum() # check whether there are any missing values in the year variable
graph = sns.countplot(x=penguins['year'],
                   order=penguins['year'].value_counts(ascending=True).index);

abs_values = penguins['year'].value_counts(ascending=False).values
plt.show()


# ## 2.3 What are the physical characteristics of the population?

# In[44]:


sns.catplot(data=penguins, x="species", y="body_mass_g", kind="box")
sns.catplot(data=penguins, x="species", y="bill_length_mm", kind="box")
plt.show()


# ## 2.4 What is the distribution of the different species across the islands?

# In[31]:


sns.displot(data=penguins, x="species", hue="island", stat="count", common_norm=False)
plt.show()


# ## 2.5. Is there a difference in physical characteristics among the species?

# In[45]:


graph = sns.boxplot(data = penguins, 
                    x = 'island',
                    y = "body_mass_g", 
                    hue = "species")
graph.set_xlabel("Island")
graph.set_ylabel("Body Mass (g)")
graph.set_title("Body Mass")
plt.show()


# In[35]:


graph2 = sns.boxplot(data = penguins, 
                    x = 'island',
                    y = "bill_length_mm", 
                    hue = "species")
graph2.set_xlabel("Island")
graph2.set_ylabel("Bill Length (mm)")#
graph2.set_title("Bill Length")
plt.show()


# In[36]:


graph3 = sns.boxplot(data = penguins, 
                    x = 'island',
                    y = "flipper_length_mm", 
                    hue = "species")
graph3.set_xlabel("Island")
graph3.set_ylabel("Flipper Length (mm)")
graph3.set_title("Flipper Length")
plt.show()


# ## 2.6. Is there a difference in physical characteristics according to sex and time?

# In[46]:


mass_year_sex = sns.catplot(x="year",
               y="body_mass_g",
               hue="sex",
               data=penguins,
           kind="bar")
mass_year_sex.set_axis_labels("year", "body mass (g)")
plt.show()


# 

# In[ ]:




