# -*- coding: utf-8 -*-
"""準備運動 08.

与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""
import re


def clipher(target_str: str) -> str:
    """文字列の暗号・復号化を行い、処理後の文字列を返す.

    :param target: 対象文字列
    """
    result_str = ''
    for target_char in target_str:
        m_alpha = re.compile("[a-z]")
        if m_alpha.search(target_char):
            result_str += chr((219 - ord(target_char)))
        else:
            result_str += target_char
    return result_str

    """ここで学んだこと.
    ord(char) 1文字の Unicode文字のUnicodeコードポイント」を表す整数を返す組み込み関数.
    chr(int) Unicodeコードポイントが整数 i である文字を表す文字列を返す.
    """


def main():
    """メイン処理関数."""
    target_str = 'ABcdefG123erFv'

    # 暗号化
    decrypt_str = clipher(target_str)
    print(decrypt_str)

    # 復号化
    encrypt_str = clipher(decrypt_str)
    print(encrypt_str)

main()
