# 辞書における繰り返し
d = {'key1': 1, 'key2': 2, 'key3': 3}

# キーのみの取得
for k in d:
    print(k)

# 値のみの取得
for v in d.values():
    print(v)

# キーと値両方の取得
for k, v in d.items():
    print(k, v)
