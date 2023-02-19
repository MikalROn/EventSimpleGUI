from pysimpleevent import EventSimpleGUI
import PySimpleGUI as sg

loop = EventSimpleGUI()



def when_btn_was_clicked(event: str, values: dict, window: sg.Window):
    if event == '_click':
        print('Just a normal event')

layout = [[sg.B('Just a button', key='_click')]]
window = sg.Window('Just a Window.', layout)

if __name__ == '__main__':
    loop.run_window( window, when_btn_was_clicked )