import plotly.express as px

#figuries são figuras, quadros por assim dizer que representam um quadro

fig = px.line(x=["a","b","c"], y=[1,3,2], title="sample figure")
print(fig)
fig.show()

if __name__ == "__main__":
    print('ola mundo')