import json
from datetime import datetime
from .utils import fetch_json_data, get_json_path, replace_old_data, sort_by_id, status_changer, format_output
from types import FunctionType

def add(content: str,
        json_path: FunctionType = get_json_path(),
        json_data: dict = fetch_json_data()) -> int:
    createdAt: datetime = datetime.now()
    updatedAt: datetime = datetime.now()
    id: int = max([t['id'] for t in json_data['tasks']], default=0) + 1
    data = {
        "id": id,
        "content": content,
        "createdAt": str(createdAt),
        "updatedAt": str(updatedAt),
        "status": 'not-done'
    }
    json_data['tasks'].append(data)
    json_path.write_text(json.dumps(json_data, indent=2))
    return id
    
def update(task_id: int,
           content: str,
           json_data: dict = fetch_json_data) -> None:
    data = json_data()
    updatedAt: datetime = datetime.now()
    old_data = list(filter(lambda x: x['id'] == task_id, data['tasks']))
    if old_data == []:
        raise ValueError('Задачи с таким ID не существует')
    updated_data = {
        "id": old_data[0]['id'],
        "content": content,
        "createdAt": old_data[0]['createdAt'],
        "updatedAt": str(updatedAt),
        "status": old_data[0]['status']
    }
    new_data = list(filter(lambda x: x['id'] != task_id, data['tasks']))
    sort_by_id(new_data, updated_data)
    replace_old_data(new_data)
    
def delete(task_id: int,
           json_data: dict = fetch_json_data) -> None:
    data = json_data()
    replace_old_data(list(filter(lambda x: x['id'] != task_id, data['tasks'])))

def mark_in_progress(task_id: int,
                     json_data: dict = fetch_json_data):
    try:
        data = json_data()
        old_data = list(filter(lambda x: x['id'] == task_id, data['tasks']))
        if old_data == []:
            raise ValueError('Задачи с таким ID не существует')
        changed_data = status_changer(old_data, 'in-progress')
        new_data = list(filter(lambda x: x['id'] != task_id, data['tasks']))
        sort_by_id(new_data, changed_data)
        replace_old_data(new_data)
    except ValueError as err:
        print(f'Error: {str(err)}')
    
def mark_done(task_id: int,
              json_data: dict = fetch_json_data):
    try:
        data = json_data()
        old_data = list(filter(lambda x: x['id'] == task_id, data['tasks']))
        if old_data == []:
            raise ValueError('Задачи с таким ID не существует')
        changed_data = status_changer(old_data, 'done')
        new_data = list(filter(lambda x: x['id'] != task_id, data['tasks']))
        sort_by_id(new_data, changed_data)
        replace_old_data(new_data)
    except ValueError as err:
        print(f"Error: {str(err)}")

def mark_not_done(task_id: int,
                  json_data: dict = fetch_json_data):
    try:
        data = json_data()
        old_data = list(filter(lambda x: x['id'] == task_id, data['tasks']))
        if old_data == []:
            raise ValueError('Задачи с таким ID не существует')
        changed_data = status_changer(old_data, 'not-done')
        new_data = list(filter(lambda x: x['id'] != task_id, data['tasks']))
        sort_by_id(new_data, changed_data)
        replace_old_data(new_data)
    except ValueError as err:
        print(f"Error: {str(err)}")

def output_list(status: str, json_data: dict = fetch_json_data):
    data = json_data()
    return format_output(list(filter(lambda x: x['status'] == status, data['tasks']))) if status != 'all' else format_output(data['tasks'])