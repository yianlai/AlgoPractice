def test(a):
	#length of the merge list
	
	i = 2
		
	while i/2 <= len(a):
		m=0
		for j in range(0, len(a), i):

			left = a[j:j+i/2]
			right = a[j+i/2:j+i]

			k=0
			l=0
			

			while k < len(left) and l < len(right):
				if left[k] < right[l]:
					a[m] = left[k]
					k = k+1

				else:
					a[m] = right[l]
					l = l+1
				

				m = m + 1
			while k < len(left):
				a[m] = left[k]
				k = k+1
				m = m + 1

			while l < len(right):
				a[m] = right[l]
				l = l+1
				m = m + 1
		i *= 2 

	print a

a = [5,1,3,4,9,8,0,2,7,10,6,1]
test(a)