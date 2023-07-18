import functions
import PySimpleGUI as pg

label = pg.Text("Enter a to-do task:")
input1 = pg.InputText(tooltip="Enter To-Do Task", key="todo")
add_button = pg.Button("ADD")
edit_button = pg.Button("EDIT")
list_box = pg.Listbox(functions.get_todo(), key="todos",
                      enable_events=True, size=[25, 25])

window = pg.Window("My TO-DO List", layout=[[label], [input1, add_button],
                                            [list_box, edit_button]], font=("Helvetica", 12))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "ADD":
            todos = functions.get_todo()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todo(todos)
            window["todos"].update(values=todos)
        case "EDIT":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]
            todos = functions.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todo(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case pg.WIN_CLOSED:
            break
window.close()


