from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from src.welcome import greet
from src.ageLimit import validateAge

app = FastAPI()

class RequestJson1(BaseModel):
    name:str

class RequestJson2(BaseModel):
    age:int


@app.post("/welcome")
def welcome(requestJson:RequestJson1):
    welcomeString = greet(requestJson.name)
    response = {"output":welcomeString}

    return response

@app.post("/validateAge")
def ageLimit(requestJson:RequestJson2):
    age = validateAge(requestJson.age)
    if age == True:
        response = {"output":"You are eligible."}
    else:
        response = {"output":"You are not eligible."}

    return response

