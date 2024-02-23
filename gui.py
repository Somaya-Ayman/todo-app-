import functions
import PySimpleGUI as sg
import time

sg.theme("Black")
time_label = sg.Text('',key="clock")
label = sg.Text("type the todo to add")
input = sg.InputText(tooltip="enter todo" , key="todo")
add_button = sg.Button("add")
list_box = sg.Listbox(values = functions.get_todos(), key="todos",
                      enable_events = True, size = [45,10])
edit_button = sg.Button("edit")
complete_button = sg.Button("complete")
exit_button = sg.Button("exit")

window = sg.Window('to do app',
                   layout=[[time_label],
                           [label],
                           [input,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font = ('Helvetica',20))
while True:
    event , values = window.read(timeout=200) #loop usually runs when an event happents but now it runs each 200 millisec
    window["clock"].update(value=time.strftime("%b %d-%m-%Y, %H:%M:%S"))
    #print(event)
    #print(values)
    match event:
        case "add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("select a todo first", font = ('Helvetica',20))
        case "complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("select a todo first", font = ('Helvetica',20))

        case "exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()