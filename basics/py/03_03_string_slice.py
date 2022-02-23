# 20文字
str_sample_20 = '0123456789abcdefghij'

# 4文字目から11文字目まで(index : 3~10, string : '3456789a' )を取得
str_4_11 = str_sample_20[3:11]
print(f'str_4_11    : str_sample_20[3:10] : {str_4_11}\n')

# 先頭から7文字目まで(index : 0~7, string : '0123456' )を取得
str_begin_7 = str_sample_20[:7]
print(f'str_begin_7 : str_sample_20[:7]   : {str_begin_7}')
str_0_7 = str_sample_20[0:7]
print(f'str_0_7     : str_sample_20[0:7]  : {str_0_7}')

print(f'    →「str_sample_20[:7]」と「str_sample_20[0:7]」は同じ処理になる\n')

# 9文字目から最後までを(index : 8~19, string : '3456789b' )取得
str_9_end = str_sample_20[8:]
print(f'str_9_end   : str_sample_20[8:]   : {str_9_end}')

str_9_19 = str_sample_20[8:20]
print(f'str_9_19    : str_sample_20[8:20] : {str_9_19}')

print(f'    →「str_sample_20[8:]」と「str_sample_20[8:20]」は同じ処理になる')
