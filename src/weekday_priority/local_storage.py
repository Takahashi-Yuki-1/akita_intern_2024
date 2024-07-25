import json

from weekday_priority.storage import WeekdayPriorityStorage


class LocalStorage(WeekdayPriorityStorage):
    _file_path = './../resource/weekday_priority_data.json'
    _encoding = 'utf-8'

    def load(self):
        """
        ローカルファイルから優先度情報を読み込む
        :return: 優先度情報
        :rtype: dict
        """
        with open(self._file_path, 'r', encoding=self._encoding) as file:
            return json.load(file)

    def save(self, data):
        """
        ローカルファイルへ引数の情報を保存する
        :param dict data: 優先度情報
        """
        with open(self._file_path, 'w', encoding=self._encoding) as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
