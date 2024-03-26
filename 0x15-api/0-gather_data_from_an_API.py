#!/usr/bin/python3
"""
    Contains code that gathers data from an API
"""
from requests import get
from sys import argv


def main():
    user_id = int(argv[1])
    total_tasks = 0
    completed_tasks = 0
    titles = list()
    url = 'https://jsonplaceholder.typicode.com/'
    user = get(url + f'users/{user_id}').json()
    name = user.get('name')
    todos = get(url + f'todos/').json()
    for todo in todos:
        if todo.get('userId') == user_id:
            total_tasks += 1
            if todo.get('completed') is True:
                completed_tasks += 1
                titles.append(todo.get('title'))

    first_line = f'Employee {name} is done with tasks('
    first_line += f'{completed_tasks}/{total_tasks}):'
    print(first_line)
    for title in titles:
        print('\t', title)


if __name__ == "__main__":
    main()
