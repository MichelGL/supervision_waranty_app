from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Construction Supervision and Warranty Service App"
)

users = [
    {"id": 1, "role": "admin", "name": "Michel"},
    {"id": 2, "role": "employee", "name": "Victor"},
    {"id": 3, "role": "contractor", "name": "Ivan"},
]

class Task(BaseModel):
    id: int


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in users if user.get("id") == user_id]

@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, users))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}
