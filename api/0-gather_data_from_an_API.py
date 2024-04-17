#!/usr/bin/python3
import requests
import sys


def TODO_PROGRESS():
    """
    Retrieves TODO list progress for a given employee.
    """
    user_id = sys.argv[1]
    todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
            user_id))
    user_info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    completed_tasks = [task["title"]
                       for task in todo.json() if task["completed"]]
    print('Employee {} is done with tasks ({}/{}):'.format(
        user_info.json()['name'], len(completed_tasks), len(todo.json())))
    print('\n'.join('\t {}'.format(task) for task in completed_tasks))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        TODO_PROGRESS()
