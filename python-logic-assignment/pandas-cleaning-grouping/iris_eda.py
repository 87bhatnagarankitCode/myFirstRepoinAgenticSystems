import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv("IRIS.csv")
print(df.info())
print(">>",df.describe(include="all"))
print("1st 10 records", df.head(10))
print("last  records", df.tail())
print(df.columns)

print(df.index)
#
print(df.isnull().sum())

print("shape>>",df.shape)

print("size>>",df.size)

print("Unique>>",df["species"].unique())

# Observation: The histogram shows that Iris-setosa has a much smaller petal length 
# (1-2cm) compared to the other two species, making it easily identifiable.




px.histogram(df,x="petal_length",color="species",color_discrete_sequence=["teal","blue","red"]).show()


#Observation: By using a box plot,  points below the lower fence (like the one at 3.0 for Versicolor) are 
# identified as outliers.


# Create a box plot to find outliers in petal_length

px.box(df, x="species", y="petal_length", color="species", 
             # Shows all individual data points next to the box
             title="Identifying Petal Length Outliers by Species").show()


# Observation:  
# Setosa forms a completely separate cluster, while Versicolor and Virginica 
# show some overlap but remain distinct groups.



px.scatter(df,x="petal_length",y="petal_width",color="species", title="petal_length VS petal_width ").show()

