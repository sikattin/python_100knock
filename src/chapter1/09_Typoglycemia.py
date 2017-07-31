# -*- coding: utf-8 -*-
"""準備運動 09.

スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．

ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば"I couldn't believe that I could actually understand
 what I was reading : the phenomenal power of the human mind ."）を与え，
その実行結果を確認せよ．
"""
import random


def shuffle_str(target: str) -> str:
    """
    受け取った文字列を単語単位で(ただし先頭と末尾はそのままで)並び替えを行い、並び替え後の文字列を返す.

    ただし、長さ4以下の単語は並び替えない.
    :param target: 対象文字列
    :return : 並び替え後の文字列
    """
    result_str = []
    target_str = target.split(' ')
    for words in target_str:
        if len(words) <= 4:
            result_str.append(words)
        else:
            char_list = list(words[1:-1])
            random.shuffle(char_list)
            result_str.append("{first}{shuffle_str}{last}".format(
                first=words[0],
                shuffle_str=''.join(char_list),
                last=words[-1]))
    return ' '.join(result_str)


def main():
    """メイン処理関数."""
    target_str = "I couldn't believe that I could actually understand" \
                 " what I was reading : the phenomenal power of the human mind ."
    result_str = shuffle_str(target_str)
    print(result_str)

main()
