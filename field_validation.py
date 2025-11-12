from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated
class Info(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value): #value = email : EmailStr
        valid_domains = ['hdfc.com', 'icici.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("age should between 0 and 100")


def update_data(info : Info):
    print(info.name)
    print(info.age)
    print(info.allergies)
    print(info.email)
    print("Insert to database")

    
info_person = {"name" : "Nam",'email' : 'abc@hdfc.com', "age" : '20',"weight" : 60.5, "married" : False, "allergies" : ['pollen','dust'], "contact_details" : {'phone' : '08388323'}}
person1 = Info(**info_person)

update_data(person1)