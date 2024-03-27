#!/usr/bin/python3
"""
    Gathers data from an API and exports to a JSON file
"""
import json
from requests import get


def main():
    """
        Code Logic here
    """
    json_data = dict()
    data = list()
    url = 'https://jsonplaceholder.typicode.com/'
    todos = get(url + 'todos/').json()

    for todo in todos:
        user_id = todo.get('userId')
        user = get(url + f'{user_id}').json()
        name = user.get('username')
        data.append({'task': todo.get('title'),
                     'completed': todo.get('completed'),
                     'username': name})
        json_data[f'{user_id}'] = data
        data.clear()

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    main()
