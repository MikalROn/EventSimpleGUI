# Events For SimpleGui

> Status of project: in progress...

This project has the intention to make easier, scalable and readable events on PySimpleGUI
## Download
````shell
$pip install EventSimpleGUI
````
## Demonstration

<h3> Creating an event function </h3>

Using the decorator event to run an event, you can pass the element key as an argument for decorator, when the event is called, function is going to be called two

````python
from pysimpleevent import EventSimpleGUI
import PySimpleGUI as sg

app = EventSimpleGUI()


@app.event('_click')
def when_btn_was_clicked(event: str, values: dict, window: sg.Window):
    print('Just a normal event')

layout = [[sg.B('Just a button', key='_click')]]
window = sg.Window('Just a Window.', layout)

if __name__ == '__main__':
    app.run_window(window)
````
Events can be passed as an argument of run window like in the exemple

````python
from pysimpleevent import EventSimpleGUI
import PySimpleGUI as sg

app = EventSimpleGUI()



def when_btn_was_clicked(event: str, values: dict, window: sg.Window):
    if event == '_click':
        print('Just a normal event')

layout = [[sg.B('Just a button', key='_click')]]
window = sg.Window('Just a Window.', layout)

if __name__ == '__main__':
    app.run_window(window, when_btn_was_clicked)
````
And can also pass an event using add_event
````python
from pysimpleevent import EventSimpleGUI
import PySimpleGUI as sg

app = EventSimpleGUI()



def when_btn_was_clicked(event: str, values: dict, window: sg.Window):
    if event == '_click':
        print('Just a normal event')

app.add_event(when_btn_was_clicked)
layout = [[sg.B('Just a button', key='_click')]]
window = sg.Window('Just a Window.', layout)

if __name__ == '__main__':
    app.run_window(window)
````
