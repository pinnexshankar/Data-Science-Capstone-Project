#!/usr/bin/env python
# coding: utf-8

# In[42]:

import streamlit as st
import pickle
import sklearn

# In[43]:


knn=pickle.load(open('Knn_model.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))


# In[44]:


st.title("Car Price Prediction")


# In[45]:


# Brand
Brand=st.selectbox('Brand',df['Car Brand'])
# model
model=st.selectbox('Car Model',df['name'])
# year
year=st.slider('select year',1990,2020)
# seller type
seller_type=st.selectbox('Seller type',df['seller_type'])
# fuel
fuel=st.selectbox('fuel',df['fuel'].unique())
# transmission
transmission=st.selectbox('transmission',df['transmission'].unique())
# km_driven
km_driven=st.selectbox('Km Driven',df['km_driven'].unique())
# owner
owner=st.selectbox('Owner',df['owner'].unique())


# In[46]:


query = np.array([model,Brand,year,seller_type,fuel,transmission,km_driven,owner])
query = query.reshape(1,8)
st.title("The predict price of this configuration is "+ str(int(knn.predict(query)[0])))

