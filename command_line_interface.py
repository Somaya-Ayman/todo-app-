import functions
import time
now = time.strftime("%b %d-%m-%Y, %H:%M:%S")
print("it is now: " + now)
while True :
    task = input("Choose between add, show, edit, complete or exit: ")
    task = task.strip()

    if task.startswith('add'):
        todo = task[4:]+ "\n"
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif task.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
        print(f"Numer of todo items still not complete is: {index + 1}")

    elif task.startswith('edit'):
        try:
            number = int(task[5:])
            todos = functions.get_todos()
            todos[number - 1] = input("Enter edited todo: ") + '\n'
            functions.write_todos(todos)

        except ValueError:
            print("Enter the number of todo item you want to edit: ")
            continue

    elif task.startswith('complete'):
        try:
            number = int(task[9:])
            todos = functions.get_todos("todos.txt")
            completed_todo = todos.pop(number - 1).strip('\n')
            functions.write_todos(todos)
            print(f"Good job you completed: {completed_todo}")
        except IndexError:
            print("There is no item with that number")
            continue
        except ValueError:
            print("Enter the number of todo item you want to complete: ")
            continue

    elif task.startswith('exit'):
        break

    else:
        print("Command not valid!")



print("Bye")