#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import json
from sys import argv


def user_information():
    if len(argv) == 2:
        Id = argv[1]
        user_url = f'https://jsonplaceholder.typicode.com/users/{Id}'
        tasks_url = f'https://jsonplaceholder.typicode.com/todos?userId={Id}'
        user = json.loads(requests.get(user_url).text)
        tasks = json.loads(requests.get(tasks_url).text)
        completed = 0
        completed_tasks = []
        employee_name = user['name']
        for task in tasks:
            if task['completed'] is True:
                completed += 1
                completed_tasks.append(task['title'])
        print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                              completed,
                                                              len(tasks)))
        for title in completed_tasks:
            print(f"\t {title}")


if __name__ == "__main__":
    user_information()
