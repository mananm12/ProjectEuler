#n! means n × (n − 1) × ... × 3 × 2 × 1
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!

total = 0
fact = 1
for x in range(1, 101) :
	fact *= x
while fact > 9 :
	total += fact%10
	fact = int(fact//10)
total += fact
print(total)