# for文を途中で終了する「break」
l = ['Alice', 'Bob', 'Charlie']

for name in l:
    if name == 'Bob':
        print('!!BREAK!!')
        break
    print(name)
