#!/usr/bin/python3
"""
Python script that, exports data in the CSV format
"""

import json
import requests
from sys import argv


def export_to_csv():
    """
    Fethces and processes user and TODO list data for the provided ID.
    """
    Id = argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{Id}'
    tasks_url = f'https://jsonplaceholder.typicode.com/todos?userId={Id}'

    user = json.loads(requests.get(user_url).text)
    tasks = json.loads(requests.get(tasks_url).text)

    employee_name = user['username']

    string = ''
    for task in tasks:
        title = task['title']
        status = task['completed']
        string += f'"{argv[1]}","{employee_name}","{status}","{title}"\n'

    filename = argv[1] + '.csv'

    "Open and write csv file"
    with open(filename, 'w') as csvfile:
        csvfile.write(string)


if __name__ == "__main__":
    if len(argv) == 2:
        export_to_csv()
