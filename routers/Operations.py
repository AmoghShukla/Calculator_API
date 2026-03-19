from fastapi import APIRouter
from schema.Validation import Input_Validator, Output_Validator
from service import Logic

router = APIRouter()

@router.get("/add/{Num1}/{Num2}")
def Addition(Num1 : float, Num2 : float):
    return Logic.addition(Num1, Num2)

@router.get("/sub/{Num1}/{Num2}")
def Subtraction(Num1 : float, Num2 : float):
    return Logic.subtract(Num1, Num2)

@router.get("/mul/{Num1}/{Num2}")
def Multiplication(Num1 : float, Num2 : float):
    return Logic.multiply(Num1, Num2)