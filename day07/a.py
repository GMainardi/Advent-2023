from collections import Counter

class PokerHand:

    CARDS = {'A': 14, 'K': 13, 
            'Q': 12, 'J': 11, 
            'T': 10, '9': 9, 
            '8': 8, '7': 7, 
            '6': 6, '5': 5, 
            '4': 4, '3': 3, 
            '2': 2}
    
    def __init__(self, hand, bid) -> None:
        self.hand = hand
        self.bid = int(bid)

    def eval_hand(self):
        freqs = Counter(self.hand)

        best = max(freqs.values())
        if best == 5:
            return 7
        if best == 4:
            return 6
        if best == 3:
            if 2 in freqs.values():
                return 5
            return 4
        if best == 2:
            if list(freqs.values()).count(2) == 2:
                return 3
            return 2
        return 1
    
    def __tiebreaker(self, other):
        for m, o in zip(self.hand, other.hand):
            if PokerHand.CARDS[m] > PokerHand.CARDS[o]:
                return True
            if PokerHand.CARDS[m] < PokerHand.CARDS[o]:
                return False
        return False

    def __gt__(self, other):
        if self.eval_hand() > other.eval_hand():
            return True
        if self.eval_hand() < other.eval_hand():
            return False
        return self.__tiebreaker(other)
    
    def __repr__(self) -> str:
        
        return f"{self.hand} {self.bid}"


with open("input.txt", "r") as f:
    lines = f.readlines()

hands = []
for line in lines:
    ph = PokerHand(*line.strip().split())
    hands.append(ph)

total_winnings = 0
for idx, hand in enumerate(sorted(hands)):
    total_winnings += hand.bid * (idx + 1)


print(total_winnings)