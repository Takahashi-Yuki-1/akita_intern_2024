import tkinter as tk
from tkinter import ttk
from setting_gui_manager import open_config_window

class RecommendWeatherView:
    treeview: ttk.Treeview
    label: ttk.Label
    button: ttk.Button
    quit_button: ttk.Button

    def __init__(self, root):
        root.title("出社日おすすめお天気アプリ")
        self._make_treeview(root)
        self._make_label(root)
        self._make_button(root)
        self._make_quit(root)

    def _make_treeview(self,root):
        self.treeview = ttk.Treeview(root)

    def _make_label(self,root):
        self.label = ttk.Label(root)

    def _make_button(self,root):
        self.button = ttk.Button(root,text="設定",command=open_config_window)

    def _make_quit(self,root):
        self.quit_button = ttk.Button(root,text="終了",command=root.quit)

    def get_treeview(self):
        return self.treeview

    def get_label(self):
        return self.label

    def get_button(self):
        return self.button

    def get_quit_button(self):
        return self.quit_button

    def set_treeview(self,tree):
        self.treeview = tree

