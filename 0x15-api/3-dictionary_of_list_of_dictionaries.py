#!/usr/bin/python3
"""Make dictionary"""
import json
import requests


def make_export_to_json_dictioinary():
    """export to json text-base format"""
    root = f"https://jsonplaceholder.typicode.com/users"
    response = requests.get(root)

    if response.status_code == 200:
        employees = response.json()
        result = {}
        for employee in employees:
            employee_id = str(employee.get("id"))
            employee_name = employee.get("username")
            url = f"{root}/{employee_id}/todos"
            todo_response = requests.get(url)

            if todo_response.status_code == 200:
                todos = todo_response.json()
                content = [{"username": employee_name, "task":
                            todo.get("title"), "completed":
                            todo.get("completed")} for todo in todos]
                result[employee_id] = content
            else:
                print("Task Error")

        json_file = "todo_all_employees.json"
        with open(json_file, 'w') as file:
            json.dump(result, file)

    else:
        print("User Error")


if __name__ == "__main__":
    make_export_to_json_dictioinary()
