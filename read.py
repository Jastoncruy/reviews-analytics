data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('读取完毕,总共有', len(data), '行的文本数据') 

sum_len = 0
for L in data:
	sum_len = sum_len + len(L)
	a = sum_len / len(data)
print('每一行的平均长度为',a)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '行的文本数据小于100')
print(new[0])
