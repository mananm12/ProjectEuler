#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?

import math

def isPrime (num) :
	for y in range(2, int(math.sqrt(num)) + 1) :
		if num%y == 0 :
			return False
	return True

def digitCount (num) :
	digits = 1
	while num > 9 :
		digits += 1
		num = num // 10
	return digits

def isCircularPrime (num) :
	digits = digitCount(num)
	lastDigPlace = math.pow(10, digits - 1)
	for x in range(1, digits) :
		firstDig = num%10
		num = int(((num // 10) + (firstDig * lastDigPlace)))
		if isPrime(num) :
			pass
		else :
			return False
	return True

numCircularPrimes = 0
for x in range(2, 1000000) :
	if (isPrime(x) and isCircularPrime(x)) :
		numCircularPrimes += 1

print(numCircularPrimes)