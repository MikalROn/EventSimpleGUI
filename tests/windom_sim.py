
class WinSimulator:
    """ This class can simulates a win """
    def __init__(self, event: str, values: dict):
        self._event = event
        self._values = values

    def chage_event(self, new_event: str) -> None:
        self._event = new_event

    def Read(self) -> tuple[str, dict]:
        return self._event, self._values

    @staticmethod
    def close():
        """ Test event to avoid errors """
