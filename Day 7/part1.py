import sys
from collections import Counter

cards_mapping = {'A': 14,'K': 13,'Q': 12,'J': 11,'T': 10,'9' : 9,'8' : 8,'7' : 7, '6' : 6,'5' : 5,'4' : 4,'3' : 3,'2' : 2}
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
    #print(f"Hand cards: {hand.cards}, with {hand.cards_num} and {sorted(counts.values())}")
    if sorted(counts.values()) == [5]: #5 of a kind
        return (7,hand.cards_num) #Best combination, 
    elif sorted(counts.values()) == [1,4]: #4 of a kind
        return (6,hand.cards_num)
    elif sorted(counts.values()) == [2,3]: #Full house
        return (5,hand.cards_num)
    elif sorted(counts.values()) == [1,1,3]: #Three of a kind
        return (4,hand.cards_num)
    elif sorted(counts.values()) == [1,2,2]: #Two pairs of a kind:
        return (3,hand.cards_num)
    elif sorted(counts.values()) == [1,1,1,2]: #One pair
        return (2,hand.cards_num)
    elif sorted(counts.values()) == [1,1,1,1,1]:
        return (1,hand.cards_num)
    else:
        print("ERR")
        return None

hands_sorted = sorted(hands_unsorted, key=sort)
sum = 0
for i in range(max_rank):
    sum += (i+1) * int(hands_sorted[i].bid)
print(sum)