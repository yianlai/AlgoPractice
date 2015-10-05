def bubblesort(a):

	j = 0

	while j != (len(a)-1):
		j = 0
		for i in range(0, (len(a)-1)):
			first = a[i]
			second = a[i+1]

			if first > second:
				a[i] = second
				a[i+1] = first
			else:
				j = j+1

	print (a)
	return a
			
	






a = [9,2,7,1,6,3,7,8]
bubblesort(a)