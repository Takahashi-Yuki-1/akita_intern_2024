import json
from abc import ABC, abstractmethod


class WeekdayPriorityManager:
    """
    曜日優先度情報を管理するクラス
    """
    _file_path = './../resource/weekday_priority_data.json'

    _weekday_priorities: dict

    def __init__(self):
        self.load()

    def load(self):
        """
        ファイルから曜日優先度の情報をロードする
        """
        with open(self._file_path, 'r', encoding='utf-8') as file:
            self._weekday_priorities = json.load(file)

    def save(self):
        """
        引数の優先度情報をファイルへ保存する
        """
        with open(self._file_path, 'w', encoding='utf-8') as file:
            json.dump(self._weekday_priorities, file, ensure_ascii=False, indent=2)

    def get_priority(self, weekday_id):
        """
        指定した曜日の優先度を取得する
        :param int weekday_id: 曜日 (日=0, 月=1, ..., 土=6)
        :return: 優先度
        :rtype: int
        :raise ValueError: 引数の値が不正
        """
        for weekday in self._weekday_priorities:
            if weekday_id == weekday['id']:
                return weekday['priority']

        raise ValueError('引数 weekday_id が不正です')

    def get_priority_all(self):
        """
        日~土までの全ての曜日の優先度をリストで取得する
        :return: 全ての曜日の優先度
        :rtype: list[int]
        """
        priorities = []

        for weekday in self._weekday_priorities:
            priorities.append(weekday['priority'])

        return priorities

    def set_priority(self, weekday_id, priority):
        """
        指定した曜日の優先度を変更する
        :param int weekday_id: 曜日 (日=0, 月=1, ..., 土=6)
        :param int priority: 優先度 (1~5)
        :raise ValueError: 引数の値が不正
        """
        if 1 > priority | 5 < priority:
            raise ValueError('引数 priority が不正です')

        for weekday in self._weekday_priorities:
            if weekday_id == weekday['id']:
                weekday['priority'] = priority
                return

        raise ValueError('引数 weekday_id が不正です')
