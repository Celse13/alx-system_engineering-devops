#!/usr/bin/python3
"""Export to CSV"""
import csv
import requests
import sys


def make_exp_to_csv(id):
    """Make exportation to CSV file."""
    root = f"https://jsonplaceholder.typicode.com"
    url = f"{root}/todos?userId={id}"
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()
        val = requests.get(f"{root}/users/{id}").json().get("username")
        csv_file = f"{id}.csv"

        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for todo in todos:
                writer.writerow([id, val,
                                 todo.get("completed"), todo.get("title")])
    else:
        print("Error")


if __name__ == "__main__":
    try:
        id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    make_exp_to_csv(id)
