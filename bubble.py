import plotly.express as px
dt=px.data.iris()
fig=px.scatter(dt,x="sepal_width",y="sepal_length",color="species",size="petal_length",hover_data=["petal_length"],title="Iris Dataset:sepal width vs leength")
fig.show()
