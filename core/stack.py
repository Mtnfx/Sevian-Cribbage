from .card import Card

class Stack():
    cards: list[Card]
    
    def __init__(self, cards: list[Card]):
        self.cards = cards
    
    def __pos__(self) -> int:
        """
        Calculate total value of stack.

        Returns:
            int: Sum of values of all cards in stack.
        """
        sum = 0
        for card in self.cards:
            sum += card.value
            
        return sum
    
    def __invert__(self):
        """
        Calculate flush points in stack.
        
        A cribbage flush is worth one point per card for a minimum of four cards. For stacks, all flush cards must be at the top of the stack.
        
        Returns:
            int: Maximum number n such that the top n cards in the stack are the same suit if n >= 4. Else 0.
        """
        #Since we use append to add cards to the stack, the top of the stack is the end of the self.cards list.
        index = -1
        #Keep moving one card backward in stack until we find pair of cards that do not the same suit or reach the end of the stack.
        while(index > -len(self.cards) and (self.cards[index] & self.cards[index-1])):
            index -= 1
        
        #If the number of same-suit cards at the top of stack is < 4, no flush is counted. 
        if(index > -4):
            return 0
        
        return(-index)
    
    def pairs(self) -> int:
        """
        Calculate pair points on top of stack.

        Returns:
            int: Number of points scored by pairs.
        """
        points = 0
        #Loop through all but top card in stack until we hit a card without the same rank as the top card.
        for i in range(2, len(self.cards)+1):
            #If the current card we're looking at is the same rank as the top, it forms a pair for each card above it in the stack (i-1)
            if self.cards[-i].rank == self.cards[-1].rank:
                points += 2*(i-1)
            #If the current card is a different rank, we've reached the end of the pairs.
            else:
                return points
        #If we make it to this point, all cards on the stack are the same rank.
        return points
        
    def add_card(self, card: Card) -> bool:
        """
        Adds card to stack if allowed by Sevian Cribbage rules.

        Args:
            card (Card): Card to be added to stack.

        Returns:
            bool: True if card was successfully added to stack. False if adding card is illegal move.
        """
        if(+self + card.value > 31):
            #Return False if adding card would exceed the total allowed value of stack (31).
            return False
        
        #If we didn't return False, card can be added to stack.
        self.cards.append(card)
        return True