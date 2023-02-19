from pysimpleevent import EventSimpleGUI
import PySimpleGUI as sg

loop = EventSimpleGUI()
win = sg.Window('Win', [[sg.B('click')]])

@loop.event('click')
def simple_event(*args):
    print('click')

if __name__ == '__main__':
    loop.run_window(win)