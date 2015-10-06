def selectionsort(a):
	k = None
	j = 0
	while j != len(a):
		for i in range(j, len(a)):
			if k == None:
				k = i
			elif a[i] < a[k]:
				k = i
		a[j], a[k] = a[k], a[j]
		j = j+1
		k = None

	print(a)
	return(a)

a = [5,4,3,1,3,5,7,2,0]
selectionsort(a)

