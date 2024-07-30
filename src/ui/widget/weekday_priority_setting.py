"""
曜日ごとの優先度を設定するコンボボックスとラベルのセット
"""
import tkinter.ttk as ttk
from weekday import WEEKDAY_CHARS


class WeekdayPrioritySetting:
    label: ttk.Label
    combobox: ttk.Combobox

    PRIORITY_LIST = ('1', '2', '3', '4', '5')
    COMBOBOX_STATE = 'readonly'

    def __init__(self, parent, weekday):
        self.label = ttk.Label(parent, text=WEEKDAY_CHARS[weekday])
        self.combobox = ttk.Combobox(parent, state=self.COMBOBOX_STATE, values=self.PRIORITY_LIST)

    def get_label(self):
        return self.label

    def get_combobox(self):
        return self.combobox
