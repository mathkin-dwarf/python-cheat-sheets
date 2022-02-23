# リストの要素とインデックスを同時に取得して繰り返す「enumerate()」
l = ['Alice', 'Bob', 'Charlie']
n = [12, 34, 56]

for name in l:
    print(name)

for index, number in enumerate(n):
    print(index, number)
