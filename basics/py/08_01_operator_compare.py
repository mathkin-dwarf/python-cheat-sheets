# 比較演算子

print('num = 1000')
num = 1000
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

print('num = 70')
num = 70
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

print('num = 0')
num = 0
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

print('num = -100')
num = -100
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
