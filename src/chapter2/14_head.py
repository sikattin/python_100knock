# -*- coding: utf-8 -*-
"""UNIXコマンドの基礎 14. 先頭からN行を出力

自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．
"""
import codecs
from helper import *

def print_head(file: str, num: int):
    """ファイルの先頭から引数で与えられた行数分出力する.

    :param file: ファイルURI
    :param num: 行数
    """
    with codecs.open(filename=file, mode='r', encoding='utf-8') as src_file:
        tuple_row = tuple(src_file)
        if num > len(tuple_row):
            raise ValueError("行数の指定は {} 以下でなければなりません.".format(len(tuple_row)))
            return
        for i in range(num):
            print(tuple_row[i].rstrip())


def main():
    """メイン処理関数."""
    import argparse
    argparser = argparse.ArgumentParser(description="ファイルの先頭N行を表示するコマンド.")
    argparser.add_argument('-f', '--file', metavar='<FILE>', type=str, required=True, help="ファイルURI")
    argparser.add_argument('-n', '--number', metavar='<NUMBER>', type=int,
                           default=10, required=False, help="先頭から何行目までを表示するのかの数値. デフォルトは10.")
    args = argparser.parse_args()

    print_head(args.file, args.number)


main()