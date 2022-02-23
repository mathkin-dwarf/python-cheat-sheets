# 途中で終了する「break」
l = ['Alice', 'Bob', 'Charlie']
i = 0
# 変数iがリストlの数よりも小さい場合のみ繰り返す
# whileの条件はTrueなのでそのままだと無限ループになる
while True:
    if l[i] == 'Bob':
        print('!!BREAK!!')
        break
    
    print(f'i : {i} {l[i]}')
    
    i += 1
