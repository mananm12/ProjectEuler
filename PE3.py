#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

initial = 600851475143
for x in range(2, 600851475143) :
	if initial%x == 0 and initial == x :
		break
	elif initial%x == 0 :
		while (initial%x == 0) :
			initial = initial/x
	else :
		pass
print(initial)