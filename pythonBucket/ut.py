
import os # urandom
import unittest # TestCase
import random # shuffle

cards = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]
sample_deck = cards * 24
key = random.seed(os.urandom(1000))

def shuffle_cards(deck):    
    """
    Shuffle cards with random.shuffle.
    """
    shuffled_cards = deck
    random.shuffle(shuffled_cards)
    return shuffled_cards

def sum_cards(hand):    
    """
    Get the total of all cards in the supplied hand.
    Jacks, Queens and kings all have a value of 10,
    while Aces can have a value of 11 or 1, depending 
    on sum of the hand. 

    """
    total = 0
    for card in hand:
        if isinstance(card,str) and card != "ace":
            total += 10
        elif card == "ace":
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        else:
            total += card
            if total > 21:
                return total
    
    while total > 21 and "ace" in hand:
        hand[hand.index("ace")] = 1
        total -= 10


    return total

def hit_stay():
    inp = input("Hit or Stay(h/s): ").lower()
    return inp

def player_turn(deck, hand):
    print(hand, sum_cards(hand))
    # inp = input("Hit or Stay(h/s): ").lower()
    while sum_cards(hand) < 21 and hit_stay() == 'h':
        hand.append(deck.pop(0))
        print(hand, sum_cards(hand))
        # inp = input("Hit or Stay(h/s): ").lower()
        
    

def dealer_turn(deck, hand):
    while sum_cards(hand) <= 16:
        hand.append(deck.pop(0))
        
        print("=" * 90)
        print(f"Dealer hand : {hand}")
        print("=" * 90)
    

def deal(deck):
    player_hand = [] 
    dealer_hand = [] 
    for _ in range(2):
        player_hand.append(deck.pop(0))
        dealer_hand.append(deck.pop(0))
    return player_hand, dealer_hand

def check_natural(player_score, dealer_score):
    if player_score == 21 and dealer_score != 21:
        return "Player Natural Blackjack 1.5x Bet"
    if dealer_score == 21:
        return "Dealer Natural, Player Loses"

def print_hands(player_hand, dealer_hand):
    print("=" * 90)
    print(f"Player hand : {player_hand}")
    print(f"Dealer : {[dealer_hand[0]]}")
    print("=" * 90)

class Test(unittest.TestCase):
    
    def test_cards_are_shuffled(self):
        self.assertNotEqual(cards, shuffle_cards())
    
    def test_ace_conversion(self):
        self.assertEqual(sum_cards(["jack", "jack", "ace"]), 21)
        self.assertEqual(sum_cards([2, 3, "ace"]), 16)
        self.assertEqual(sum_cards([4, 4, "ace"]), 19)

def play_black():
    game_deck = shuffle_cards(sample_deck)
    player_hand, dealer_hand = deal(game_deck)
    print_hands(player_hand, dealer_hand)
    if check_natural(sum_cards(player_hand), sum_cards(dealer_hand)):
        return check_natural(sum_cards(player_hand), sum_cards(dealer_hand)), player_hand, dealer_hand
    else:
        # play the game
        player_turn(game_deck, player_hand)
        if sum_cards(player_hand) == 21:
            return "player blackjack!!", player_hand, dealer_hand
        if sum_cards(player_hand) < 21:
            dealer_turn(game_deck, dealer_hand)
            if sum_cards(dealer_hand) == 21:
                return "Dealer blackjack", player_hand, dealer_hand
            elif sum_cards(dealer_hand) > 21:
                return "Player wins, Dealer went over.", player_hand, dealer_hand
        else:
            return "Player went over, Dealer wins.", player_hand, dealer_hand
        
    player_distance = 21 - sum_cards(player_hand)
    dealer_distance = 21 - sum_cards(dealer_hand)
    # game should be over

    if player_distance == dealer_distance:
        return "Draw"
    return ["Player wins","Dealer wins"][player_distance > dealer_distance], player_hand, dealer_hand

winner, player, dealer = play_black()
print("="*60)
print(winner)
print(f"Player score: {sum_cards(player)} {player}")
print(f"Dealer score: {sum_cards(dealer)} {dealer}")
print("="*60)