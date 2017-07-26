# -*- coding: utf-8 -*-
"""準備運動 05.

与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""


def create_ngram_from_sequence(target, n):
    """指定されたリストからn-gramを作成.

    :param target: 対象となるリスト
    :param n: n-gramの値(1ならuni-gram, 2ならbi-gram)
    :return : gramのリスト
    """
    result = []
    for i in range(0, len(target) - n + 1):
        result.append(target[i:i + n])
    return result


def main():
    """メイン処理関数."""
    target_str = 'I am an NLPer'
    words_target = target_str.split(' ')

    # 単語bi-gram
    result = create_ngram_from_sequence(words_target, 2)
    print(result)

    # 文字bi-gram
    result = create_ngram_from_sequence(target_str, 2)
    print(result)

main()
