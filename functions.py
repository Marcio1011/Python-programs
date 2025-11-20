FILEPATH = "todo.txt"
# Defines the default file path where all todo items will be stored and retrieved from.


def get_todos(filepath=FILEPATH):
    """
    Opens the specified file and returns its content as a list of lines.
    Each line in the file represents a single todo item.
    """
    with open(filepath, 'r') as file_local:
        # Opens the file in read mode ('r') and ensures it closes automatically using 'with'.
        todos_local = file_local.readlines()
        # Reads all lines from the file and stores them in a list.
    return todos_local
    # Returns the list of todo items to the caller.


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Writes the provided list of todo items to the specified file.
    Each item in the list is written as a separate line in the file.
    """
    with open(filepath, 'w') as file:
        # Opens the file in write mode ('w'), replacing existing content.
        file.writelines(todos_arg)
        # Writes the entire list of todo items to the file as-is.


if __name__ == "__main__":
    # This block runs only when this file is executed directly (not imported as a module).
    print("Hello")
    # Prints a simple greeting to indicate the script is running.
    print(get_todos())
    # Calls the get_todos function and prints the current list of stored tasks.
