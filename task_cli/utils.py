from pathlib import Path
import json
from types import FunctionType
from typing import Callable
from .config import config

def get_json_path(path: str = None) -> Path:
    if path is None:
        return Path(config['path'])
    else:
        return Path(path)

def fetch_json_data(json_path_factory: Callable[[], Path] = get_json_path) -> dict:
    path = json_path_factory()
    try:
        if not path.exists():
            return {"tasks": []}
            
        data = json.loads(path.read_text(encoding='utf-8'))
        return {"tasks": data.get("tasks", [])}
        
    except (json.JSONDecodeError, FileNotFoundError):
        return {"tasks": []}
    
def create_json_file(path = get_json_path) -> bool:
    try:
        path = path()
        if path.exists():
            raise FileExistsError(f"Файл '{path}' уже существует")
            
        path.parent.mkdir(parents=True, exist_ok=True)
        
        template_data = {"tasks": []}
        path.write_text(
            json.dumps(template_data, indent=2, ensure_ascii=False), 
            encoding="utf-8"
        )
        return True
        
    except FileExistsError as e:
        print(f"Ошибка: {e}")
        return False
        
    except PermissionError:
        print(f"Нет прав на запись в '{path}'")
        return False
        
    except Exception as e:
        print(f"Неизвестная ошибка: {str(e)}")
        return False
    

def replace_old_data(new_data: list, json_path: FunctionType = get_json_path) -> None:
    path = json_path()
    data = {"tasks": new_data}
    path.write_text(json.dumps(data, indent=2))

def sort_by_id(data: list, appended_data: list) -> list:
    data.append(appended_data)
    data.sort(key=lambda x: x['id'])
    return data

def status_changer(data: list, new_status: str) -> dict:
    data_with_updated_status = {
        "id": data[0]['id'],
        "content": data[0]['content'],
        "createdAt": data[0]['createdAt'],
        "updatedAt": data[0]['updatedAt'],
        "status": new_status
    }
    return data_with_updated_status

def format_output(tasks):
    return "\n".join(
        f"ID: {t['id']} | {t['status']} | {t['content']}"
        for t in tasks
)