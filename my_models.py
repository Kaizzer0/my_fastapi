from pydantic import BaseModel

class Info(BaseModel):
    name : str
    age : int
    

#logic 
def insert_data(info : Info):
    print(info.name)
    print(info.age)
    print("Insert to database")

    
info_person = {"name" : "Nam", "age" : 20}
person1 = Info(**info_person)

insert_data(person1)