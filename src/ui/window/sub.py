import tkinter
from tkinter import ttk

from ui.widget.weekday_priority_setting import WeekdayPrioritySetting
from weekday_priority.manager import WeekdayPriorityManager

_WINDOW_TITLE = '設定画面'
_WINDOW_GEOMETRY = '300x250'
_DESCRIPTION = '月～金の優先度を選択して下さい'
_BUTTON_TEXT = 'OK'
_WEEKDAY_SETTING_RANGE = range(0, 4)


class SubWindow:
    window: tkinter.Toplevel
    description_label: tkinter.Label
    comboboxes: list[ttk.Combobox]
    button: ttk.Button

    def __init__(self, callback):
        self.window = tkinter.Toplevel()
        self.window.title(_WINDOW_TITLE)
        self.window.geometry(_WINDOW_GEOMETRY)

        tkinter.Label(self.window, text=_DESCRIPTION).pack()
        self._add_weekday_priorities_widgets()
        tkinter.Button(self.window, text=_BUTTON_TEXT,
                       command=self._on_ok_button_click(callback)).pack()

    def _add_weekday_priorities_widgets(self):
        self.comboboxes = []
        priority_manager = WeekdayPriorityManager()

        for i in _WEEKDAY_SETTING_RANGE:
            # 曜日ラベルセット
            priority_widgets = WeekdayPrioritySetting(self.window, i)
            priority_widgets.get_label().pack()
            # コンボボックスのセット
            priority_combobox = priority_widgets.get_combobox()
            priority_combobox.set(priority_manager.get_priority(i))
            priority_combobox.pack()
            self.comboboxes[i] = priority_combobox

    def _on_ok_button_click(self, callback):
        priority_manager = WeekdayPriorityManager()
        for i in _WEEKDAY_SETTING_RANGE:
            priority = self.comboboxes[i].get()
            priority_manager.set_priority(i, int(priority))
        priority_manager.save()

        callback()

