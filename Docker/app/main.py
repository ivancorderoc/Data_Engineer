from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
import pandas as pd
import matplotlib.pyplot as plt

app = FastAPI()

@app.get("/")
async def inicio():
    return "Work in progress!!"

@app.get("/obtener-iris")
def obtener_iris():
    open_file ='/Users/ivanlamb/Documents/GitHub/Data_Engineer/Docker/app/iris.csv'
    iris = pd.read_csv(open_file)
    return iris.to_dict(orient='records')

@app.get("/graficar-iris")
async def graficar_iris():
    open_file ='/Users/ivanlamb/Documents/GitHub/Data_Engineer/Docker/app/iris.csv'
    iris = pd.read_csv(open_file)

    plt.scatter(iris['sepal_length'], iris['sepal_width'])
    plt.savefig('iris.png')
    with open('iris.png', mode="rb") as file:
        contents = file.read()

    return StreamingResponse(contents, media_type="image/png")

