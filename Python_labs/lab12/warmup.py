
##
## Demonstrate some of the operations of the Fraction class
##

import fraction

def display( arg1, arg2 ):

    print( "Display:", locals() )
    print()
    
    print( "arg1:", arg1 )
    print( "arg2:", arg2 )
    print()

    print( "arg1 + arg2:", arg1 + arg2 )
    print()
    print( "arg1 - arg2:", arg1 - arg2 )
    print()

    print( "arg1 == arg2:", arg1 == arg2 )
    print()
    print( "arg1 < arg2:", arg1 < arg2 )
    print()
    print( "arg1 > arg2:", arg1 > arg2 )
    print()

def main():

    A = fraction.Fraction( 1, 2 )
    B = fraction.Fraction( 2, 3 )
    display( A, B )

    C = fraction.Fraction( 4, 5 )
    D = fraction.Fraction( 4, 5 )
    display( C, D )

    E = fraction.Fraction( 3, 4 )
    F = fraction.Fraction( 5, 1 )
    display( E, F )

    G = fraction.Fraction( 7, 1 )
    H = fraction.Fraction( 1, 4 )
    display( G, H )

main()
