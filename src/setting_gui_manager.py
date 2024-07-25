import tkinter as tk
from weekday_priority.manager import WeekdayPriorityManager
from weekday import WEEKDAY_CHARS
from weekday_priority_setting import WeekdayPrioritySetting

WEEKDAY_NUMBER = 5

def open_config_window():
    config_win = tk.Toplevel()
    config_win.title("設定画面")
    config_win.geometry("300x250")

    tk.Label(config_win, text="月～金の優先度を選択して下さい").pack()

    priority_manager = WeekdayPriorityManager()
    combolist = []

    #曜日ラベルと優先度コンボボックスのセット
    for i in range(WEEKDAY_NUMBER):
        #曜日ラベルセット
        priority_setting = WeekdayPrioritySetting(config_win,WEEKDAY_CHARS.get(i))
        priority_setting.get_label().pack()

        #コンボボックスのセット
        priority_combo = priority_setting.get_combobox()
        priority_combo.set(priority_manager.get_priority(i))
        combolist.append(priority_combo) #値取得用のcomboboxリストの作成
        priority_combo.pack()

    # ボタンの作成
    button = tk.Button(config_win, text="優先度をセット",
                       command=set_selected_priority(priority_manager,combolist))
    button.pack()

def set_selected_priority(manager,combolist):
    for i in range(WEEKDAY_NUMBER):
        priority = combolist[i].get()
        manager.set_priority(i,int(priority))
    manager.save()


