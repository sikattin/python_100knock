# -*- coding: utf-8 -*-
"""UNIXコマンドの基礎 11.

タブ1文字につきスペース1文字に置換せよ．
確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""
import codecs
from helper import *


def replace_tab_to_space(input_files: list):
    """タブをスペースに置換して新しいファイルを出力する.

    :param input_files: インプットファイル名
    :return:
    """
    for idx, input_file in enumerate(input_files):
        with codecs.open(filename=input_file, mode='r', encoding='utf-8') as file:
            with codecs.open(filename='output_{}.txt'.format(idx), mode='w', encoding='utf-8') as output_file:
                for row in file:
                    import re
                    output_file.write(re.sub(r'\t', ' ', str(row)))

                if os.path.exists('.\output_{}.txt'.format(idx)):
                    print("文字列を置換した結果を .\output_{}.txt に出力しました.".format(idx))


def main():
    """メイン処理関数."""
    input_filenames = get_input_filename()
    replace_tab_to_space(input_filenames)


main()
