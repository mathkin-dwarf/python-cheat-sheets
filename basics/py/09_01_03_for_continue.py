# その時点以降の処理をスキップする「continue」
l = ['Alice', 'Bob', 'Charlie']

for name in l:
    if name == 'Bob':
        print('!!SKIP!!')
        continue
    print(name)
