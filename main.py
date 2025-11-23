# Import FastAPI class from fastapi package
from fastapi import FastAPI

# Create an instance of FastAPI
# This object "app" is our web application
app = FastAPI()

# GET endpoint at root "/"
@app.get("/")  # This means: "if someone visits '/' with GET request, run this function"
async def root():
    """
    Returns a simple welcome message
    Example URL: GET http://127.0.0.1:8000/
    """
    return {"message": "hello world"}


#  POST endpoint at root "/"
# This is a POST request (usually used to send data to the server)
# deprecated=True marks this endpoint as old, you shouldn’t use it in new code
@app.post("/", deprecated=True)
async def post_root():
    return {"message": "this is a post request"}


#  PUT endpoint at root "/"
# This is a PUT request (usually used to update data)
# description will appear in the automatically generated API docs
@app.put("/", description="This endpoint handles PUT requests to update data")
async def put_root():
    return {"message": "this is a put request"}


#  GET endpoint to list all users
@app.get("/users")  # Visiting '/users' with GET will trigger this function
async def list_users():
    return {"message": "this is user list"}

#fast api sees the func by order
#so if there's static parameter it should be the first before the dynamic one
@app.get("/users/1")
async def admin_user():
    return{"message":"this is the main admin portal"}

# GET endpoint to get a single user by ID
# {user_id} is a path parameter
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """
    Returns a specific user based on user_id

    Important:
    - We put `user_id: int` to tell FastAPI: "user_id must be an integer"
    - If someone sends a non-integer, FastAPI will automatically return an error
      (example: /users/abc → 422 Unprocessable Entity)
    - If we didn't put int, FastAPI would treat it as a string.
      That works, but if your logic expects a number, you may get errors later.
    """
    return {"user id": user_id}



