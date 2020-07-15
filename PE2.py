total = 2
term1 = 1
term2 = 2
while term2 < 4000000 :
	temp = term1 + term2
	term1 = term2
	term2 = temp
	if temp%2 == 0 :
		total += temp
print(total)