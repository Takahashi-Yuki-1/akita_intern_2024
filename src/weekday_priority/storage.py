from abc import ABC, abstractmethod


class WeekdayPriorityStorage(ABC):
    @abstractmethod
    def load(self):
        """
        曜日優先度の情報を外部記憶から読み込む
        :return: 曜日優先度情報
        :rtype: Any
        """
        pass

    @abstractmethod
    def save(self, data):
        """
        曜日優先度の情報を外部記憶へ保存する
        :param Any data: 保存データ
        """
        pass
