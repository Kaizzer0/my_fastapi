from pydantic import BaseModel

class Address(BaseModel):
    city: str
    country: str
    pin : str

class Patient(BaseModel):
    name: str
    age: int
    address: Address


address_dict = {'city' : 'HCM' , 'country' : 'VietNam', 'pin' : '90000'}
address1 = Address(**address_dict)

patient_dict = {'name' : 'Baki', 'age' : 25, "address" : address1}
patient1 = Patient(**patient_dict)
print(patient1)