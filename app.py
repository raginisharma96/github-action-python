from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from src.welcome import greet

app = FastAPI()

class RequestJson(BaseModel):
    name:str


@app.post("/welcome")
def welcome(requestJson:RequestJson):
    welcomeString = greet(requestJson.name)
    response = {"output":welcomeString}

    return response
