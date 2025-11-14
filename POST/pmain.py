from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
import json
from typing import Annotated,Literal

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description='id of the patient',examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of patient')]
    age: Annotated[int,Field(...,gt=0,lt=100, description='Age of patient')] 
    city: Annotated[str, Field(..., description='City of patient where are they living')]
    gender: Annotated[Literal['male', 'female','other'],Field(..., description='Gender of patient')]
    height: Annotated[float, Field(...,gt=0, description='Height of patient (m)')]
    weight: Annotated[float, Field(...,gt=0, description='Weight of patient (kg)')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18:
            return 'underweight'
        elif self.bmi < 30:
            return 'normal'
        else:
            return 'obesity'



def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)

@app.get("/")
def hello():
    return {'message':'patient management system API'}

@app.get("/about")
def about():
    return {'message':'a fully functional API to manage infomation'}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/info/{id}")
def view_id(id : str = Path(..., description="ID of an patient in DB",example="P001")):
    data = load_data()
    if id in data:
        return data[id]
    raise HTTPException(status_code =404, detail="ID not found")


@app.get("/sort")
def sort_id(sort_by: str = Query(..., description="sort by height,weight,.."), order: str = Query("asc", description="sort by asc or desc order")):
    valid_field = ['name', 'city', 'age', 'gender','height','weight','bmi','verdict']
    
    
    if sort_by not in valid_field:
        raise HTTPException(status_code=400, detail=f"invalid selection from {valid_field}")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="invalid select asc or desc")
    
    data = load_data()
    
    sort_oder = True if order == "desc" else False

    sort_data = sorted(
        data.values(),

        key=lambda x: x.get(sort_by, 0),
        reverse = sort_oder
    )
    
    return sort_data

@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()

    # check if exist
    if patient.id in data:
        raise HTTPException(status_code=400, detail='patient already exists')


    data[patient.id] = patient.model_dump(exclude=['id']) #add new patient in DB
    save_data(data)

    return JSONResponse(status_code=201,content={'message' : 'patient created successfully'})