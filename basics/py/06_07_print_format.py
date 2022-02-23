# 変数を文字列に埋め込んで出力 : 文字列メソッドformat()
s = 'Alice'
i = 25
print('{} is {} years old'.format(s, i))

# インデックスを指定
print('{0} is {1} years old / {0}{0}{0}'.format(s, i))

# キーワード引数として指定
print('{name} is {age} years old / {age}{age}{age}'.format(name=s, age=i))
