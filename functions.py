FILEPATH = "todo.txt"

def get_todos(filepath=FILEPATH):
    """Read the todo file and return the list of tasks."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the list of tasks to the todo file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())