


def merge(array, left, m, right):
	l = m-left+1
	r = right-m
	leftarray = [0]*(l)
	rightarray = [0]*(r)
	for i in range(l):
		leftarray[i]= array[left+i]
	for j in range(r):
		rightarray[j]=array[m+1+j]

	i,j, k = 0, 0, left
	while i< l and j<r:
		if leftarray[i]<= rightarray[j]:
			array[k] = leftarray[i]
			i+=1
		else:
			array[k]= rightarray[j]
			j+=1
		k += 1

	while i < l:
		array[k] = leftarray[i]
		i+=1
		k+=1
	while j<r:
		array[k]= rightarray[j]
		j+=1
		k += 1

def mergesort(array, left, right):
	if left < right:
		m = (left+right-1)/2
		mergesort(array, left, m)
		mergesort(array, m+1, right)
		merge(array, left, m, right)
 	
array = [1,5,2,3,1,8]
mergesort(array,0,len(array)-1)
print array

def partition(array,low,right):
	pivot = array[right]
	i = low-1
	for j in range(low,right):
		if array[j]<= pivot:
			i+=1
			array[i],array[j]= array[j], array[i]
	array[i+1], array[right]= array[right],array[i+1]
	return i+1

def quicksort(array,low,high):
	if low<high:
		pi = partition(array,low,high)
		quicksort(array, low, pi-1)
		quicksort(array, pi+1, high)



array = [5,3,1,5,2,8]
quicksort(array,0,len(array)-1)
print array