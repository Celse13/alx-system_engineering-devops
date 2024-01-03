#!/usr/bin/python3
"""Collect information from a REST API"""
import requests
import sys


def fetch_user_activity(employee_id):
    """Retrieve user activity details"""
    root = f"https://jsonplaceholder.typicode.com"
    url = f"{root}/todos?userId={employee_id}"
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()
        fins = [todo for todo in todos if todo["completed"]]
        val = requests.get(f"{root}/users/{sys.argv[1]}").json().get("name")

        print(f"Employee {val} is done with tasks({len(fins)}/{len(todos)}):")
        for todo in fins:
            print(f"\t {todo['title']}")
    else:
        print("Error")


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    fetch_user_activity(employee_id)
