import sys
from tests.windom_sim import WinSimulator
from pysimpleevent.fastevent import EventSimpleGUI
from io import StringIO


class Test:
    """ Testing all features from main code """
    def test_if_event_go_to_list_of_events_using_decor(self):
        loop = EventSimpleGUI()

        @loop.event('test')
        def event_test(*args):
            pass
        assert event_test in loop.get_events

    def test_if_simulatedwin_return_event_values_and_close(self):
        loop = EventSimpleGUI()
        win = WinSimulator(event='test', values={})

        @loop.event('test')
        def test_event(*args):
            return True
        result = loop.run_window(win, return_values=True, close_event='test')
        assert result['test_event']

    def test_if_event_go_to_list_of_events_using_add_event(self):
        loop = EventSimpleGUI()

        def event_test(*args):
            ...
        loop.add_event(event_test)
        assert event_test in loop.get_events

    def test_run_events_as_run_win_args(self):
        loop = EventSimpleGUI()
        win = WinSimulator(event='test', values={})

        def event_test(*args):
            event, values, _ = args
            if event == 'test':
                values[event_test.__name__] = True
        result = loop.run_window(win, event_test, close_event='test')
        assert result['event_test']

    def test_if_loop_run_taks(self):
        loop = EventSimpleGUI()
        win = WinSimulator(event='test', values={})

        string_io = StringIO()
        sys.stdout = string_io

        def test_task(*args):
            print('test')

        loop.run_window(win, close_event='test', task=test_task)

        console_output = string_io.getvalue().strip()
        sys.stdout = sys.__stdout__

        assert console_output == 'test'


