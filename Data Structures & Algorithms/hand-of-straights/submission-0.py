class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import Counter
        hand.sort()
        cards = Counter(hand)

        if len(hand)<groupSize:
            return False
        if len(hand)%groupSize!=0:
            return False
        start = 0
        while sum(cards.values()):
            for key in cards:
                if cards[key]>0:
                    start = key
                    break
            for i in range(groupSize):
                if start+i in cards and cards[start+i]>0:
                    cards[start+i]-=1
                else:
                    return False
        return True
        
