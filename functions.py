FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """"read the text file and returns
    a list of todo items in that file
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """"write on text file with
        a list of todo items
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

