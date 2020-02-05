##Tower of hanoi
def toh(a, c, b, n):
	if n == 1:
		print("Move Block from {} to {}".format(a,b))
		
	else:
		toh(a, b, c, n - 1)
		toh(a, c, b, 1)
		toh(b, c, a, n - 1)
	

#toh("a", "b", "c", 3)

##GCD using recursion

def gcd(m, n):
	if m == n:
		print(m)
		return
	
	if m > n:
		gcd(m - n, n)
	else:
		gcd(m, n - m)
	
#gcd(10, 2)

##Binary search
a = [1, 2, 3, 3, 3, 4, 5, 6]
length = 8
def search(key, a):
	start1 = 0
	end1 = length - 1
	
	
	#while flag1 == 0 or flag2 == 0:
		#if flag1 == 0:
			#mid1 = (start + end) // 2
			#if a[mid1] == key:
				#if a[mid1] - a[mid1 - 1] != 0:
					#print("First occrance is {}".format(mid1))
					#flag = 1
				#else:
					#end1 = mid1 - 1
			#elif a[mid1] > key:
				#end1 = mid1 - 1
			#else:
				#start1 = mid1 + 1
			
	while start1 < end1:
		mid1 = (start1 + end1) // 2
		if a[mid1] == key:
			pos = mid1
			
		elif a[mid1] > key:
			end1 = mid1 - 1
			
		elif a[mid1] < key:
			start1 = mid1 + 1
	
	start1 = end1 = pos
	while key - a[start1] == 0 or key - a[end1] 	
				
					
				
	
		

