import time
from random import randint
#Input Array
leng = 1000
print(leng)
arr = []
for i in range(leng):
	val = randint(1, 10000)
	arr.append(val)
#arr = [12, 7, 1, 5, 4, 6]

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
		#print(arr)
	return arr
	
start = time.time()
sel_sort(arr)
end = time.time()
print(end - start)

#K largest Values
def k_larg(array, k):
	arr = sel_sort(array)
	return arr[-k:]

def k_larg2(arr, k):
	for i in range(len(arr) - k):
		temp = i
		for j in range(i, len(arr)):
			if arr[temp] > arr[j]:
				temp = j
				#print(temp)
		a = arr[i]
		arr[i] = arr[temp]
		arr[temp] = a
		#print(arr)
		
	return arr[-k:]

start = time.time()
k_larg2(arr, 3)
end = time.time()
print(end - start)
	
		
		
		
