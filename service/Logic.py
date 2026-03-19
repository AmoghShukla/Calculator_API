from fastapi import HTTPException

def addition(Value1, Value2):
    result = Value1 + Value2
    return {"Output_Value" : result}

def subtract(Value1, Value2):
    result = Value1 - Value2
    return {"Output_Value" : result}

def multiply(Value1, Value2):
    result = Value1 * Value2
    return {"Output_Value" : result}

def divide(Value1, Value2):
    if Value2 == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    result = Value1 / Value2
    return {"Output_Value" : result}