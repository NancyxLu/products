
import os

product = []

#檢查檔案存不存在
if os.path.isfile('menu.csv'):
	print('找到已經建立的檔案，內容如下:')
#讀取檔案 一格一格開起來
	with open('menu.csv','r',encoding = 'utf-8') as f:
		for line in f:
			if '商品名稱,價格' in line:
				continue
			name, price = line.strip().split(',')
			product.append([name, price])
	print (product)
else:
	print('沒有歷史檔案內容')
	
#輸入商品
print('註:按 "q" 結束商品建立模式')

while True:
	name = input ('請建立新商品名稱: ')
	if name == 'q':
		break
	price = input ('請輸入新商品的價格: ')
	item = [name, price]
	product.append(item)
#列印剛剛輸入的商品
for i in product:
	print('商品', i[0], '的價格為', i[1])

#將輸入的商品存到CSV檔案裡
with open ('menu.csv', 'w', encoding = 'utf-8') as file:
	file.write('商品名稱'+','+'價格'+'\n')
	for i in product:
		file.write(i[0] + ',' +  i[1] + '\n')