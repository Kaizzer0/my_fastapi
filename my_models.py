from pydantic import BaseModel,EmailStr,AnyUrl,Field    
from typing import List,Dict,Optional,Annotated
class Info(BaseModel):
    name : Annotated[str, Field(max_length=50, title='Name of 1 person',description='Give the name less than 50 character',examples=['Ben','Armish'])]
    email : EmailStr
    linkedin_url : AnyUrl
    age : int = Field(gt = 0,lt = 60)
    weight : Annotated[float,Field(gt=0, strict= True)]
    married : Annotated[bool, Field(default=None, description='married or not')]
    allergies : Annotated[Optional[List[str]] , Field(default=None,max_length=5)]
    contact_details : Dict[str, str]

#logic 
def insert_data(info : Info):
    print(info.name)
    print(info.age)
    print(info.allergies)
    print(info.married)
    print("Insert to database")

    
info_person = {"name" : "Nam",'email' : 'abc@gmail.com',"linkedin_url" : "http://linkedin.com/9884", "age" : 20,"weight" : 60.5,"allergies" : ['pollen','dust'], "contact_details" : {'phone' : '08388323'}}
person1 = Info(**info_person)

insert_data(person1)