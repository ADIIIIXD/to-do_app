import functions
import PySimpleGUI as pg

label = pg.Text("Enter a to-do task:")
input1 = pg.InputText(tooltip="Enter To-Do Task", key="todo")
add_button = pg.Button("ADD")
window = pg.Window("My TO-DO List", layout=[[label], [input1, add_button]], font=("Helvetica", 12))

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
        case pg.WIN_CLOSED:
            break

window.close()


