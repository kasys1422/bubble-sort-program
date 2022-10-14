# coding: utf-8
import random
print("[バブルソートプログラム]")
# 変数
data = []      # 格納用リスト
data_max = 100 # 乱数の最大値
data_min = 0   # 乱数の最小値
# 入力
data_num = int(input("リストの乱数の数を入力してください:"))
is_desc_offset = input("ソートを降順にしますか(Y/N):")
if(is_desc_offset in ["Y","y","yes"]):
    is_desc_offset = [1,0]
else:
    is_desc_offset = [0,1]
# 乱数生成
for i in range(data_num):
    data.append(random.randint(data_min,data_max))
print("元のデータ　　　:" + str(data))
# バブルソート
for i in range(data_num):
    for j in range(data_num - i - 1):
        if data[j + is_desc_offset[0]] > data[j + is_desc_offset[1]]:
            buf = data[j + is_desc_offset[1]]
            data[j + is_desc_offset[1]] = data[j + is_desc_offset[0]]
            data[j + is_desc_offset[0]] = buf
print("ソート後のデータ:" + str(data))
