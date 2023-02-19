from pysimpleevent import EventSimpleGUI
import PySimpleGUI as sg

loop = EventSimpleGUI()


@loop.event( '_click' )
def when_btn_was_clicked(event: str, values: dict, window: sg.Window):
    print('Just a normal event')
    return True

layout = [
    [sg.B('Just a button', k='_click')]
]

sg.theme(sg.theme_list()[1])
window = sg.Window('Just a Window.', layout, resizable=True, scaling=5)

if __name__ == '__main__':
    loop.run_window( window )
