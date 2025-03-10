class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()

        n = len(deck)
        order = [0] * n
        queue = deque(range(n))

        for card in deck:
            ind = queue.popleft()
            order[ind] = card

            if queue:
                queue.append(queue.popleft())
        
        return order
        
