import functions
import PySimpleGUI as sg

label = sg.Text("type the todo to add")
input = sg.InputText(tooltip="enter todo" , key="todo")
add_button = sg.Button("add")
window = sg.Window('to do app',
                   layout=[[label],[input,add_button]],
                   font = ('Helvetica',20))
while True:
    event , values = window.read()
    match event:
        case "add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close()