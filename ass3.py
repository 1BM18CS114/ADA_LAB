#Input Array
arr = [12, 7, 1, 5, 4, 6]

#Selection Sort 
def sel_sort(arr):
	for i in range(len(arr) - 1):
		temp = i
		for j in range(i, len(arr)):
			if arr[temp] > arr[j]:
				temp = j
				#print(temp)
		a = arr[i]
		arr[i] = arr[temp]
		arr[temp] = a
		print(arr)
	return arr
	

print(sel_sort(arr))

#K largest Values
def k_larg(array, k):
	arr = sel_sort(array)
	return arr[-k:]

print(k_larg(arr, 3))
	
		
		
