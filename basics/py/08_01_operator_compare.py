# 比較演算子
def operate_compare(num):
    if num >= 100:  # numが100以上（100を含む）
        print(f'  100 <= num({num})')
    elif num >= 50: # numが50より大きい（50を含む）
        print(f'  50 <= num({num}) < 100')
    elif num > 0:   # numが0より大きい（0を含まない）
        print(f'  0 < num({num}) <= 50')
    elif num == 0:  # numが0である
        print(f'  num({num}) == 0')
    else:           # numが0より小さい
        print(f'  num({num}) < 0')

print('num = 1000')
operate_compare(1000)

print('num = 70')
operate_compare(70)

print('num = 0')
operate_compare(0)

print('num = -100')
operate_compare(-100)
