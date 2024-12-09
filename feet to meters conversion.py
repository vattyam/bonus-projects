import FreeSimpleGUI as sg

def convert(feet, inches):
    feet_local = float(feet)
    inches_local = float(inches)
    meters_local = feet_local * 0.3048 + inches_local * 0.0254
    return meters_local


label1 = sg.Text("Enter feet")
input1 = sg.Input()
label2 = sg.Text("Enter inches")
input2 = sg.Input()
convert_button = sg.Button("Convert")
output_label = sg.Text(key="output", text_color="white")
window = sg.Window('Convertor', layout=[[label1,input1], [label2,input2], [convert_button, output_label]])

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Convert":
            meters = convert(values[0], values[1])
            window["output"].update(value=f"{meters} m")
        case sg.WIN_CLOSED:
            break


window.close()

