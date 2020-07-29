#The file, poker.txt, contains one-thousand random hands dealt to two players. 
#Each line of the file contains ten cards (separated by a single space): 
#the first five are Player 1's cards and the last five are Player 2's cards. 
#You can assume that all hands are valid (no invalid characters or repeated cards), 
#each player's hand is in no specific order, and in each hand there is a clear winner.

#How many hands does Player 1 win?

player1 = []
player2 = []
f = open("p054_poker.txt")

CARDVALUES = {
	"2": 2,
	"3": 3,
	"4": 4,
	"5": 5,
	"6": 6,
	"7": 7,
	"8": 8,
	"9": 9,
	"T": 10,
	"J": 11,
	"Q": 12,
	"K": 13,
	"A": 14
}

CARDNAMES = {
	2: "2",
	3: "3",
	4: "4",
	5: "5",
	6: "6",
	7: "7",
	8: "8",
	9: "9",
	10: "10",
	11: "Jack",
	12: "Queen",
	13: "King",
	14: "Ace"
}

CARDSUITS = {
	"D": "Diamonds",
	"H": "Hearts",
	"C": "Clubs",
	"S": "Spades"
}

def parameterizeHands (combinedHands, handList1, handList2) :
#	tenCards = combinedHands.readline().strip()
	for x in range(1, 11) :
		if x < 6 :
			handList1.append([CARDVALUES[combinedHands.read(1)], combinedHands.read(1)])
			garbage = combinedHands.read(1)
		else :
			handList2.append([CARDVALUES[combinedHands.read(1)], combinedHands.read(1)])
			garbage = combinedHands.read(1)

def printHand (playerHand) :
	for c in playerHand :
		print(CARDNAMES[c[0]] + " of " + CARDSUITS[c[1]])

def lowCard (playerHand) :
	lowIndex = 14
	for x in range(0, len(playerHand)) :
		if (playerHand[x][0] < lowIndex) :
			lowIndex = playerHand[x][0]
	return lowIndex

def reOrderHand (playerHand) :
	tempHand = []
	for iterations in range(0, 5) :
		highIndex =[0, "S"]
		for x in playerHand :
			if (x[0] > highIndex[0]) :
				highIndex = x
		tempHand.append(highIndex)
		playerHand.remove(highIndex)
	for x in tempHand :
		playerHand.insert(0, x)

#1
def highCard (playerHand) :
	highIndex = 0
	for x in range(0, len(playerHand)) :
		if (playerHand[x][0] > highIndex) :
			highIndex = playerHand[x][0]
	return highIndex

def nextHighest (playerHand, prevHigh) :
	if prevHigh == lowCard(playerHand) :
		return prevHigh
	highIndex = 0
	for x in range(0, len(playerHand)) :
		if (playerHand[x][0] > highIndex and playerHand[x][0] < prevHigh) :
			highIndex = playerHand[x][0]
	return highIndex

def highestWithout (playerHand, cardToRemove) :
	modifiedHand = []
	for x in range(0, 5) :
		if (playerHand[x][0] != cardToRemove) :
			modifiedHand.append(playerHand[x])
	return highCard(modifiedHand)


#2
def containsOnePair (playerHand) :
	for x in range(0, 4) :
		if playerHand[x][0] == playerHand[x + 1][0] :
			return playerHand[x][0]
	return 0

def pairTie (player1, player2, pairValue) :
	modifiedHand1 = []
	modifiedHand2 = []
	for x in range(0, 5) :
		if (player1[x][0] != pairValue) :
			modifiedHand1.append(player1[x])
		if (player2[x][0] != pairValue) :
			modifiedHand2.append(player2[x])
	high1 = highCard(modifiedHand1)
	high2 = highCard(modifiedHand2)
	while (high1 == high2) :
		high1 = nextHighest(modifiedHand1, high1)
		high2 = nextHighest(modifiedHand2, high2)
	if high1 > high2 :
		return 1
	else :
		return 2

#3
def containsTwoPairs (playerHand) :
	firstPairFound = False
	returnable = [0, 0]
	foundConsecutive = []
	for x in range(0, 4) :
		if playerHand[x][0] == playerHand[x + 1][0] :
			foundConsecutive.append(playerHand[x][0])
	returnable = list(dict.fromkeys(foundConsecutive))
	if len(returnable) == 0 :
		returnable.append(0)
		returnable.append(0)
	elif len(returnable) == 1 :
		returnable.append(0)
	return returnable


def strayCard (playerHand) :
	pairCards = containsTwoPairs(playerHand)
	for x in playerHand :
		if x[0] != pairCards[0] and x[0] != pairCards[1] :
			return x[0]
	return 0

#4
def containsThree (playerHand) :
	for x in range(0, 3) :
		if (playerHand[x][0] == playerHand[x + 1][0] 
		and playerHand[x + 1][0] == playerHand[x + 2][0]) :
			return playerHand[x][0]
	return 0

