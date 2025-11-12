from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict
class Info(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float
    height : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi 
   


def update_data(info : Info):
    print(info.name)
    print(info.age)
    print(info.allergies)
    print(info.email)
    print("BMI",info.bmi)
    print("Insert to database")

    
info_person = {"name" : "Nam",'email' : 'abc@gamil.com', "age" : '20',"weight" : 60.5, "height" : "1.75", "married" : False, "allergies" : ['pollen','dust'], "contact_details" : {'phone' : '08388323'}}
person1 = Info(**info_person)

update_data(person1)