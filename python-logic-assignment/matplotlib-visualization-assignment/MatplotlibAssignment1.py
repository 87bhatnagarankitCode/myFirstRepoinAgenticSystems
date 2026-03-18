
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

#10 epochs

epochs = np.arange(1,11,1)

#loss
loss = np.linspace(0,10,10)+np.random.rand(10)

print(epochs)
print(loss)
data = {
        "epoch" : epochs ,
        "loss" : loss
}

#df = 
#line plot
plt.figure(figsize=(8, 5))
plt.plot(epochs,loss, marker ="h", linestyle='dashdot',label ="Training Loss")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.title("Loss vs Epoch")
for i in range(len(epochs)):
    plt.text(epochs[i],loss[i],f"{loss[i]:.2f}",fontsize=8, ha="left", va="bottom",rotation=45)
plt.grid(True)
plt.legend()
plt.show()
plt.figure(figsize=(8, 5))
plt.scatter(loss,epochs, marker ="h", color='red',label ="Training Loss")
plt.xlabel("loss")
plt.ylabel("epochs")
plt.title("Epochs Vs Loss")
for i in range(len(epochs)):
    plt.text(loss[i],epochs[i],f"{loss[i]:.2f}",fontsize=8, ha="left", va="bottom",rotation=45)
plt.grid(True)
plt.legend()
plt.show()

Models = {
        "Model A": 0.85,
        "Model B": 0.90,
        "Model C": 0.88
}


modelName = Models.keys()
accuracy  = Models.values()
print(type(accuracy))
listaccuracy= list(accuracy)
plt.figure(figsize=(8, 5))
plt.bar(modelName,accuracy,color=["skyblue","orange","yellow"])
for i in range(len(listaccuracy)):
    plt.text(i,listaccuracy[i],str(listaccuracy[i]),color ="red",rotation =45,ha="center", va="bottom", fontsize=8)
#plt.text
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.title("Model Accuracy chart")
#plt.legend()
plt.grid(True)
plt.show()
