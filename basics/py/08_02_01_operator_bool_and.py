# 論理演算子(and)
def operate_bool_and(num):
    if num >= 0 and num % 2 == 1:   # 0以上かつ奇数
        print('  num is "positive odd"')
    else:
        print('  num is not "positive odd"')

print('num = 5')
operate_bool_and(5)

print('num = 10')
operate_bool_and(10)

print('num = -10')
operate_bool_and(-10)
