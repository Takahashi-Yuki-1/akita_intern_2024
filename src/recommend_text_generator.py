import dataclasses


def generate_recommend_text(dates):
    """
    日付ごとの優先度を元に、おすすめコメントを生成する
    :param list[PrioritizedDate] dates: 優先度付きの日付クラスのリスト
    :return: おすすめコメント
    :rtype: str
    """

    most_recommended_date = None
    for date in dates:
        if most_recommended_date is None:
            most_recommended_date = date

        if date.priority >= most_recommended_date:
            most_recommended_date = date.priority

    if most_recommended_date.priority < 3:
        return '出社をおすすめできる日がありません...'
    else:
        return '出社おすすめ日は {} です！'.format(most_recommended_date.string)


@dataclasses.dataclass
class PrioritizedDate:
    """
    優先度付きの日付クラス. おすすめコメント生成用に情報を一元化
    """
    def __init__(self, string, priority):
        self.string = string
        self.priority = priority

    @classmethod
    def builder(cls):
        """
        おすすめコメント生成のインプット要素となる優先度付きの日付クラスを作成するビルダークラスを取得する
        :return: ビルダークラス
        :rtype: PrioritizedDate.Builder
        """
        return PrioritizedDate.Builder()

    class Builder:
        string: str
        priority: int

        def string(self, string):
            """
            日付の文字列をセットする
            :param str string: 日付文字列
            """
            self.string = string

        def priority(self, priority):
            """
            優先度をセットする
            :param int priority: 曜日優先度
            """
            self.priority = priority

        def build(self):
            """
            優先度付きの日付クラスを生成する
            :return: 優先度付きの日付クラス
            :rtype: RecommendTextGenerator.Date
            """
            if self.string is None or self.priority is None:
                raise ValueError('必須パラメータが設定されていません')
            return PrioritizedDate(self.string, self.priority)
