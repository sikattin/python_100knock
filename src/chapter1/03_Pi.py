# -*- coding: utf-8 -*-
"""準備運動 03.

"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""
target_str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
result_target = target_str.split(' ')
result = []
for word in result_target:
    count = 0
    for char in word:
        if char.isalpha():
            count += 1
    result.append(count)
print(result)
