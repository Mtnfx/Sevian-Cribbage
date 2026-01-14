import pytest

from core.card import Card
from core.hand import Hand
from core.deck import Deck

@pytest.fixture
def rand_hand():
    return Hand(Deck(13,5).cards[1:5]) #Produce random hand of five cards

@pytest.fixture
def test_hand():
    return Hand([Card(9,2), Card(3,3), Card(0,0), Card(4,0), Card(3,1)])

@pytest.fixture
def test_card():
    return Card(1,4) #Wild Two

def test_add_size(rand_hand: Hand, test_card: Card):
    #Confirm that += operation on Hand increases size by one.
    initial_size = len(rand_hand.cards)
    rand_hand += test_card
    assert len(rand_hand.cards) == initial_size + 1
    
def test_suit_count(test_hand: Hand):
    assert test_hand % 0 == 2

#Testing pair counting

@pytest.mark.parametrize("p_hand, points", [
    (Hand(Deck(13, 1).cards[0:5]), 0), #Hand with no pairs scores 0 points from pairs
    (Hand([Card(1,4), Card(3,3), Card(1,3), Card(2,1), Card(10,1)]), 2), #Hand with one pair scores 2 points
    (Hand([Card(1,4), Card(2,3), Card(1,3), Card(2,1), Card(10,1)]), 4), #Hand with two pairs scores 4 points
    (Hand([Card(1,4), Card(3,3), Card(1,3), Card(1,1), Card(10,1)]), 6), #Hand with three-of-a-kind scores 6 points
    (Hand([Card(1,4), Card(1,3), Card(1,0), Card(1,1), Card(1,4)]), 20), #Hand with five-of-a-kind scores 20 points
])
   
def test_pairs(p_hand: Hand, points: int):
    assert p_hand.pair_points() == points
     
#Testing fifteen counting
@pytest.mark.parametrize("f_hand, points", [
    (Hand(Deck(2, 5).cards[0:5]), 0), #Five cards from this deck can add to at most 10 (only ranks are A and 2). Zero fifteen points expected.
    (Hand([Card(0,4), Card(5,3), Card(10,3), Card(8,1), Card(10,1)]), 2), #Hand of A, 6, J, 9, J has one possible 15; scores 2 points.
    (Hand([Card(5,4), Card(4,3), Card(12,3), Card(2,1), Card(10,1)]), 4), #Hand with 6, 5, K, 3, J has two possible 15 combinations; scores 4 points.
    (Hand([Card(8,4), Card(3,3), Card(8,3), Card(1,1), Card(5,1)]), 8), #Hand with 9, 4, 9, 2, 6 has four possible 15 combinations; scores 8 points.
])

def test_fifteen_points(f_hand: Hand, points: int):
    assert f_hand.fifteen_points() == points