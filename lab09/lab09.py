#card game war-simple version
import cards

def play_war(h1, h2):
    #while any one has more than one card on hand:
    while ????:
        h1,h2 = play_one(h1,h2)
        print("hand1:",h1)
        print("hand2:",h2)
        # break the loop manually
        if input("Keep Going: (Nn) to stop:").lower() == 'n':
            break
    #if the length of h1 is greater than the length of h2, print player 1 wins
    #if the length of h2 is greater than the length of h1, print player 2 wins
    #if two players have the same number of cards on hand, Tie
    
def play_one(h1, h2):
    #get the top card from h1: top1
    #get the top card from h2: top2

    #get the rank of top1, if it is 1 (Ace), change to 13:  val1
    #get the rank of top2, if it is 1 (Ace), change to 13:  val2
    
    if val1 > val2:
        # h1 gets both cards
    elif val2 > val1:
        # h2 gets both cards
    else:
        #h1, h2 get their cards back
    return h1,h2

def main():
    # Create a deck of cards
    the_deck = cards.Deck()
    the_deck.shuffle()

    # Create two player lists: hand1, hand2

    # Shuffle the deck

    #while the deck is not empty:
        #deal card to the two players
    
    # make a short deck, only use the first 5 cards to play
    hand1 = hand1[:5]
    hand2 = hand2[:5]
    play_war(hand1, hand2)

if __name__ == "__main__":
    main()


#suits ignored in this game
#aces highest ranked cards
#cards distributed (alternatingly), until both players have 26 cards
#The top card of each players deck goes 1v1, then both are added to the bottom of the deck(using .append)
#If both cards have the same rank, the cards just simply go to the bottom of the deck
#Game continues until one player has all 52 cards in his stack(Winning the match)


