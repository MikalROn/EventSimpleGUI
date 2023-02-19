import pytest
import pyautogui
import PySimpleGUI as sg
from pysimpleevent.fastevent import EventSimpleGUI


class Test:
    """ Testing all features from main code """
    def test_if_event_go_to_list_of_events_using_decor(self):
        loop = EventSimpleGUI()

        @loop.event('test')
        def event_test(*args):
            pass
        assert event_test in loop.get_events

    def test_if_event_go_to_list_of_events_using_add_event(self):
        loop = EventSimpleGUI()

        def event_test(*args):
            ...
        loop.add_event(event_test)
        assert event_test in loop.get_events


