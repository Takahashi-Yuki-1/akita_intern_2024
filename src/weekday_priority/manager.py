import json
from weekday_priority.local_storage import LocalStorage
from weekday_priority.storage import WeekdayPriorityStorage


class WeekdayPriorityManager:
    """
    曜日優先度情報を管理するクラス
    """
    _storage: WeekdayPriorityStorage
    _weekday_priorities: dict

    def __init__(self):
        self._storage = LocalStorage()
        self._weekday_priorities = self._storage.load()

    def save(self):
        """
        引数の優先度情報をファイルへ保存する
        """
        self._storage.save(self._weekday_priorities)

    def get_priority(self, weekday_id):
        """
        指定した曜日の優先度を取得する
        :param int weekday_id: 曜日 (月=0, 火=1, ..., 日=6)
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
        :param int weekday_id: 曜日 (月=0, 火=1, ..., 日=6)
        :param int priority: 優先度 (1~5)
        :raise ValueError: 引数の値が不正
        """
        if 0 > priority | 6 < priority:
            raise ValueError('引数 priority が不正です')

        for weekday in self._weekday_priorities:
            if weekday_id == weekday['id']:
                weekday['priority'] = priority
                return

        raise ValueError('引数 weekday_id が不正です')
