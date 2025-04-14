from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def get_tasks():
    return {'message': 'List of tasks'}

@router.post('/')
def create_task():
    return {'message': 'Task created'}

@router.get('/{task_id}')
def get_task(task_id: int):
    return {'message': f'Task {task_id}'}

@router.put('/{task_id}')
def update_task(task_id: int):
    return {'message': f'Task {task_id} updated'}

@router.delete('/{task_id}')
def delete_task(task_id: int):
    return {'message': f'Task {task_id} deleted'}