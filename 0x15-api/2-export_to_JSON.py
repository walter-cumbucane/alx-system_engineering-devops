#!/usr/bin/python3
import json
from requests import get
from sys import argv


def main():
    """
        Code Logic here
    """
    user_id = int(argv[1])
    total_tasks = 0
    completed_tasks = 0
    json_data = dict()
    data = list()
    url = 'https://jsonplaceholder.typicode.com/'
    user = get(url + f'users/{user_id}').json()
    name = user.get('username')
    todos = get(url + f'todos/').json()
    for todo in todos:
        if todo.get('userId') == user_id:
            data.append({'task': todo.get('title'),
                         'completed': todo.get('completed'),
                         'username': name})
    json_data[str(user_id)] = data
    with open(f'{user_id}.json', 'w') as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    main()
