from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel  

# create an instance of the FastAPI class
app = FastAPI()

# we are gonna define a class, this will tell us what a post should look like.
# we are inherting the base model, it gonna exted base model.
class Post(BaseModel):
    title : str
    content : str


# path operation decorator to define the endpoint and HTTP method
@app.get("/")
async def greet():
    return {"Hello": "World"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}

@app.post("/createposts")
# in order to store the body data, we need to define a variable in our method.
# the fast api will convert the json into dict & store it in payload variable
# so now we use pydantic to give schema on how we want the body to look like - 
# we want : 
    # title : str & content : str, category, 
# def create_post(payload : dict = Body(...)): # type: ignore # <---- old way
def create_post(new_post : Post): # type: ignore
    """used to create post"""
    # print(new_post) # it works
    # to access individually we can do ; post.title & post.content
    print(new_post.title, '\n', new_post.content)
    return {"data" : "new post"}

# now you can head to post man & modify the body to remove the title & see the validaton being done by pydantic, it will throw an error saying title is required.


    