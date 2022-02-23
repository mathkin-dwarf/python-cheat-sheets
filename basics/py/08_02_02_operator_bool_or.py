# 論理演算子(or)
def operate_bool_or(num):
    if num >= 0 or num % 2 == 1:   # 0以上もしくは奇数
        print('  num is "positive or odd"')
    else:
        print('  num is not "positive or odd"')

print('num = 5')
operate_bool_or(5)

print('num = 10')
operate_bool_or(10)

print('num = -10')
operate_bool_or(-10)
