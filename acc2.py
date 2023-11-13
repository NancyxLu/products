
import os
product = []

#讀取檔案 一格一格開起來
def checked_open(file) :
	with open(file,'r',encoding = 'utf-8') as f:
		for line in f:
			if '商品名稱,價格' in line:
				continue
			name, price = line.strip().split(',')
			product.append([name, price])
	print (product)
	return product

#輸入商品
def input_new_item(product) :
	print('註:按 "q" 結束商品建立模式')
	while True:
		name = input ('請建立新商品名稱: ')
		if name == 'q':
			break
		price = input ('請輸入新商品的價格: ')
		product.append([name, price])
	return product

#列印表頭和商品
def print_all(product) :
	for i in product:
		print('商品', i[0], '的價格為', i[1])


#將輸入的商品存到CSV檔案裡
def save_new(file,product) :
	with open (file, 'w', encoding = 'utf-8') as f:
		f.write('商品名稱'+','+'價格'+'\n')
		for i in product:
			f.write(i[0] + ',' +  i[1] + '\n')


def main(m,b) :
	#檢查檔案存不存在
	if os.path.isfile(m):
		print('找到已經建立的檔案，內容如下:')
		checked_open(m)
	else:
		print('沒有歷史檔案內容')
	input_new_item(b)
	print_all(b)
	save_new(m, b)


main(m='menu.csv',b=product)