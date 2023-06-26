#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip freeze | grep scikit-learn')


# In[2]:


import pickle
import pandas as pd


# In[3]:


with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


# In[4]:


categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


# In[6]:


df = read_data('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-02.parquet')


# In[7]:


dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = model.predict(X_val)


# # Q1. Notebook
# 

# In[10]:


print(f"The standard deviation of the predicted duration of this dataset is {y_pred.std()}")


# # Q2. Preparing the output
# 

# In[18]:


year = 2022
month = 2
output_file = f"output_yellow_tripdata_{year:04d}-{month:02d}.parquet"

df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')

df_result = pd.DataFrame({'ride_id' : df['ride_id'], 'preds' :  y_pred})

df_result.to_parquet(
    output_file,
    engine='pyarrow',
    compression=None,
    index=False
)


# In[25]:


from pathlib import Path

print(f"The size of the output file is {Path(output_file).stat().st_size / (1024 * 1024):2f}")


# # Q3. Creating the scoring script
# 

# In[ ]:




