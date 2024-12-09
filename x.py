import FreeSimpleGUI as sg
text = sg.Text("Welcome")
button = sg.Button("Delete", key="delete")
window = sg.Window('My App', layout=[[text], [button]])

window.read()
print(window['delete'])