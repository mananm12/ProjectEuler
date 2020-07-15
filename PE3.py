#Sieve of Eratosthenes methodology used
initial = 600851475143
primesList = []
composite = False
for x in range(2, 600851475143) :
	for y in primesList :
		if x%y == 0 :
			composite = True
	if composite : continue
	if initial%x == 0 and initial == x :
		break
	elif initial%x == 0 :
		while (initial%x == 0) :
			initial = initial/x
	else :
		pass
print(initial)