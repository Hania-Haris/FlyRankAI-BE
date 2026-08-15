from fastapi import FastAPI, HTTPException

app = FastAPI()

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