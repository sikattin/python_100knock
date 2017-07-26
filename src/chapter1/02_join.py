# -*- coding: utf-8 -*-
"""準備運動 02.

「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""
target_str_01 = 'パトカー'
target_str_02 = 'タクシー'

list_target_01 = list(target_str_01)
list_target_02 = list(target_str_02)
tuple_targets = tuple(zip(list_target_01, list_target_02))
result_str = ''
for tuple_target in tuple_targets:
    result_str += ''.join(tuple_target)
print(result_str)
