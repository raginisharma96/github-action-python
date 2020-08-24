from src.welcome import greet
from src.ageLimit import validateAge

def test_greet():
    name = "Emma"
    output = "Welcome to the year 2020, Emma"
    assert(greet(name) == output)

def test_validateAge():
    age1 = 20
    age2 = 14
    output1 = True
    output2 = False
    assert(validateAge(age1) == output1)
    assert(validateAge(age2) == output2)