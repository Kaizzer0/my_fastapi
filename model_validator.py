from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict
class Info(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Person older than 60 must have an emergency contact")
        return model


def update_data(info : Info):
    print(info.name)
    print(info.age)
    print(info.allergies)
    print(info.email)
    print("Insert to database")

    
info_person = {"name" : "Nam",'email' : 'abc@hdfc.com', "age" : '70',"weight" : 60.5, "married" : False, "allergies" : ['pollen','dust'], "contact_details" : {'phone' : '08388323','emergency' : 14242141}}
person1 = Info(**info_person)

update_data(person1)