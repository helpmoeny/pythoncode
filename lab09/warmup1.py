##
## Demonstrate some of the operations of the Deck and Card classes
##

import cards

# Seed the random number generator to a specific value so every execution
# of the program uses the same sequence of random numbers (for testing).

import random
random.seed( 25 )


# Create a deck of cards

my_deck = cards.Deck()


# Display the deck (unformatted)
print( "===== initial deck =====" )
print( my_deck )
print()


# Display the deck in 13 columns

print( "===== initial deck =====" )
my_deck.pretty_print( column_max=13 )


# Shuffle the deck, then display it in 13 columns

my_deck.shuffle()
print( "===== shuffled deck =====" )
my_deck.pretty_print( column_max=13 )


# Deal first card from the deck and display it (and info about the deck)

card1 = my_deck.deal()
print( "First card dealt from the deck:", card1 )
print()
print( "Card suit:", card1.get_suit() )
print( "Card rank:", card1.get_rank() )
print( "Card value:", card1.get_value() )
print()
print( "Deck empty?", my_deck.is_empty() )
print( "Number of cards left in deck:", my_deck.cards_count() )
print()


# Deal second card from the deck and display it (and info about the deck)

card2 = my_deck.deal()
print( "Second card dealt from the deck:", card2 )
print()
print( "Card suit:", card2.get_suit() )
print( "Card rank:", card2.get_rank() )
print( "Card value:", card2.get_value() )
print()
print( "Deck empty?", my_deck.is_empty() )
print( "Number of cards left in deck:", my_deck.cards_count() )
print()


# Compare the two cards

if card1.equal_suit( card2 ):
    print( card1, "same suit as", card2 )
else:
    print( card1, "and", card2, "are from different suits" )

if card1.equal_rank( card2 ):
    print( card1, "and", card2, "of equal rank" )
elif card1.get_rank() > card2.get_rank():
    print( card1, "of higher rank than", card2 )
else:
    print( card2, "of higher rank than", card1 )

if card1.equal_value( card2 ):
    print( card1, "and", card2, "of equal value" )
elif card1.get_value() > card2.get_value():
    print( card1, "of higher value than", card2 )
else:
    print( card2, "of higher value than", card1 )

