"""
曜日ごとの優先度を設定するコンボボックスとラベルのセット
"""
import tkinter.ttk as ttk
from weekday import WEEKDAYS


class WeekdayPrioritySetting:
    label: ttk.Label
    combobox: ttk.Combobox

    PRIORITY_LIST = ('1', '2', '3', '4', '5')
    COMBOBOX_STATE = 'readonly'

    def __init__(self, base, weekday: WEEKDAYS):
        self.label = ttk.Label(base, text=weekday.character)
        self.combobox = ttk.Combobox(base, state=self.COMBOBOX_STATE, values=self.PRIORITY_LIST)

    def get_label(self):
        return self.label

    def get_combobox(self):
        return self.combobox
