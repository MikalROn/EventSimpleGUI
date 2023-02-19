
class WinSimulator:
    """ This class can simulates a win """
    def __init__(self, event: str, values: dict):
        self._event = event
        self._values = values

    def Read(self):
        return self._event, self._values

    @staticmethod
    def close():
        return None
