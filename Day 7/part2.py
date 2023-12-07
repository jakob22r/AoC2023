import sys
from collections import Counter

cards_mapping = {'A': 13,'K': 12,'Q': 11,'T': 10,'9' : 9,'8' : 8,'7' : 7, '6' : 6,'5' : 5,'4' : 4,'3' : 3,'2' : 2, 'J': 1}
class hand:
    cards = ''
    bid = 0
    cards_num = 0
    def mapcardstonum(self,cards):
        sum = 0
        for i in range(len(cards)):
            sum =sum*15 + cards_mapping.get(cards[i])
        return sum

    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.cards_num = self.mapcardstonum(self.cards)

input = open(sys.argv[1]).read().strip()
#Create list of tuple to work with
lines = [tuple(line.split()) for line in input.split('\n')]
max_rank = len(lines)
#Create a hand object for encapsulation to make it easier to work with
hands_unsorted = [hand(line[0], line[1]) for line in lines]
#Given a string containing a hand of five cards, appropiately sorts it according to game rules
def sort(hand: hand):
    cards = hand.cards
    counts = Counter(cards)
    j_count = counts.get('J', 0)
    counts.pop('J', None) #Removes j entries
    distinct_values = len(set(counts))
    most_common_cnt = 0
    if j_count < 5:
        most_common_cnt = (counts.most_common()[0])[1]
    #print(f"Hand cards: {hand.cards}, with {hand.cards_num} and {sorted(counts.values())}")
    if most_common_cnt + j_count == 5: #5 of a kind
        print("5 kind")
        return (7,hand.cards_num) #Best combination, 
    elif most_common_cnt + j_count == 4: #4 of a kind
        print("Four kind")
        return (6,hand.cards_num)
    elif distinct_values <= 2: #Full house
        print("Full house")
        return (5,hand.cards_num)
    elif sorted(counts.values()) == [1,1,3] or most_common_cnt + j_count == 3: #Three of a kind
        print("Three of a kind")
        return (4,hand.cards_num)
    elif sorted(counts.values()) == [1,2,2] or (most_common_cnt == 2 and j_count == 1): #Two pairs of a kind:
        print("Two pairs")
        return (3,hand.cards_num)
    elif (counts.most_common()[0])[1] == 2 or j_count == 1: #One pair
        print("One pair")
        return (2,hand.cards_num)
    else:
        print("high card")
        return (1,hand.cards_num)
    
hands_sorted = sorted(hands_unsorted, key=sort)
sum = 0
for i in range(max_rank):
    sum += (i+1) * int(hands_sorted[i].bid)
print(sum)