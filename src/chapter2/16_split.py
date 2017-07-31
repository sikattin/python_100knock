# -*- coding: utf-8 -*-
"""UNIXコマンドの基礎 16. ファイルをN分割する

自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""
import codecs
from helper import *
from collections import OrderedDict


def split_file(file: str, num: int):
    """与えられた数値単位でファイルを分割する.

    :param file: ファイルURI
    :param num: 何行単位でファイルを分割するかの数値
    """
    with codecs.open(filename=file, mode='r', encoding='utf-8') as src_file:
        src_tuple = tuple(src_file)
        row_num = int(len(src_tuple))
        split_num = int(row_num / num)
        if num > row_num:
            raise ValueError("行数の指定は {} 以下でなければなりません.".format(row_num))
            return
        # N行単位で分割した辞書を作成.
        dict_split_rows = OrderedDict()
        for i in range(split_num):
            dict_split_rows[i] = src_tuple[num * i:num * (i+1)]
            with codecs.open(filename='{prefix}_{filename}'.format(prefix=i+1, filename=file),
                             mode='w',
                             encoding='utf-8') as split_file:
                for row in dict_split_rows[i]:
                    split_file.write(row.rstrip())
        # 端数行がある場合の処理.
        if not row_num % num == 0:
            with codecs.open(filename='{prefix}_{filename}'.format(prefix=split_num+1, filename=file),
                             mode='w',
                             encoding='utf-8') as split_file:
                for row in src_tuple[num * split_num:]:
                    split_file.write(row.rstrip())


def main():
    """メイン処理関数."""
    import argparse
    argparser = argparse.ArgumentParser(description="ファイルをN分割するコマンド.")
    argparser.add_argument('-f', '--file', metavar='<FILE>', type=str, required=True, help="ファイルURI")
    argparser.add_argument('-n', '--number', metavar='<NUMBER>', type=int,
                            required=True, help="何行単位でファイルを分割するかの数値.")
    args = argparser.parse_args()

    split_file(file=args.file, num=args.number)


main()