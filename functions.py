FILEPATH = "to-do.txt"


def get_todo(filename=FILEPATH):
    with open(filename, "r") as file:
        read_todos = file.readlines()
    return read_todos


def write_todo(todo_args, filename=FILEPATH):
    with open(filename, "w") as file:
        todos = file.writelines(todo_args)
        return todos
