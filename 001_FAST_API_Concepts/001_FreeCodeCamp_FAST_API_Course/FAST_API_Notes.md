
---
# <div align=center> *__Python API Development - Comprehensive Course for Beginners__* </div>
---

- Link to Video 👉 [Link](https://www.youtube.com/watch?v=0sOvCWFmrtA)
- Taught by Sanjeev Thigarajan
- FAST API docs : [FAST_API_DOCs](https://fastapi.tiangolo.com/)
## Overview
- Building API which uses
    1. Authentication
    2. CRUD operation
    3. Validation
    4. Documentation
- SQL & ORMs
- Database migration tools : Alembic
- Postman : to construct HTTP packets to test API
- Automated Intergration Tests
- Deployment : 
    1. Deployment 
        - On Ubuntu on Cloud like AWS, Azure etc
        - Deploy on Heroku
        - Dockerize the API
    2. Nginx
    3. Setup firewall to block all non HTTP & set up SSL so that we handle HTTPS traffic
    4. Build our own CI/CD pipe lines using GitHub actions

- Tech Stack:
    1. Python
        - FAST API : which is fast, easy to use & comes with **`Auto Documentation`** Feature.
    2. SQL 
        - Postgres
        - SQL Alchemy for ORM.
    
---

## Contents : 
1. [Setting up Virtual Environment](#setting-up-virtual-environment)
    - [Fix venv problem](#grok-solution-to-fix-venv-activation----grok-solution-)
2. [Installing FAST API](#2-installing-fast-api)
3. [The Code]
---

### 1. *Setting Up Virtual environment.*

- This will enable us to run customized python packages isolated for other projects.
- We can install completely different versions of packages 
- Commad to create a virtual terminal : 
    ```bash
    python -m venv <name>
    # usually we give it as .venv
    ```
- This will create a `<name>` folder in out environment & under scripts you'll find we have a python interpreter instance for our isolated environment.
- Inorder to use this instance of the interpreter we need to activate it.
- Go to View > Command Palatte (Ctrl + Shift + P) > Select interpreter & type the following : 
    > .\venv\Scripts\python.exe
- Now make sure our terminal is also using the virtual environment, we go the path called of the "activate.bat" file inside scripts.
- Then open that in our terminal
    ```bash
    source .venv/bin/activat
    ```
    - Sometimes this might not work in windows, in such a case run : 
        ```bash
        Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
        # then 
        .\.venv\Scripts\Activate.ps1
        ```
#### Grok solution to fix venv activation : - GROK solution : 
- Hey buddy, this is a super common issue on Windows when trying to activate a Python **virtual environment** (`.venv`) in **PowerShell**. 

- PowerShell has a security setting called **Execution Policy** that's set to **Restricted** by default, which blocks running any `.ps1` scripts (like `Activate.ps1`).

 -  are the **best ways** to fix it, from safest/quickest to more permanent:

    ##### 1. Quickest fix (only for this terminal session – recommended first try)
    In your VS Code terminal (or PowerShell), run these two commands one after another:

    ```powershell
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
    .\.venv\Scripts\Activate.ps1
    ```

    - The first command only affects the current terminal (it resets when you close it).
    - The second one activates your venv (you should see `(.venv)` appear in your prompt).

    ##### 2. Best long-term fix (Recommended for most people)
    Run this **once** in PowerShell (you can do it in VS Code terminal):

    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```

    - Type `Y` or `A` when it asks for confirmation.
    - This allows **locally created scripts** (like your venv's Activate.ps1) to run, but still blocks unsigned scripts downloaded from the internet → pretty safe.
    - After this, just use the normal activation command:

    ```powershell
    .\.venv\Scripts\Activate.ps1
    ```

    (or simply `.\.venv\Scripts\Activate` – PowerShell usually figures it out).

    ##### 3. Alternative: Switch to Command Prompt (easiest if you don't want to change anything)
    In VS Code:
    - Click the dropdown arrow next to the terminal (where it says "PowerShell")
    - Select **Command Prompt** (`cmd.exe`)
    - Then activate with:

    ```cmd
    .venv\Scripts\activate.bat
    ```

    This avoids PowerShell completely and works without any policy changes.

    ##### Bonus tips:
    - Check your current policy anytime with: `Get-ExecutionPolicy`
    - After activating, your prompt should show `(.venv)` at the beginning.
    - If you're in the project folder, the path is usually just `.\.venv\Scripts\Activate.ps1`

---

### *2. Installing FAST API*

- we go to the documentation of the FAST API site : https://fastapi.tiangolo.com/
- Here we run the command to install all dependencies
    ```bash
    pip install fastapi[all]
    ```
- we run a :
    ```bash
    pip freeze 
    ```
    to see what all the packages that got installed.
- all the packages we installed will reside in the path : `.venv/Lib`

---

### *3. The Code*

- we import fast api & call the path operation decorator to define the endpoint and HTTP method.
- we use the `uvicorn` which is out web server to open our app.
- in our `main.py` we do : 
    ```python
    from fastapi import FastAPI

    # create an instance of the FastAPI class
    app = FastAPI()

    # path operation decorator to define the endpoint and HTTP method
    @app.get("/")
    async def root():
        return {"Hello": "World"}
    ```
- then we run :
    ```bash
    uvicorn main:app
    ```
- fast api if we return a dic, it will convert it to json
- after the decorator `@app` we pass in the HTTP method that the use should use, which is a `GET` method.
- What the `GET` method does is, it send a get request from out API
- By using the decorators, we can invoke path functions so that someone wo wants to use our API can hit this `end-point`
- When we run our app, it runs at local host : `http://127.0.0.1:8000/`
- in the decorator we give the parameter as `"/"`, this is the *`root path`* which is similar to our `http://127.0.0.1:8000/`
- if we enter the paratmeter say `"/login"`, it would be `http://127.0.0.1:8000/login`
- *NOTE*
    - Anychanges you do to the code, you need to *`restart`* the server to see the changes.
    - Pass in the *`--reload`* flag only in an `developer` environment.
- *Trick*
    - IF you want to **dynamically** show changes in our server we run as below 
        ```bash
        uvicorn main:app --reload
        ```
    - what this does is : when do the changes to main.py file, a command will be sent to automatically restart the server.
- we use the `get` HTTP request to fetch details.
- To more about the HTTP requests go to : https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- Now when you add this to your code :
    ```python
    @app.get("/posts")
    def get_posts():
        return {"data": "This is your post"}
    ```
- You will see that in the URL : `http://127.0.0.1:8000/posts`, it would be printed as :
    ```json
    {"data": "This is your post"}
    ```
- The way fastapi works is that, when we send a request to out API server:
    - it's going to go down the list of all of our path operations
    - it's going to find the first match & once it finds it stops. 
    - so if you have several `/post` path operations, it will go for the first one.
    - 

---

### *4. Testing API*
 - In order to test our API we need to send multiple requests & this cannot be done just using the browser.
 - We can do it by using a tool called `Postman`.
 - This tool allows us to `construct our own HTTP request`, this way we can specify the individual fields of an HTTP request.
 - 

### *5. Important Points*:
- HTTP GET request v/s POST
    - In a GET request, we send a request & the API send us some data.
    - In a POST request, along with the request we send `DATA` to the API, & API will send us some data.
    - We use POST request for "creating things", say we send a file to google drive, etc. 
    - How each request talk to the API server : 
        - GET : Hey API server, give me some data.
        - POST : Hey API server, here's soem data, do whatever you need to do with it. 
    - The whole idea behind the post request is to send data to the server. We do this in the `body` of the request.
    - In order to receive the data that the we need to do the following in out `path operation`:
        - follow the below method :
            ```python
            @app.post("/createposts")
            # in order to store the body data, we need to define a variable in our method.
            # the fast api will convert the json into dict & store it in payload variable
            def create_post(payload : dict = Body(...)): # type: ignore
                """used to create post"""
                print(payload) # it works
                return {"new_post" : 
                        {
                            'title' : payload['title'], 
                            'content' : payload['content']
                        }
                        }
            ```
    - Why we need schema : 
        1. Its a pain to get all the values from the body
        2. The client can send whatever data they want
        3. data is not getting validated. Eg what if a user sends a blank titile?...hence data needs to be validated.
        4. we ulitmately want to force the client to send data in a schema we expect.
        5. This schema will act like a contract between the front end & the back end.
    
    - We're gonna make use of a lib called `pydantic`.
    - PYdantic has got nothing to do with fastapi, you can use it wiht any of your python applications.
    - Fast API just makes use of the it so we can `define a schema`.
    - 




---


**`Stopped @ 01:16:00`**