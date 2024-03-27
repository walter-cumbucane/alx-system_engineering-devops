#!/usr/bin/python3
"""
    Contains code that gathers data from an API and exports it to
    csv format
"""
import csv
from requests import get
from sys import argv


def main():
    """
        Code Logic here
    """
    user_id = int(argv[1])
    total_tasks = 0
    completed_tasks = 0
    data = list()
    url = 'https://jsonplaceholder.typicode.com/'
    user = get(url + f'users/{user_id}').json()
    name = user.get('username')
    todos = get(url + f'todos/').json()
    for todo in todos:
        if todo.get('userId') == user_id:
            data.append(
                       {'USER_ID': user_id, 'USER': name,
                        'STATUS': todo.get('completed'),
                        'TITLE': todo.get('title')})

    csv_file_name = f'{user_id}.csv'
    field_names = ['USER_ID', 'USER', 'STATUS', 'TITLE']
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(
                               file, fieldnames=field_names,
                               quoting=csv.QUOTE_ALL)
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    main()
