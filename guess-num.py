#產生一個隨機整數1~100（不要印出來）
#讓使用者重複輸入數字去猜
#猜對的話，就印出"終於猜對了"
#猜錯的話，要告訴他，比答案大/小

import random

start = int(input("請決定隨機數字範圍的開始值："))
end = int(input("請決定隨機數字範圍的結束值："))
r = random.randint(start, end)
count = 0 #計算猜了多少次
while True:
	count += 1  #count = count + 1
	num = int(input("請猜數字：")
	if num == r:
		print("你猜對了")
		print("用了", count, "次猜中")
		break
	elif num > r:
		print("比答案大")
	elif num < r:
		print("比答案小")
	print("這次是你猜的第", count, "次")	
