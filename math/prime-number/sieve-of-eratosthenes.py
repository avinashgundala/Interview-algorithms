def sieve_of_ertosthenese(n): 
	#create boolean array prime[0,...n] initialize
	#finally we will leave with true and false array
	#true value array are prime
	prime = [true for i in range(n+1)]
	p = 2 
	#why p*p ?
	#example when n is 198,
	#nearest squared number to it is 14,14*14=196
	#13 is prime number where it's square is 169
	#169 is only number that divisiable by 13 
	#hence 169 is not prime,
	#it is not divisible by number that is less than 13
	while p*p <= n: 
		#if prim[p] is not changed it is prime
		if prime[p]==true:
			for i in range(p*2,n+1,p):
				prime[i] = false
	    p += 1
	# print all true one,which is prime    
	for i in range(2,n+1): 
		if prime[i]: 
			print(i)

if __name__== '__main__' : 
	n = 198
	print('these are the prime number below',n)
	sieve_of_ertosthenese(n)
