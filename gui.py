import functions
# standard module: advanced library (third party)
import FreeSimpleGUI as sg
import time

# Add theme
sg.theme("LightGrey3")

# Date and time
clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo", size=(34, 1))
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos("files/todos.txt"), key="todos", enable_events=True, size=(33, 5))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font="Arial, 20")

while True:
    event, values = window.read(timeout=10)
    # Add date and time (update the empty string above
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos("files/todos.txt")
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos("files/todos.txt", todos)
            # real time toevoegen
            window["todos"].update(values=todos)
        case "Edit":
            # Error handling (clicking edit but not selecting one of the todos)
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos("files/todos.txt")
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos("files/todos.txt", todos)
                window["todos"].update(todos)
            except IndexError:
                sg.popup("Please select an item to edit", font=("Arial", 14))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos("files/todos.txt")
                todos.remove(todo_to_complete)
                functions.write_todos("files/todos.txt", todos)
                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except IndexError:
                sg.popup("Please select an item to edit", font=("Arial", 14))

        case "Exit":
            break
        case "todos":
            # in invoerveld laten zien welke je aanklikt om te editen
            window["todo"].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()
