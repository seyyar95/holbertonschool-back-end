#!/usr/bin/python3
""""""
import requests
import json
from sys import argv


def gather_user_information():
    """
    Fethces and processes user and TODO list data for the provided ID.
    """
    Id = argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{Id}"
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={Id}"

    user = json.loads(requests.get(user_url).text)
    tasks = json.loads(requests.get(tasks_url).text)

    employee_name = user["name"]
    for task 


if __name__ == "__main__":
    if len(argv) == 2:
        gather_user_information()
