import re
import pathlib
import os

file = path = input("抽出したいログデータをドラッグ&ドロップしてください")
user = input("抽出したいユーザー名を入力してください(半角/全角|大文字/小文字を区別")
file = re.sub(r"\.log", "", file)
file = re.sub(r"C\:", "", file)
file = re.sub(r"Users", "", file)
file = re.sub(r"BNO", "", file)
file = re.sub(r"GundamOnline", "", file)
file = re.sub(r"chat", "", file)
file = re.sub(r"\\", "", file)
path = re.sub(r"\s", "", path)
path = pathlib.Path(path)
print(file)

with open(path,encoding='U16') as f:
    l_strip = [s.strip() for s in f.readlines()]
    
l = [l for l in l_strip if user in l]
l = '\n'.join(l)
print(l)

f = open(str(file)+ ".txt", 'w',encoding='UTF-8')
for x in l:
    f.write(str(x))
f.close()
