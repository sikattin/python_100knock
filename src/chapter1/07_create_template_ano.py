# -*- coding: utf-8 -*-
"""準備運動 07.

引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""
from string import Template


def create_template_str(x: str, y: str, z: str):
    """決まった文字列を返す関数.

    :param x: str
    :param y: str
    :param z: str
    :return: template string => "x時のyはz"
    """
    template_str = Template('$hour時の$targetは$value')
    return template_str.substitute(hour=x, target=y, value=z)


def main():
    """メイン処理関数."""
    print(create_template_str(x=12, y="気温", z="22.4"))


main()
