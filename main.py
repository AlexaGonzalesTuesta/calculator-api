from fastapi import FastAPI, status, HTTPException


app = FastAPI()


@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a: str, b: str):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both a and b must be valid numbers")

    return {"result": a + b}

@app.get("/subtract/{a}/{b}", status_code=200)
def subtract(a: str, b: str):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both a and b must be valid numbers")

    return {"result": a - b}

@app.get("/multiply/{a}/{b}", status_code=200)
def multiply(a: str, b: str):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both a and b must be valid numbers")
    return {"result": a * b}

@app.get("/divide/{a}/{b}", status_code=200)
def divide(a: str, b: str):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both a and b must be valid numbers")
    if (b == 0):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Cannot divide by zero")
    return {"result": a / b}