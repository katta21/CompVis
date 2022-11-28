# No Pair – This very common hand contains "nothing." None of the five cards 
# pair up, nor are all five cards of the same suit or consecutive in rank. When more than 
# one player has no pair, the hands are rated by the highest card each hand contains, so 
# that an ace-high hand beats a king-high hand, and so on.

# Will be given an array of 5 cards for cards in the middle. 4 array of 2 cards for hands.
# Cards are denoted by [Card][Suit] 2,3,4,5,6,7,8,9,0,J,Q,K,A and S,C,H,D
card_map = {
"2": 2,
"3": 3,
"4": 4,
"5": 5,
"6": 6,
"7": 7,
"8": 8,
"9": 9,
"0": 10,
"J": 11,
"Q": 12,
"K": 13,
"A": 14
}#Changes card number to int value

def getHighCard(cards):
    high_card = 0
    for card in cards:
        if card_map[card[0]] > high_card:
            high_card = card_map[card[0]] # if current card is higher than last, replace it
    return high_card #return highest card number

# One Pair – This frequent combination contains just one pair with the other 
# three cards being of different rank. An example is 10, 10, K, 4, 3.
def isPair(cards):
    res = False
    card_num = 0
    temp = []
    for card in cards:
        temp.append(card_map[card[0]]) #puts value of cards into a temp array
    temp.sort() #sorts array
    for i in range (len(temp) - 1):
        if temp[i] == temp[i + 1]: # looks to see if similar values are next to each other
            return [True, temp[i]] # returns true and the number value
    return [res, card_num]

# Two Pairs – This hand contains a pair of one rank and another pair of a 
# different rank, plus any fifth card of a different rank, such as Q, Q, 7, 7, 4.
def isTwoPairs(cards):
    res = False
    card_num = 0
    temp = []
    compare = isPair(cards)[1] # Compare is the value given from the pair
    if isPair(cards)[0]: #If one pair is present we will take that pair out and run is pair on the
        # remaining cards     
        for card in cards:
            if card_map[card[0]] != compare:
                temp.append(card) #Add the cards that were not in the pair to temp
        if isPair(temp)[0]: #Check to see if the remainder cards have a pair as well
            pairs = [compare, isPair(temp)[1]]
            return [True, max(pairs)]#returns ture and number of higher pair
    return [res, card_num]

# Three of a Kind – This combination contains three cards of the same rank, 
# and the other two cards each of a different rank, such as three jacks, a seven, and a four.
def isThreeOfAKind(cards):
    res = False
    card_num = 0
    temp = []
    for card in cards:
        temp.append(card_map[card[0]]) #puts value of cards into a temp array
    temp.sort() #sorts array
    for i in range (len(temp) - 2):
        if temp[i] == temp[i + 1] == temp[i + 2]: # looks to see if similar values are next to each other
            return [True, temp[i]] # returns true and the number value
    return [res, card_num]

# Straight – Five cards in sequence, but not all of the same suit is a straight. 
# An example is 9♥, 8♣, 7♠, 6♦, 5♥.
def isStraight(cards):
    res = False
    card_num = 0
    temp = []
    for card in cards:
        if card_map[card[0]] not in temp:
            temp.append(card_map[card[0]]) #puts value of cards into a temp array
    temp.sort() #sorts array
    for i in range (len(temp) - 4):
        if temp[i] + 4 == temp[i + 1] + 3 == temp[i + 2] + 2 == temp[i + 3] + 1 == temp[i + 4]: # looks to see if 
            # values next to each other are in ascending order
            return [True, temp[i + 4]] # returns true and the number value
    return [res, card_num]

# Flush – Five cards, all of the same suit, but not all in sequence, is a flush. 
# An example is Q, 10, 7, 6, and 2 of clubs.
def isFlush(cards):
    res = False
    card_num = 0
    suit = [0,0,0,0]
    for card in cards:
        if card[1] == "C":
            suit[0] += 1
            if suit[0] == 5:
                return[True, card_map[card[0]]]
        elif card[1] == "D":
            suit[1] += 1
            if suit[1] == 5:
                return[True, card_map[card[0]]]
        elif card[1] == "H":
            suit[2] += 1
            if suit[2] == 5:
                return[True, card_map[card[0]]]
        elif card[1] == "S":
            suit[3] += 1
            if suit[3] == 5:
                return[True, card_map[card[0]]]
    return [res, card_num]

