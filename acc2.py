#讀取檔案 一格一格開起來

oplist = []
with open('menu.csv','r',encoding = 'utf-8') as f:
	for line in f:
		if '商品名稱,價格' in line:
			continue
		name, price = line.strip().split(',')
		oplist.append([name, price])
print (oplist)

print('註:按 "q" 結束商品建立模式')
product = []
while True:
	name = input ('請建立新商品名稱: ')
	if name == 'q':
		break
	price = input ('請輸入新商品的價格: ')
	item = [name, price]
	product.append(item)

for i in product:
	print('商品', i[0], '的價格為', i[1])

with open ('menu.csv', 'w', encoding = 'utf-8') as file:
	file.write('商品名稱'+','+'價格'+'\n')
	for i in product:
		file.write(i[0] + ',' +  i[1] + '\n')