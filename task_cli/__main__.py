#Roadmap.sh: Task Tracker -- https://roadmap.sh/projects/task-tracker

# What is need to do:
# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress

# Contrains:
# You can use any programming language to build this project.
# Use positional arguments in command line to accept user inputs.
# Use a JSON file to store the tasks in the current directory.
# The JSON file should be created if it does not exist.
# Use the native file system module of your programming language to interact with the JSON file.
# Do not use any external libraries or frameworks to build this project.
# Ensure to handle errors and edge cases gracefully.

import argparse
from .commands import add, update, delete, mark_in_progress, mark_done, mark_not_done, output_list
from .utils import create_json_file, get_json_path

def main():
    
    if not get_json_path().exists():
        create_json_file()
    
    parser = argparse.ArgumentParser(description="Программа таск-менеджер")
    subparsers = parser.add_subparsers(dest='command', help='Доступные команды')

    parser_add = subparsers.add_parser('add', help='Добавить таск в менеджер')
    parser_add.add_argument('task_content', type=str, help='Содержание таска')
    
    parser_update = subparsers.add_parser('update', help="Обновить такс в менеджере")
    parser_update.add_argument('id', type=int)
    parser_update.add_argument('content', type=str)
    
    parser_delete = subparsers.add_parser('delete', help='Удаляет таск')
    parser_delete.add_argument('id', type=int)
    
    parser_mark_in_progress = subparsers.add_parser('mark-in-progress')
    parser_mark_in_progress.add_argument('id', type=int)
    
    parser_mark_done = subparsers.add_parser('mark-done')
    parser_mark_done.add_argument('id', type=int)
    
    parser_mark_not_done = subparsers.add_parser('mark-not-done')
    parser_mark_not_done.add_argument('id', type=int)
    
    parser_output_list = subparsers.add_parser('list')
    parser_output_list.add_argument(
    'status', 
    choices=['done', 'not-done', 'in-progress', 'all'],
    help="Status: done|not-done|in-progress|all"
    )

    args = parser.parse_args()

    try:
        if args.command == 'add':
            id = add(args.task_content)
            print(f'Task added successfully (ID: {id}): {args.task_content}')
        elif args.command == 'update':
            update(args.id, args.content)
        elif args.command == 'delete':
            delete(args.id)
        elif args.command == 'mark-in-progress':
            mark_in_progress(args.id)
        elif args.command == 'mark-done':
            mark_done(args.id)
        elif args.command == 'mark-not-done':
            mark_not_done(args.id)
        elif args.command == 'list':
            print(output_list(args.status))
        else:
            parser.print_help()
    except FileNotFoundError as err:
        create_json_file()
        print(err)
        
if __name__ == "__main__":
    main()