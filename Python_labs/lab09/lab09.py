#card game war-simple version
import cards

def play_war(h1, h2):
    #while any one has more than one card on hand:
    while True:
        h1,h2 = play_one(h1,h2)
        print("hand1:",h1)
        print("hand2:",h2)
        if len(h2)==0:
            print("Player 1 Wins")
            break
        elif len(h1)==0:
            print("Player 2 Wins")
            break
        if input("Keep Going: (Q or q) to stop:") == 'q':
            print("Concede")
            break # break the loop manually
    
def play_one(h1, h2):
    #get the top card from h1: top1
    topcard1 = h1.pop( 0 )
    #get the top card from h2: top2
    topcard2 = h2.pop( 0 )

    #get the rank of top1, if it is 1 (Ace), change to 13:  val1
    val1=topcard1.get_rank()
    if val1==1:
        val1=14
    #get the rank of top2, if it is 1 (Ace), change to 13:  val2
    val2=topcard2.get_rank()
    if val2==1:
        val2=14
    
    if val1 > val2:
        # h1 gets both cards
        h1.append(topcard1)
        h1.append(topcard2)
    elif val2 > val1:
        # h2 gets both cards
        h2.append(topcard2)
        h2.append(topcard1)
    else:
        #h1, h2 get their cards back
        h1.append(topcard1)
        h2.append(topcard2)
    return h1,h2

def main():
    # Create a deck of cards
    the_deck = cards.Deck()

    # Shuffle the deck
    the_deck.shuffle()

    # Create two player lists: hand1, hand2
    hand1=[]
    hand2=[]

    #while the deck is not empty:
        #deal card to the two players
    while not the_deck.is_empty():
        for i in range(26):
            hand1.append( the_deck.deal() )
            hand2.append( the_deck.deal() )
    
    # make a short deck, only use the first 5 cards to play
    #hand1 = hand1[:5]
    #hand2 = hand2[:5]
    play_war(hand1, hand2)

if __name__ == "__main__":
    main()


