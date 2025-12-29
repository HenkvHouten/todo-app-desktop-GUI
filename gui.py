import functions
# standard module: advanced library (third party)
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label],[input_box, add_button]], font="Arial, 20")

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos("files/todos.txt")
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos("files/todos.txt", todos)
        case sg.WIN_CLOSED:
            break


window.close()
