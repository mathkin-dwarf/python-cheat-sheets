# 無限ループ防止
LOOP_LIMIT = 10
MAX_LOOP = 0

l = ['Alice', 'Bob', 'Charlie']
i = 0
# 変数iがリストlの数よりも小さい場合のみ繰り返す
while (i < len(l)) & (MAX_LOOP < LOOP_LIMIT):
    if l[i] == 'Bob':
        print('!!BREAK!!')
        break
    
    print(f'i : {i} {l[i]}')
    
    # ここに「i += 1 」がなかった場合、無限ループになる
    
    MAX_LOOP += 1
