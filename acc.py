#建立商品與商品價格
product = []

print('註:按 "q" 結束商品建立模式')
while True:
	name = input ('請建立新商品名稱: ')
	if name == 'q':
		break
	price = input ('請輸入新商品的價格: ')
	item = [name, price]
	product.append(item)

#print(product) 


#分別列式剛剛建立的商品

for i in product:
	print('商品', i[0], '的價格為', i[1])