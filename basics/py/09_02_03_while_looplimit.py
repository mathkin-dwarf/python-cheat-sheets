# 無限ループ防止
LOOP_LIMIT = 10
LOOP_COUNT = 0

l = ['Alice', 'Bob', 'Charlie']
i = 0
# 変数iがリストlの数よりも小さい場合のみ繰り返す
while (i < len(l)) & (LOOP_COUNT < LOOP_LIMIT):
    if l[i] == 'Bob':
        print('!!BREAK!!')
        break
    
    print(f'i : {i} {l[i]}')
    
    # ここに「i += 1 」がなかった場合、無限ループになる
    
    LOOP_COUNT += 1
