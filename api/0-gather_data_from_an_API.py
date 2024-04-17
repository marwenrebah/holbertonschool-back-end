import requests
import sys


def TODO_PROGRESS():
    """
    Retrieves To Do list progress for a given employee.
    """
    user_id = sys.argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos/?userId={user_id}'
    user_response = requests.get(user_url).json()
    name = user_response.get('name')
    todos_response = requests.get(todos_url).json()
    tasks = [task.get('title')
             for task in todos_response if task.get('completed') is True]
    print('Employee {} is done with tasks ({}/{}):'.format(name,
          len(tasks), len(todos_response)))
    print('\n'.join('\t {}'.format(task) for task in tasks))


if __name__ == "__main__":
    TODO_PROGRESS()
