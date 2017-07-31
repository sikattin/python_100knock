# -*- coding: utf-8 -*-
"""UNIXコマンドの基礎 15. 末尾のN行を出力

自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ．
"""
import codecs
from helper import *


def print_tail(file: str, num: int):
    """ファイルの末尾N行を表示する.

    :param file: ファイルURI
    :param num: 行数
    """
    with codecs.open(filename=file, mode='r', encoding='utf-8') as src_file:
        if num > 0:
            src_tuple = tuple(src_file)[-num:]
            if num > len(src_tuple):
                raise ValueError("行数の指定は {} 以下でなければなりません.".format(len(src_tuple)))
                return
            for row in src_tuple:
                print(row.rstrip())


def main():
    """メイン処理関数."""
    import argparse
    argparser = argparse.ArgumentParser(description="ファイルの末尾N行を表示するコマンド.")
    argparser.add_argument('-f', '--file', metavar='<FILE>', type=str, required=True, help="ファイルURI")
    argparser.add_argument('-n', '--number', metavar='<NUMBER>', type=int,
                           default=10, required=False, help="末尾の何行目を表示するのかの数値. デフォルトは10.")
    args = argparser.parse_args()

    print_tail(args.file, args.number)


main()