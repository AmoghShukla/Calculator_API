from fastapi import APIRouter
from schema.Validation import Input_Validator, Output_Validator
from service import Logic

router = APIRouter()

@router.get("/add/{Num1}/{Num2}")
def Addition(Num1 : float, Num2 : float):
    return Logic.addition(Num1, Num2)