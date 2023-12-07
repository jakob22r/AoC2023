import sys
from collections import Counter

cards_mapping = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9' : 9,
    '8' : 8,
    '7' : 7,
    '6' : 6,
    '5' : 5,
    '4' : 4,
    '3' : 3,
    '2' : 2
}
class hand:
    cards = ''
    bid = 0
    cards_num = 0
    
    def mapcardstonum(self,cards):
        sum = 0
        for i in range(len(cards)):
            sum =sum*10 + cards_mapping.get(cards[i])
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
    unique = set(cards)
    counts = Counter(cards)

    print(f"Hand cards: {hand.cards}, with {hand.cards_num}")

    if len(unique) == 1: #5 of a kind
        return (7,hand.cards_num) #Best combination, 
    elif any(count >= 4 for count in counts.values()): #4 of a kind
        return (6,hand.cards_num)
    elif sorted(counts.values()) == [2,3]: #Full house
        return (5,hand.cards_num)
    elif any(count >= 3 for count in counts.values()): #Three of a kind
        print("Three")
        return (4,hand.cards_num)
    elif sum(count == 2 for count in counts.values()) == 2: #Two pairs of a kind:
        print("Case two pairs")
        return (3,hand.cards_num)
    elif sorted(counts.values()) == [2,1,1,1]: #One pair
        return (1,hand.cards_num)
    else: #High card
        return (0,hand.cards_num)

hands_sorted = sorted(hands_unsorted, key=sort)

for h in hands_sorted:
    print(f"Cards {h.cards}, num: {h.cards_num} with bid {h.bid}, unique: {set((h.cards))}")

sum = 0
for i in range(max_rank):
    sum += (i+1) * int(hands_sorted[i].bid)
print(sum)