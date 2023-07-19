import functions
import PySimpleGUI as pg

pg.theme("LightBrown9")

label = pg.Text("Enter a to-do task:")
input1 = pg.InputText(tooltip="Enter To-Do Task", key="todo")
add_button = pg.Button("ADD")
edit_button = pg.Button("EDIT")
completed_button = pg.Button("COMPLETED")
list_box = pg.Listbox(functions.get_todo(), key="todos",
                      enable_events=True, size=[30, 10])

window = pg.Window("My TO-DO List", layout=[[label],
                                            [input1, add_button],
                                            [list_box, edit_button, completed_button]],
                                     font=("Helvetica", 12))
while True:
    event, values = window.read()
    match event:
        case "ADD":
            todos = functions.get_todo()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todo(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "EDIT":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = functions.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todo(todos)
                window["todos"].update(values=todos)
            except IndexError:
                pg.popup("Please select a to-do item first", title="ERROR", font=("OpenSans", 12))
        case "COMPLETED":
            try:
                completed_todo = values["todos"][0]
                todos = functions.get_todo()
                todos.remove(completed_todo)
                functions.write_todo(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                pg.popup("Please select a to-do item first", title="ERROR", font=("OpenSans", 12))
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case pg.WIN_CLOSED:
            break
window.close()