# Full House – This colorful hand is made up of three cards of one rank and two cards 
# of another rank, such as three 8s and two 4s, or three aces and two 6s.
def isFullHouse(cards):
    res = False
    card_num = 0
    temp = []
    compare = isThreeOfAKind(cards)[1] # Compare is the value given from three of a kind
    if isThreeOfAKind(cards)[0]: #If one group of 3 is present we will take it out and run is pair
        # on the remaining cards     
        for card in cards:
            if card_map[card[0]] != compare:
                temp.append(card) #Add the cards that were not in the group of 3 to temp
        if isPair(temp)[0]: #Check to see if the remainder cards has a pair
            pairs = [compare, isPair(temp)[1]]
            return [True, max(pairs)]#returns ture and number of higher grouping
    return [res, card_num]

# Four of a Kind – This is the next highest hand, and it ranks just below a straight flush. 
# An example is four aces or four 3s. It does not matter what the fifth, unmatched card is.
def isFourOfAKind(cards):
    res = False
    card_num = 0
    counts = {}
    for card in cards:
        counts[card[0]] = counts.get(card[0], 0) + 1 #adds to dict the count of each rank
        if counts.get(card[0]) == 4:
            return [True, card_map[card[0]]] #if 4 are present, returns True and card number
    return [res, card_num]

# Straight Flush – This is the highest possible hand when only the standard pack is used, 
# and there are no wild cards. A straight flush consists of five cards of the same suit in sequence, 
# such as 10, 9, 8, 7, 6 of hearts. The highest-ranking straight flush is the A, K, Q, J, and 10 of 
# one suit, and this combination has a special name: a royal flush or a royal straight flush. 
# The odds on being dealt this hand are 1 in almost 650,000.
def isStraightFlush(cards):
    if isStraight(cards)[0] and isFlush(cards)[0]:
        if isStraight(cards)[1] == isFlush(cards)[1]:
            return [True, isStraight(cards)[1]]
    return [False, 0]
        
def getTier(cards):
    if isStraightFlush(cards)[0]:
        return [8,isStraightFlush(cards)[1]]
    elif isFourOfAKind(cards)[0]:
        return [7,isFourOfAKind(cards)[1]]
    elif isFullHouse(cards)[0]:
        return [6,isFullHouse(cards)[1]]
    elif isFlush(cards)[0]:
        return [5,isFlush(cards)[1]]
    elif isStraight(cards)[0]:
        return [4,isStraight(cards)[1]]
    elif isThreeOfAKind(cards)[0]:
        return [3,isThreeOfAKind(cards)[1]]
    elif isTwoPairs(cards)[0]:
        return [2,isTwoPairs(cards)[1]]
    elif isPair(cards)[0]:
        return [1,isPair(cards)[1]]
    return [0,getHighCard(cards)]

def evaluateHands(cards, hands):
    players = []
    highest_tier = 0
    for hand in hands:
        players.append(hand + cards) # Creates total of hand and card
    for player in players:
        tier = getTier(player)[0]
        player.append(getTier(player)[0]) # Adds 'tier level' to the end of the players' cards
        if tier > highest_tier:
            highest_tier = tier #Finds highest tier present

    winning_hands = []
    #Finds all hand (if multiple present) that are the same tier
    for i in range(len(players)): 
        if players[i][-1] == highest_tier:
            winning_hands.append(i)

    #If there is only one winning hand, that will be returned
    if len(winning_hands) == 1:
        print(hands[winning_hands[0]])
        return hands[winning_hands[0]]

    #If there are multiple winning hands I will determine the highest rank of them all
    else:
        winning_hand = hands[winning_hands[0]]
        c = cards + hands[0]
        winning_comp = getTier(c)[1]
        for h in winning_hands:
            c = cards + hands[h]
            print(getTier(c)[1])
            if getTier(c)[1] > winning_comp:
                winning_hand = hands[h]
                winning_comp = getTier(c)[1]
        print (winning_hand)
        return winning_hand


c = ["3S", "AS", "7S", "QD", "QS"]
h1 = ["4S", "8H"]
h2 = ["3H", "KS"]
h3 = ["2S", "0H"]
h4 = ["AD", "2C"]
h5 = ["5C", "6C"]
h = []
h.append(h1)
h.append(h2)
h.append(h3)
h.append(h4)
h.append(h5)
evaluateHands(c, h)