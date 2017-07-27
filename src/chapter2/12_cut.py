# -*- coding: utf-8 -*-
"""UNIXコマンドの基礎 12.1列目をcol1.txtに，2列目をcol2.txtに保存

各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
"""
import codecs
from helper import *


def cut_column_from_row(input_files: list):
    with codecs.open(filename='col1.txt', mode='w', encoding='utf-8') as col1:
        with codecs.open(filename='col2.txt', mode='w', encoding='utf-8') as col2:
            for input_file in input_files:
                with codecs.open(filename=input_file, mode='r', encoding='utf-8') as src:
                    for row in src:
                        split_row = row.split('\t')
                        col1.write(split_row[0] + "\n")
                        col2.write(split_row[1] + "\n")


def main():
    """メイン処理関数."""
    input_filenames = get_input_filename()
    cut_column_from_row(input_filenames)


main()
