#!/usr/bin/env python
# coding: utf-8

# In[1]:


#use pymysql


# In[1]:


pip install mysql-connector-python


# In[1]:


import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Connect to server + specific database
cnx = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="admin@123",
    database="banking_case"   # 👈 replace with your DB name
)

# Run a query and load into pandas
query = "SELECT * FROM customer"   # 👈 replace with your table name
df = pd.read_sql(query, cnx)

print(df.head(5))


# In[18]:


#Generating descriptive statistics(numerical) for the dataframe
df.describe()


# In[19]:


df.info()


# In[24]:


df.shape


# In[4]:


df['Estimated Income'].min()


# In[8]:


bins = [0, 100000, 300000,float('inf')]
labels = ['Low', 'Med', 'High']

df['Income Band'] = pd.cut(df['Estimated Income'], bins= bins, labels= labels, right= False)


# In[12]:





# In[ ]:


# Examine the distribution of unique categories in categorial columns
categorial_cols = df[["BRId", "GenderId","IAId", "Amount of Credit Cards", "Nationality","Occupation","Fee Structure", "Loyalty Classification","Properties Owned", "Risk Weighting","Income Band"]].columns

for col in categorial_cols:
    print(f"Value Counts for '{col}':")
    display(df[col].value_counts())


# # univariate Analysis
# 

# In[20]:


for i, predictor in enumerate(df[["BRId", "GenderId","IAId", "Amount of Credit Cards", "Nationality","Occupation","Fee Structure", "Loyalty Classification","Properties Owned", "Risk Weighting","Income Band"]].columns):
    plt.figure(i)
    sns.countplot(data=df, x= predictor)


# In[22]:


for i, predictor in enumerate(df[["BRId", "GenderId","IAId", "Amount of Credit Cards", "Nationality","Occupation","Fee Structure", "Loyalty Classification","Properties Owned", "Risk Weighting","Income Band"]].columns):
    plt.figure(i)
    sns.countplot(data=df, x= predictor, hue='Nationality')


# In[24]:


# Histplot of value counts for different Occupation
 
for col in categorial_cols:
    if col == "Occupation":
        continue
    plt.figure(figsize=(8,4))
    sns.histplot(df[col])
    plt.title('Histogram of Occupation Count')
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.show()


# # Numerical Analysis

# In[2]:


numerical_cols = ['Fee Structure','Age', 'Estimated Income', 'Superannuation Savings', 'Credit Card Balance', 'Bank Loans', 'Bank Deposits', 'Checking Accounts', 'Saving Accounts', 'Foreign Currency Account', 'Business Lending']

# Univariate analysis and visualization
plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols):
    plt.subplot(4, 3, i + 1)
    sns.histplot(df[col], kde=True)
    plt.title(col)
plt.tight_layout()
plt.show()


# In[4]:


# Select numerical columns for correlation analysis
numerical_cols = ['Age', 'Estimated Income', 'Superannuation Savings', 'Credit Card Balance',
                  'Bank Loans', 'Bank Deposits', 'Checking Accounts', 'Saving Accounts',
                  'Foreign Currency Account', 'Business Lending', 'Properties Owned']

# Calculate the correlation matrix
correlation_matrix = df[numerical_cols].corr()

# Create a heatmap of the correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True,      , fmt=".2f")
plt.title('Correlation Matrix of Numerical Features')
plt.show()


# In[ ]:




