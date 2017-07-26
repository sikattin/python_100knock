# -*- coding: utf-8 -*-
"""準備運動 06.

"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
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
    target_str_1 = 'paraparaparadise'
    target_str_2 = 'paragraph'

    # target_str_1 の 文字bi-gram
    x = set(create_ngram_from_sequence(target_str_1, 2))
    print("X: {}".format(x))
    # target_str_2 の 文字bi-gram
    y = set(create_ngram_from_sequence(target_str_2, 2))
    print("Y: {}".format(y))

    # x と y　の和集合
    print("x と y　の和集合: {}".format(x.union(y)))
    # x と y の積集合
    print("x と y　の積集合: {}".format(x.intersection(y)))
    # x と y の差集合
    print("x と y　の差集合: {}".format(x.difference(y)))

main()
