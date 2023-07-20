import functions

while True:
    user_action = input("Type add, show, edit, completed, or exit : ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todo()

        todos.append(todo)

        functions.write_todo(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todo()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}.{item}")

    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todo()
            print("Here is the existing list \n", [todo.strip("\n") for todo in todos])
            num = int(input("Enter the number of to-do task you want to edit : "))
            num = num - 1
            new_todo = input("What do you want it to replace it with : ")
            todos[num] = new_todo + "\n"
            functions.write_todo(todos)
        except ValueError:
            print("Your input is not valid")
            continue

    elif user_action.startswith("completed"):
        try:
            todos = functions.get_todo()
            num = int(user_action[9:])
            index = num - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todo(todos)
            print(f"{todo_to_remove} was marked completed and has been removed from the to-do list")
        except IndexError:
            print("invalid index, please enter an index that exists")
            continue

    elif "exit" in user_action:
        break


