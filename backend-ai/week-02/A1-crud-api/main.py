from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class TaskCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False

class TaskUpdate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False

tasks = [
    {
        "id": 1,
        "title": "Finish Week 2 API",
        "description": "Build the first CRUD API",
        "completed": False
    },
    {
        "id": 2,
        "title": "Test the API",
        "description": "Test all endpoints with Swagger",
        "completed": False
    }
]

@app.get("/")
def root():
    return {"message": "Hello from my Task API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    new_id = max([task["id"] for task in tasks], default=0) + 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }

    tasks.append(new_task)

    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    for existing_task in tasks:
        if existing_task["id"] == task_id:
            existing_task["title"] = task.title
            existing_task["description"] = task.description
            existing_task["completed"] = task.completed
            return existing_task

    raise HTTPException(status_code=404, detail="Task not found")