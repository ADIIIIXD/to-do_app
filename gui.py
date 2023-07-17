import PySimpleGUI as pg

label = pg.Text("Enter a to-do task:")
input1 = pg.Input()

# BUTTONS
add_button = pg.Button("ADD")
show_button = pg.Button("SHOW")
edit_button = pg.Button("EDIT")
complete_button = pg.Button("COMPLETED")

# Window
window = pg.Window("My TO-DO List",
                   layout=[[label, input1],
                           [add_button, show_button],
                           [edit_button, complete_button]])
window.read()
window.close()
