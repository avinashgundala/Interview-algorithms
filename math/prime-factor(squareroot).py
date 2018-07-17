import math 
#with this function we will find prime_factor
def prime_factor(n): 
	#finding number  of 2 that divide n
	while n % 2==0: 
		print(2)
		n= n/2
	#why square root of n?
	#for ex: 323  sqare root is 17.97
	#323 = 17*19 let it be c=a*b
    #b is divisible by a's factor unless it is prime number
	for i in range(3,math.sqrt(n)+1,2):   
	    while n % i ==0:  
	    	print(i)
	    	n =n/i
    if n > 2:
    	print(n)

print('factors of this number',n)  
prime_factor(646)  	
#time complexiy O(sqrt(n))
