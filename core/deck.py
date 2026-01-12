from .card import Card
import random

class Deck:
    cards: list[Card]
    
    def __init__(self, suits: int, ranks:int):
        #Generate random sequence of integers from 0 to number of cards in the deck - 1.
        seq = random.sample([i for i in range(suits*ranks)], k = suits*ranks)
        
        #Build shuffled deck by assigning each integer n in seq to corresponding card such that n = card.suit*ranks + card.rank
        self.cards = [Card(i % ranks, i // ranks) for i in seq]