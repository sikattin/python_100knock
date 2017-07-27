# -*- coding: utf-8 -*-
"""汎用系メソッドをまとめた."""
import os
import glob


def get_input_filename() -> list:
    """インプット対象となるファイル名を取得する."""
    # スクリプトが配置されているディレクトリの絶対パスを取得するおまじない.
    abs_path = os.path.abspath(os.path.dirname(__file__))
    search_path = abs_path + '\*.txt'
    print("search_path= {}".format(search_path))

    # .txtファイルのみのファイルパスを取得して、これのファイル名のみをリストに格納している.
    filename_list = [os.path.basename(filepath) for filepath in glob.glob(search_path)]
    return filename_list
