#!/usr/bin/python3
"""Make export to JSON"""
import json
import requests
import sys


def make_exp_to_json(id):
    """Make export to json"""
    root = f"https://jsonplaceholder.typicode.com"
    url = f"{root}/todos?userId={id}"
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()
        val = requests.get(f"{root}/users/{id}").json().get("username")
        json_file = f"{id}.json"
        employee_info = {str(id): [{"task": todo.get("title"), "completed":
                         todo.get("completed"), "username":
                         val} for todo in todos]}

        with open(json_file, mode='w') as file:
            json.dump(employee_info, file)
    else:
        print("Error")


if __name__ == "__main__":
    try:
        get_employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    make_exp_to_json(get_employee_id)
