from demo1 import when_btn_was_clicked, window, app
from pysimpleevent import EventSimpleGUI


test_app = EventSimpleGUI() # Without any event

class Test:

    def test_event_when_btn_was_clicked(self):
        # Context
        event = '_click'
        values = {}
        # When action
        result = when_btn_was_clicked(event, values, window) # put on the return what shows that function doesen't failed
        assert result


