#!/usr/bin/python3
import requests
import sys


def TODO_PROGRESS():
    """
    Extracting the user ID from the command-line argument
    """
    user_id = sys.argv[1]
    todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId{}'.format(user_id))
    user_info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    completed_tasks = [task["title"] for task in todo if task["completed"]]
    print('Employee {} is done with tass({}/{}):'.format(
        user_info, len(completed_tasks), len(todo)))
    print('\n'.join('\t {}'.format(task) for task in tasks))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        TODO_PROGRESS()
