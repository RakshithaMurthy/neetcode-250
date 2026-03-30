class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        freq = {}
        for card in hand:
            freq[card] = freq.get(card, 0) + 1  # build frequency dictionary

        for card in sorted(freq):
            count = freq[card]
            if count > 0:  # only try to form groups if this card exists
                for i in range(groupSize):
                    next_card = card + i
                    if freq.get(next_card, 0) < count:
                        return False
                    freq[next_card] -= count
        return True

        