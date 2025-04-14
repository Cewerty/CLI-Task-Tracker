from pathlib import Path
import json
from types import FunctionType
from config import config
from pprint import pprint

def get_json_path(path: str = None) -> Path:
    if path is None:
        return Path(config['path'])
    else:
        return Path(path)

def fetch_json_data(path: Path = get_json_path()) -> dict:
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
        return data
    except FileNotFoundError:
        print(f'Файл по пути: {path} не существует!')
        data = {'Error': 'File not found'}
        return data
    except json.JSONDecodeError:
        print('Файл не получается декодировать в json!')
        data = {'Error': "File can't be decoded"}
        return data
    
def create_json_file(path = get_json_path()) -> bool:
    try:
        # Устанавливаем путь по умолчанию
        # Проверяем существование файла
        if path.exists():
            raise FileExistsError(f"Файл '{path}' уже существует")
            
        # Создаем родительские директории, если их нет
        path.parent.mkdir(parents=True, exist_ok=True)
        
        # Создаем файл с базовой структурой
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
    

def replace_old_data(new_data: list, updated_data: dict, json_path: FunctionType = get_json_path()) -> None:
    updated_data['tasks'].clear()
    for i in range(len(new_data)):
            updated_data['tasks'].append(new_data[i])
    json_path.write_text(json.dumps(updated_data, indent=2))

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
        

if __name__ == '__main__':
    pprint(fetch_json_data())
    pprint(create_json_file())