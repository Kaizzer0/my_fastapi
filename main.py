from fastapi import FastAPI
import json
app = FastAPI()

def load_data():
    with open("duc.json", "r",encoding="utf-8") as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {'message':'my API management system'}

@app.get("/about")
def about():
    return {'message':'a fully functional API to manage my infomation'}

@app.get("/view")
def view():
    data = load_data()
    return data