# 16文字
str_sample_1 = '0123456789abcdef'

# 検索対象の文字列に検索文字列が含まれる場合
found_sample_1 = str_sample_1.find('9ab')
print(f'found_sample_1 :  {found_sample_1} ←見つかった検索文字列先頭のインデックスが取得される')

# 文字「_」を区切りに分解
found_sample_2 = str_sample_1.find('bs9')
print(f'found_sample_2 : {found_sample_2} ←見つからなかった場合は「-1」が取得される')