#5
def containsStraight (playerHand) :
	if (playerHand[0][0] + 4 == playerHand[1][0] + 3 
		and playerHand[1][0] + 3 == playerHand[2][0] + 2 
		and playerHand[2][0] + 2 == playerHand[3][0] + 1
		and playerHand[3][0] + 1 == playerHand[4][0]) :
		return 1
	return 0

#6
def containsFlush (playerHand) :
	suit = playerHand[0][1]
	for x in playerHand :
		if (x[1] != suit) :
			return 0
	return 1

#7
def containsFullHouse (playerHand) :
	pairValue = containsOnePair(playerHand)
	threeValue = containsThree(playerHand)
	if (pairValue != threeValue 
		and pairValue > 0
		and threeValue > 0) :
		return [pairValue, threeValue]
	return [0, 0]

#8
def containsFour (playerHand) :
	for x in range(0, 2) :
		if (playerHand[x][0] == playerHand[x + 1][0] 
		and playerHand[x + 1][0] == playerHand[x + 2][0]
		and playerHand[x + 2][0] == playerHand[x + 3][0]) :
			return playerHand[x][0]
	return 0	

#9
def containsStraightFlush (playerHand) :
	if containsStraight(playerHand) == 1 and containsFlush(playerHand) == 1 :
		return 1
	return 0

#10
def containsRoyalFlush (playerHand) :
	if containsStraightFlush(playerHand) and playerHand[0][0] == 11 :
		return 1
	return 0

def handPower (playerHand) :
	handPower = 1
	if containsOnePair(playerHand) != 0 :
		handPower = 2
	if (containsTwoPairs(playerHand)).count(0) == 0 :
		handPower = 3
	if containsThree(playerHand) != 0 :
		handPower = 4
	if containsStraight(playerHand) == 1 :
		handPower = 5
	if containsFlush(playerHand) == 1:
		handPower = 6
	if containsFullHouse(playerHand) != [0, 0] :
		handPower = 7
	if containsFour(playerHand) != 0 :
		handPower = 8
	if containsStraightFlush(playerHand) == 1 :
		handPower = 9
	if containsRoyalFlush(playerHand) == 1 :
		handPower = 10
	return handPower

player1Score = 0
player2Score = 0
for x in range(0, 1000) :
	player1.clear()
	player2.clear()
	parameterizeHands(f, player1, player2)
	reOrderHand(player1)
	reOrderHand(player2)
	printHand(player1)
	printHand(player2)
	power1 = handPower(player1)
	print("Player 1 power:" + str(power1))
	power2 = handPower(player2)
	print("Player 2 power:" + str(power2) + "\n")
	if (power1 > power2) :
		player1Score += 1
		#continue
	elif (power2 > power1) :
		player2Score += 1
		#continue
	else :
		if power1 == 1 :
			if highCard(player1) > highCard(player2) :
				player1Score += 1
			elif highCard(player2) > highCard(player1) :
				player2Score += 1
			else :
				nextHigh1 = nextHighest(player1, highCard(player1))
				nextHigh2 = nextHighest(player2, highCard(player2))
				while (nextHigh1 == nextHigh2) :
					nextHigh1 = nextHighest(player1, nextHigh1)
					nextHigh2 = nextHighest(player2, nextHigh2)
				if nextHigh1 > nextHigh2 :
					player1Score += 1
					#continue
				else :
					player2Score += 1
					#continue
		elif power1 == 2 :
			if containsOnePair(player1) > containsOnePair(player2) :
				player1Score += 1
				#continue
			elif containsOnePair(player2) > containsOnePair(player1) :
				player2Score += 1
				#continue
			else :
				if pairTie(player1, player2, containsOnePair(player1)) == 1 :
					player1Score += 1
				else :
					player2Score += 1
		elif power1 == 3 :
			if strayCard(player1) > strayCard(player2) :
				player1Score += 1
				#continue
			else :
				player2Score += 1
				#continue
		elif power1 == 4 :
			if containsThree(player1) > containsThree(player2) :
				player1Score += 1
				#continue
			elif containsThree(player2) > containsThree(player1) :
				player2Score += 1
				#continue
			else :
				if pairTie(player1, player2, containsThree(player1)) == 1 :
					player1Score += 1
				else :
					player2Score += 1
		elif power1 == 5 or power1 == 6 or power1 == 9 :
			if (lowCard(player1) > lowCard(player2)) :
				player1Score += 1
				#continue
			else :
				player2Score += 1
				#continue
		elif power1 == 7 :
			if containsThree(player1) > containsThree(player2) :
				player1Score += 1
				#continue
			elif containsThree(player2) > containsThree(player1) :
				player2Score += 1
				#continue
		elif power1 == 8 :
			if containsFour(player1) > containsFour(player2) :
				player1Score += 1
				#continue
			else :
				player2Score += 1
				#continue

print("Player 1 Score: " + str(player1Score))
print("Player 2 Score: " + str(player2Score))