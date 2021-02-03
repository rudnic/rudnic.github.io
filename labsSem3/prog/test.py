lst = [11, 3, 8, 1, 10, 12, 6]
target = 13
dct = {}

for i in lst:
	dct[target - i] = i

for i in dct.values():
	if i in dct:
		print(dct[i], i)
