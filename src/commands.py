import json
from datetime import datetime
from utils import fetch_json_data, get_json_path, replace_old_data, sort_by_id, status_changer
from types import FunctionType

def add(content: str,
        json_path: FunctionType = get_json_path(),
        json_data: dict = fetch_json_data()) -> int:
    createdAt: datetime = datetime.now()
    updatedAt: datetime = datetime.now()
    print(len(json_data['tasks']))
    if (len(json_data['tasks'])) > 0:
        id: int = json_data['tasks'][-1]['id']
    else:
        id: int = 0 
    data = {
        "id": id + 1,
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
           json_data: dict = fetch_json_data()) -> None:
    updatedAt: datetime = datetime.now()
    old_data = list(filter(lambda x: x['id'] == task_id, json_data['tasks']))
    if old_data == []:
        raise ValueError('Задачи с таким ID не существует')
    data = {
        "id": old_data[0]['id'],
        "content": content,
        "createdAt": old_data[0]['createdAt'],
        "updatedAt": str(updatedAt),
        "status": old_data[0]['status']
    }
    new_data = list(filter(lambda x: x['id'] != task_id, json_data['tasks']))
    sort_by_id(new_data, data)
    replace_old_data(new_data, json_data)
    
def delete(task_id: int,
           json_data: dict = fetch_json_data()) -> None:
    replace_old_data(list(filter(lambda x: x['id'] != task_id, json_data['tasks'])), json_data)

def mark_in_progress(task_id: int,
                     json_data: dict = fetch_json_data()):
    old_data = list(filter(lambda x: x['id'] == task_id, json_data['tasks']))
    if old_data == []:
        raise ValueError('Задачи с таким ID не существует')
    data = status_changer(old_data, 'in-progress')
    new_data = list(filter(lambda x: x['id'] != task_id, json_data['tasks']))
    sort_by_id(new_data, data)
    replace_old_data(new_data, json_data)
    
def mark_done(task_id: int,
              json_data: dict = fetch_json_data()):
    old_data = list(filter(lambda x: x['id'] == task_id, json_data['tasks']))
    if old_data == []:
        raise ValueError('Задачи с таким ID не существует')
    data = status_changer(old_data, 'done')
    new_data = list(filter(lambda x: x['id'] != task_id, json_data['tasks']))
    sort_by_id(new_data, data)
    replace_old_data(new_data, json_data)

def mark_not_done(task_id: int,
                  json_data: dict = fetch_json_data()):
    old_data = list(filter(lambda x: x['id'] == task_id, json_data['tasks']))
    if old_data == []:
        raise ValueError('Задачи с таким ID не существует')
    data = status_changer(old_data, 'no-done')
    new_data = list(filter(lambda x: x['id'] != task_id, json_data['tasks']))
    sort_by_id(new_data, data)
    replace_old_data(new_data, json_data)

def output_list(status: str, json_data: dict = fetch_json_data()):
    return list(filter(lambda x: x['status'] == status, json_data['tasks']))


if __name__ == '__main__':
    # add(
    #     'asdfasdfasdj;fal'
    # )
    # update(
    #     7,
    #     'Check append'
    # )
    # delete(
    #     7
    # )
    # mark_in_progress(
    #     1
    # )
    output_list(
        'in-progress'
    )
