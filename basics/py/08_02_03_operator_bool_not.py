# 論理演算子(not)
def operate_bool_not(num):
    if not num % 2 == 1:   # 奇数ではない
        print('  num is "not odd"')
    else:
        print('  num is not "not odd"')

print('num = 5')
operate_bool_not(5)

print('num = 10')
operate_bool_not(10)

print('num = -10')
operate_bool_not(-10)
