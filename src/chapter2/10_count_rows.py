# -*- coding: utf-8 -*-
"""UNIXコマンドの基礎 10.

行数をカウントせよ．確認にはwcコマンドを用いよ．
"""
import codecs
from helper import *


def count_rows(input_files: list) -> list:
    """インプットファイルの行数を返す.

    :param input: input file name.
    :return : total rows.
    """
    row_num = []
    for input_file in input_files:
        with codecs.open(filename=input_file, mode='r', encoding='utf-8') as file:
            row_num.append(len(list(file)))
    return row_num


def main():
    """メイン処理関数."""
    input_filename = get_input_filename()
    number_of_rows = count_rows(input_filename)
    print(number_of_rows)

main()
