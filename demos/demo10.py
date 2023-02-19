from pysimpleevent import EventSimpleGUI
import PySimpleGUI as sg


loop = EventSimpleGUI()

keys = ['_click', '_click1']

@loop.event(keys)
def when_btn_was_clicked(*args):
    print('Just a normal event')


layout = [
    [sg.B(f'{"Just a button":54}', key='_click')],
    [sg.B(f'{"Just another button":50}', key='_click1')]
]
window = sg.Window('Just a Window.', layout, scaling=1.5)
if __name__ == '__main__':
    loop.run_window(window, window_log=True)
