from pydantic import BaseModel

class User(BaseModel):
    id:int
    age:int
    name:str


data = {
    "id":1,
    "age":20,
    "name": "ram"
}

user = User(**data)

class Item:
    price: float
    quantity: int

item = Item(price='19.99', quantity='2')
print(item.price * item.quantity)  # 39.98


def fun(*args,**kwargs):
    print(args)
    print(kwargs)
if __name__=="__main__":
    print(user)
    fun(1,2,name="ram",age=23)