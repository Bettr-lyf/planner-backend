from fastapi import APIRouter
from models.task import Task

router = APIRouter()

@router.get('/tasks')
def get_tasks():
    tasks = Task.all()
    return {"tasks": [task for task in tasks]} 
    # return {'message': 'List of tasks'}

@router.post('/')
def create_task():
    task = Task.create(
        title=title,
        priority=priority,
        category=category,
        status=status,
        time_estimate_minutes=time_estimate_minutes,
        user_id=user_id  # Assuming the user is passed as a user ID
    )
    return {"message": f"Task '{task.title}' created", "task_id": task.id}

@router.get('/{task_id}')
def get_task(task_id: int):
    try:
        task = Task.get(id=task_id)  # Fetch the task by ID
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"task": task} 

@router.put('/{task_id}')
def update_task(task_id: int):
    try:
        task = Task.get(id=task_id)  # Fetch the task by ID
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if title:
        task.title = title
    if priority:
        task.priority = priority
    if category:
        task.category = category
    if status:
        task.status = status
    if time_estimate_minutes is not None:
        task.time_estimate_minutes = time_estimate_minutes

    task.save()  # Save the updated task
    return {"message": f"Task {task_id} updated", "task": task}

@router.delete('/{task_id}')
def delete_task(task_id: int):
    try:
        task = Task.get(id=task_id)  # Fetch the task by ID
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Task not found")

    task.delete()  # Delete the task
    return {"message": f"Task {task_id} deleted"}