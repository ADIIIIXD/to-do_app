def get_todo(filename):
    with open(filename, "r") as file:
        read_todos = file.readlines()
    return read_todos


while True:
    user_action = input("Type add, show, edit, completed, or exit : ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todo("to-do.txt")

        todos.append(todo)

        with open("to-do.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        todos = get_todo("to-do.txt")

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}.{item}")

    elif user_action.startswith("edit"):
        try:
            todos = get_todo("to-do.txt")
            print("Here is the existing list \n", [todo.strip("\n") for todo in todos])
            num = int(input("Enter the number of to-do task you want to edit : "))
            num = num - 1
            new_todo = input("What do you want it to replace it with : ")
            todos[num] = new_todo + "\n"
            with open("to-do.txt", "w") as file:
                todos = file.writelines(todos)
        except ValueError:
            print("Your input is not valid")
            continue

    elif user_action.startswith("completed"):
        try:
            get_todo("to-do.txt")
            print(todos)
            num = int(user_action[9:])
            todos = get_todo("to-do.txt")
            index = num - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open("to-do.txt", "w") as file:
                todos = file.writelines(todos)
            print(f"{todo_to_remove} was marked completed and has been removed from the to-do list")
        except IndexError:
            print("invalid index, please enter an index that exists")
            continue

    elif "exit" in user_action:
        break


