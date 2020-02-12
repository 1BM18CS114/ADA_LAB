import time



def bub(arr):
	n = len(arr)
	
	while n != 0:
		i = 0
		while i < n - 1:
			if arr[i] > arr[i+1]:
				temp = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = temp
				#print(arr)
			i += 1
			
		n -= 1
		#print(arr)

leng = randint(0, 10)
arr = []
for i in range(leng):
	val = randint(0, 10000)
	arr.append(val)	
#print(arr)
#bub(arr)
#print(arr)


					
	
