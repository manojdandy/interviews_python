from typing import Final
from datetime import datetime

name:str="bob"
age:int = "dd"
VERSION:Final[str] = "1.0.0"
VERSION = "1.0.1"
print(VERSION)
print(name,age)


def show_date() -> None:
    print(datetime.now())


show_date()