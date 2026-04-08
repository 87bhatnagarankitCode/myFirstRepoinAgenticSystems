import os

import requests
import pandas as pd
import plotly.express as px

URL = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(URL)

data = response.json()

#print(data)
os.system('cls')
data_frame = pd.DataFrame(data)
print(data_frame.head())
print("**"*60)
print(data_frame.info())
print("**"*60)
print(data_frame.describe())
print("**"*60)
print(data_frame.describe(include='all'))
print("before",data_frame.columns)
data_frame = data_frame.rename(columns={"userId": "user_id"})
print("renamed",data_frame.columns)
#data_frame = data_frame.drop(columns='id')
data_frame = data_frame.drop('id', axis= 1)
print("dropped",data_frame.columns)
post_per_user = data_frame.groupby("user_id").count()
print(" Post per user \n", post_per_user)
data_frame.reset_index()
data_frame['post_length'] = data_frame['body'].str.len()
data_frame['post_length_by_Lambda'] =  data_frame['body'].apply(len)
print(data_frame.head(30))

px.bar(post_per_user,x =post_per_user.index, y= 'body', color= post_per_user.index, color_discrete_sequence=['teal'], title="Posts per User").show()


px.histogram(data_frame,x='post_length',labels={'post_length': 'Characters', 'count': 'Frequency'},
             color='post_length',title ='post length', color_discrete_sequence=['teal','red','yellow','grey']).show()

