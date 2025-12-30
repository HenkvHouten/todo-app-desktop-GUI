import functions
# standard module: advanced library (third party)
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos("files/todos.txt"), key="todos", enable_events=True, size=(44, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font="Arial, 20")

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos("files/todos.txt")
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos("files/todos.txt", todos)
            # real time toevoegen
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos("files/todos.txt")
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos("files/todos.txt", todos)
            window["todos"].update(todos)
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos("files/todos.txt")
            todos.remove(todo_to_complete)
            functions.write_todos("files/todos.txt", todos)
            window["todos"].update(values=todos)
            window["todo"].update(value='')
        case "Exit":
            break
        case "todos":
            # in invoerveld laten zien welke je aanklikt om te editen
            window["todo"].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()
