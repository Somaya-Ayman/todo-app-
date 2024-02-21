import functions
import PySimpleGUI as sg

label = sg.Text("type the todo to add")
input = sg.InputText(tooltip="enter todo")
add_button = sg.Button("add")
window = sg.Window('to do app',layout=[[label],[input,add_button]])
window.read()
window.close()