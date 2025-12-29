# Add desktop GUI
import time
from functions import write_todos, get_todos

now = time.strftime("%b %d, %Y %H:%M:%S")
print("The time is below:")
print("It is " + now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos("files/todos.txt")

        todos.append(todo + '\n')

        write_todos("files/todos.txt", todos)

    elif 'show' in user_action:
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    elif 'edit' in user_action:
        try:
           number = int(user_action[5:])
           number = number - 1

           todos = get_todos("files/todos.txt")

           new_todo = input("Enter new todo: ")
           todos[number] = new_todo + '\n'

           write_todos("files/todos.txt", todos)

        except ValueError:
            print("Please enter a valid input")
            continue

    elif 'complete' in user_action:
        try:
           number = int(user_action[8:])

           todos = get_todos("files/todos.txt")

           index = number -1
           todo_to_remove = todos[index].strip('\n')
           todos.pop(index)

           write_todos("files/todos.txt", todos)

           message = f"Todo {todo_to_remove} was successfully removed!"
           print(message)

        except IndexError:
            print("Please enter a valid input")
            continue

    elif 'exit' in user_action:
       break

    else:
        print("Please enter a valid input")

print("Bye!")