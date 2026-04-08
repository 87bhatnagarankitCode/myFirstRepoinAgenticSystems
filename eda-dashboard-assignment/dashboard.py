from fetch_data import data_frame, post_per_user
import streamlit as st
import os
import plotly.express as px

os.system('cls')

#print(data_frame)


st.set_page_config(page_title="Post Analytics", layout="wide")
st.title("📊 JSONPlaceholder Analysis Dashboard")



st.write("Showing Post Data")

st.dataframe(data_frame.head(20))



st.subheader("Filter by user")
user = st.selectbox("Select User", data_frame["user_id"].unique()) 
user_df = data_frame[data_frame["user_id"] == user] #
st.write(user_df)



st.subheader("Post Length Distribution")
fig = px.histogram(data_frame, x="post_length")
st.plotly_chart(fig)


st.subheader("Post per user ")
fig1 = px.bar(post_per_user,x =post_per_user.index, y= 'body', color= post_per_user.index, color_discrete_sequence=['teal','red'], title="Posts per User")
st.plotly_chart(fig1)
