# 基本の繰り返し処理
l = ['Alice', 'Bob', 'Charlie']

i = 0
# 変数iがリストlの数よりも小さい場合のみ繰り返す
# len(l)は3なので、iが3になった時点でwhileの条件から外れて繰り返し終了になる
while i < len(l):
    print(f'i : {i} {l[i]}')
    
    i+=1
