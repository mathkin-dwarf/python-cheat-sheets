# 16文字
str_sample_1 = '0123456789abcdef'
# 16文字（アンダースコア入り）
str_sample_2 = '01234_6789ab_def'

# 文字「7」を区切りに分解
divided_sample_1 = str_sample_1.split('7')
print(f'divided_sample_1 : {divided_sample_1}    ←区切りとなった「7」は含まれない')

# 文字「_」を区切りに分解
divided_sample_2 = str_sample_2.split('_')
print(f'divided_sample_2 : {divided_sample_2} ←区切りとなった「_」は含まれない')
