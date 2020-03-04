#Insertion Sort

def find_min(array):
	temp = 0
	for i in range(0, len(array)):
		if array[i] < array[temp]:
			temp = i
	return temp
	
def weird_sort(array):
	for i in range(0, len(array)):
		index = i + find_min(array[i:])
		temp = array[index]
		for j in range(index, i, -1):
			array[j] = array[j-1]
		array[i] = temp
		
	return array

def ins_sort(array):
	for j in range(0, len(array)):
		temp = array[j]
		for k in range(j, 0, -1):
			if array[k] < array[k-1]:
				array[k] = array[k-1]
				array[k-1] = temp
	return array
			
		
		
array = [5, 6, 1, 2, 2, 1]
#array = [1, 2, 3, 4, 5, 6]

#print(ins_sort(array))

#Part B
'''There is one meeting room in a firm. There are N meetings in the form of (Si, Fi) where Si is the start time of meeting i and Fi is finish time of meeting i. The task is to find the maximum utilization of time of meetings that can be accommodated in the meeting room. Print all meeting numbers'''

si = [9, 10, 11, 9, 8.5, 9.5, 11]
fi = [x + 1 for x in si]

def sche(si, f1):
	
print(fi)





	
