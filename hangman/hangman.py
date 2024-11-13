import PySimpleGUI as sg

class Hangman:
    def __init__(self) -> None:
        self._window = sg.Window(
            title="Hangman",
            layout=[[]], #empty window
            finalize=True, #the window keeps it's layout during game execution, no modifying it
            margins=(100, 100),
        )

    def read_event(self):
        event = self._window.read()
        event_id = event[0] if event is not None else None
        return event_id

    def close(self):
        self._window.close()

if __name__ == "__main__":
    game = Hangman()
    # Event loop
    while True:
        event_id = game.read_event()
        if event_id in {sg.WIN_CLOSED}:
            break
    game.close()