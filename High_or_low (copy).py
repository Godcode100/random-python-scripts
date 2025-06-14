#usr/bin/python3
#OOP combines code and data into one cohesive unit thereby avoiding the problems inherent in procedural programming.
#The program represents a deck of 52 cards which i will represent as a list.
#Each of the cards will be represented as a dictionary containing 3 key/value pairs such as {'rank':'Jack','suit':'clubs','value':11}
#The rank is the name of the card such as (Ace,King,Queen,2,3,....10) value is the integer used for comparing the cards
#Before playing the game the list representing the deck is created and shuffled.

import random
#Card constants
SUIT_TUPLE = ('Spades','Hearts','Club','Diamonds')
RANK_TUPLE =('2','3','4','5','6','7','8','9','10','Ace','Jack','King','Queen')

NCARDS =8
#Pass this function in a deck and it returns a random card from the deck
def main():
	def getcard(DeckListIn):
		thiscard = DeckListIn.pop()#pop one off from the top and return it.
		return thiscard

	#Pass in a deck and this returns a shuffled copy of the deck
	def shuffle(DeckListIn):
		DeckListOut = DeckListIn.copy()
		random.shuffle(DeckListOut)
		return DeckListOut

	print('Welcome to the Lower or Higher Game')
	print()

	startingDeckList =[]
	for suit in SUIT_TUPLE:
		for thisvalue,rank in enumerate(RANK_TUPLE):
		cardDict = {'rank':rank,'suit':suit,'value': thisvalue+1}
		startingDeckList.append(cardDict)

	score =50
	#print(startingDeckList)
	while True:
		gameDeckList = shuffle(startingDeckList)
		CurrentCard = getcard(gameDeckList)
		CurrentCardrank = CurrentCard['rank']
		CurrentCardsuit =CurrentCard['suit']
		CurrentCardvalue = CurrentCard['value']
		print (gameDeckList[1])
		print (gameDeckList[2])
		print (gameDeckList[3])
		print (gameDeckList[1])

		#for gameDeckList in range(8) :
		#    print(gameDeckList)
		print("Starting card rank is ", CurrentCardrank + ' of ' + CurrentCardsuit)

		for Number_of_cards in range(0,NCARDS):
		answer = input('Will th next card be higher or lower than the ' + CurrentCardrank + ' of ' + CurrentCardsuit +'? (enter h or l):')
		answer = answer.casefold()
		nextCard = getcard(gameDeckList)
		nextCardrank = nextCard['rank']
		nextCardsuit = nextCard['suit']
		nextCardvalue = nextCard['value']
		print("Next Card is "+ nextCardrank + ' of '+ nextCardsuit)

		if answer == 'h':
			if nextCardvalue > CurrentCardvalue:
			    print('You got it right')
			    score += 20
			else:
			    print('You got it wrong')
			    score -=15
		#print('Your score is: ',score)

		if answer == 'l':
			if nextCardvalue < CurrentCardvalue:
			    print('You are right')
			    score+=20

			else:
			    print('Incorrect')
			    score -=15
		print("Your score is ",score)

		CurrentCardrank = nextCardrank
		CurrentCardvalue = nextCardvalue
		goAgain = input ('To play again press Enter or q to quit:')
		if goAgain =='q':
		break
if __name__=="__main__":
	main()
