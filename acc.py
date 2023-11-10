
product = []

print('註:按 "q" 結束商品建立模式')
while True:
	name = input ('請建立新商品名稱: ')
	if name == 'q':
		break
	price = input ('請輸入新商品的價格: ')
	item = [name, price]
	product.append(item)

print(product) 
