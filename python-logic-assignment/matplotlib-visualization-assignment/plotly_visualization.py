
import pandas as pd
import numpy as np
import plotly.express as px


epoch = list(range(1,11))
loss  = np.linspace(0.99,0.36,10)

df = pd.DataFrame({
            "Epoch" : epoch,
            "Loss"  : loss

})

#print(df.info(),"####\n",df.describe())


fig = px.line(df,"Epoch","Loss",title="Training Loss Over Epochs",
              labels={"Epoch": "Epoch Number", "Loss": "Training Loss"},  markers=True ,text= "Loss"
)
fig.update_traces(textposition="top center")
fig.add_annotation(
    x=df["Epoch"].iloc[-1],      # X-coordinate (last Epoch)
    y=df["Loss"].iloc[-1],       # Y-coordinate (last Loss)
    text="Final Model State",    # The annotation text
    showarrow=True,              # Display an arrow pointing to the data
    arrowhead=2,
    ax=-50,                      # X-offset for the text box
    ay=-40                       # Y-offset for the text box
)


fig.add_annotation(
    x=df["Epoch"].iloc[-1],      # X-coordinate (last Epoch)
    y=df["Loss"].iloc[-1],       # Y-coordinate (last Loss)
    text="stable loss",    # The annotation text
    showarrow=True,              # Display an arrow pointing to the data
    arrowhead=4,
    arrowcolor="red",
    ax=50,                      # X-offset for the text box
    ay=40                       # Y-offset for the text box
)


fig.add_annotation(
    x=df["Epoch"].iloc[0], 
    y=df["Loss"].iloc[0],
    text="Initial Loss",
    showarrow=True, arrowhead=1, ax=40, ay=-30
)

fig.show()