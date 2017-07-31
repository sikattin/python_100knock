# -*- coding: utf-8 -*-
"""UNIXコマンドの基礎 13. col1.txtとcol2.txtをマージ

12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
"""
import codecs
from helper import *

def merge_txtfile(file_1: str, file_2: str):
    """2つのテキストファイルをマージして新たなテキストファイルを生成する.

    :param file_1: ファイル1
    :param file_2: ファイル2
    """
    with codecs.open(filename=file_1, mode='r', encoding='utf-8') as file1:
        with codecs.open(filename=file_2, mode='r', encoding='utf-8') as file2:
            merge_list = ["{col1}\t{col2}".format(col1=str(col1).rstrip(), col2=col2) for col1, col2 in zip(file1, file2)]
            with codecs.open(filename='new_file.txt', mode='w', encoding='utf-8') as newfile:
                for row in merge_list:
                    newfile.write(str(row))


def main():
    """メイン処理関数."""
    import argparse
    argparser = argparse.ArgumentParser(description="2つのファイルの内容を統合して新しいファイルを生成するコマンド")
    argparser.add_argument('-f1', '--file1', metavar='<FILE1>', type=str, required=True, help="1つめのファイルURI")
    argparser.add_argument('-f2', '--file2', metavar='<FILE2>', type=str, required=True, help="2つ目のファイルURI")
    args = argparser.parse_args()

    merge_txtfile(args.file1, args.file2)

main()
