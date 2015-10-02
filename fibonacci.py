def fibbonaci(num):

	a = 0
	b = 1
	c = 0
	list = []

	while num > 0:

		list.append(a)
		a , b = b , a + b
		num = num - 1
	print(list)
fibbonaci(5)

