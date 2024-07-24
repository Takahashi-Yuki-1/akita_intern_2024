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

        if date.recommendation >= most_recommended_date.recommendation:
            most_recommended_date = date

    if most_recommended_date.recommendation < 3:
        return '出社をおすすめできる日がありません...'
    else:
        return '出社おすすめ日は {} です！'.format(most_recommended_date.string)


@dataclasses.dataclass
class PrioritizedDate:
    """
    優先度付きの日付クラス. おすすめコメント生成用に情報を一元化
    """
    string: str
    recommendation: int

    def __init__(self, string, recommendation):
        self.string = string
        self.recommendation = recommendation

    @classmethod
    def builder(cls):
        """
        おすすめコメント生成のインプット要素となる優先度付きの日付クラスを作成するビルダークラスを取得する
        :return: ビルダークラス
        :rtype: PrioritizedDate.Builder
        """
        return PrioritizedDate.Builder()

    class Builder:
        _string: str
        _recommendation: int

        def string(self, string):
            """
            日付の文字列をセットする
            :param str string: 日付文字列
            :return: ビルダークラス
            :rtype: PrioritizedDate.Builder
            """
            self._string = string
            return self

        def recommendation(self, recommendation):
            """
            優先度をセットする
            :param int recommendation: 曜日優先度
            :return: ビルダークラス
            :rtype: PrioritizedDate.Builder
            """
            self._recommendation = recommendation
            return self

        def build(self):
            """
            優先度付きの日付クラスを生成する
            :return: 優先度付きの日付クラス
            :rtype: RecommendTextGenerator.Date
            """
            if self._string is None or self._recommendation is None:
                raise ValueError('必須パラメータが設定されていません')
            return PrioritizedDate(self._string, self._recommendation)
