# Call reference

## <b> <em>class:</em> EventSimpleGUI(  )</b>

    Use this class to start a window and create events

#### Exemple:

````python
loop = EventSimpleGUI()
````

### <b> <em>method:</em> add_event( event ) </b>
    You can use this method, but it is recomended to use decor @EventSimpleGUI.event

<b>:param event:</b>                                     Must be an event function

<h6><b>Exemple: </b></h6>

````python
def func(*args):
    print(args)
loop.add_event(func)
````

### <b> <em>property:</em> get_events(  )</b>
    Use this property to get all events, from @event or add_event

<b>:return:</b>                                     List of event functions

<h6><b>Exemple: </b></h6>

````python
loop.get_events
````

### <b> <em>method:</em> run_window( window, *args, **keyargs)  </b>
    Use this property to get all events, from @event or add_event
<table>
<tr> <th> params </th> <th> resume </th>

</tr>
      <tr>
        <td><b>Window</b></td>
        <td>can be any PySimpleGUI Window</td> 
        </tr><tr>
        <td><b>args</b></td>
        <td>can be any function that recives (event: str , values: dict, window: PySimpleGUI.Window)</td>
        </tr><tr>        
        <td><b>window_log</b></td>
        <td>if True prints events and values on the console</td>
        </tr><tr>
        <td><b>return_values</b>
        <td>if True return values of window.read()</td>
        </tr><tr>
        <td><b>task</b></td>
        <td>can be any callable  function</td>
        </tr><tr>
        <td><b>close event</b></td>
        <td>a diferent key to close the window</td>
        </tr><tr>
        <td><b>return</b></td>
        <td>dict of values or None</td>
        </tr>
</table>

<h6><b>Exemple: </b></h6>
````python
win = sg.Window('win', [[sg.T('hello world')]])
loop.run_window(win)
````
### <b> <em>decorator:</em> event( key )  </b>
    Use this decorator to create an event function 
<table>
      <tr>
        <td><b>param key</b></td>
        <td> event string or a list of them </td>
      </tr>
</table>

<h6><b>Exemple: </b></h6>
````python
win = sg.Window('win', [[sg.T('hello world')]])
loop.run_window(win)
````