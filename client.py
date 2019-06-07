import requests
import json
import datetime

BASE_URL = "http://127.0.0.1:5000"
barra="-----------------------------------------------------------------------------------"

def create_user():
    name="Luis Francisco"
    username="Jxey"
    email="luis008m@hotmail.com"
    password="123"
    json_body= {"name":name,"username":username,"email":email,"password":password}
    value1=requests.post(f"{BASE_URL}/create",json=json_body)
    #json_obj = value1.json()
    print(value1)
    #print(json_obj)

def get_user_info():
    pass

def list_posts():
    pass

def create_new_post():
    pass

create_user()