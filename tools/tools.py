from core.state import STATE

def food_output(food: str):
    return STATE[food]
    
def fat_checker(food: str):
    return STATE[food] + "the food can be bad for you if its more than a hundred because the food fat s hight."

def food_validator(food: str):
    
    if food in STATE:
        return("this food is in the state")
    else:
        return ("error 404 not valid")