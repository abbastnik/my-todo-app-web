FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):  # todos.txt is the default argument which can be overwritten in code
    """""Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()  # creates the list and each line is an item of todos list
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):  # it doesn't need to return anything
    """Write the to-do items list in the text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":  # it only prints Hello when I run this script separately
    print("Hello")
