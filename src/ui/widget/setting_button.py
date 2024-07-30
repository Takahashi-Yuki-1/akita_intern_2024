import tkinter
from tkinter import ttk, Button
from ui.window.sub import SubWindow

_BUTTON_TEXT = '設定'


class SettingButton(Button):
    button: ttk.Button

    def __init__(self, parent, callback):
        super().__init__(parent, text=_BUTTON_TEXT)
        self.config(command=self._on_click(callback))

    def add_event(self, event):
        if event is not None:
            self.config(command=event)

    def _on_click(self, callback):
        sub_window = SubWindow(callback)


