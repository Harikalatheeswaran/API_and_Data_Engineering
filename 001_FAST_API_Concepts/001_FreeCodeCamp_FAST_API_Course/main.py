from fastapi import FastAPI

# create an instance of the FastAPI class
app = FastAPI()

# path operation decorator to define the endpoint and HTTP method
@app.get("/")
async def greet():
    return {"Hello": "World"}
