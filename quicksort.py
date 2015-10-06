def quicksort(a,lo,hi):
	if lo < hi:
		pivot = partition(a, lo, hi)

		quicksort(a, lo, pivot-1)
		quicksort(a, pivot+1, hi)

	
	return a

def partition(a, lo, hi):
	pivot = hi
	i = lo 

	while i != pivot:
		if a[i] > a[pivot] and abs(pivot-i) == 1:
			a[pivot], a[i] = a[i], a[pivot]

		elif a[i] > a[pivot]:
			a[pivot], a[pivot-1], a[i]= a[i], a[pivot], a[pivot-1]
			pivot = pivot -1 

		else:
			i = i+1


	print a		
	return pivot




a = [5,3,1,0,7,4]
quicksort(a,0,5)

