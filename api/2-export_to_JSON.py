#!/usr/bin/python3
"""
Python script to export data in the JSON fromat
"""
import json
import requests
from sys import argv


def export_to_json():
    """
    Fethces and processes user and TODO list data for the provided ID.
    """
    Id = argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{Id}"
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={Id}"

    user = json.loads(requests.get(user_url).text)
    tasks = json.loads(requests.get(tasks_url).text)
    print("tasks", tasks)
    user_name = user["username"]

    " Creating necessary lists and dictionaries "
    tasks_list = []
    json_dict = {}

    for task in tasks:
        tasks_dict = {}
        tasks_dict['task'] = task['title']
        tasks_dict['completed'] = task['completed']
        tasks_dict['username'] = user_name
        tasks_list.append(tasks_dict)

    json_dict[Id] = tasks_list

    with open(Id + '.json', "w") as js_file:
        json.dump(json_dict, js_file)


if __name__ == "__main__":
    if len(argv) == 2:
        export_to_json()
