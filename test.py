from src.welcome import greet

def test_greet():
    name = "Emma"
    output = "Welcome to the year 2020, Emma"
    assert(greet(name) == output)