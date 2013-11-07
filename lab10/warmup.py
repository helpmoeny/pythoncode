
################################################################################
## Demonstration program for class Date
################################################################################

import date

A = date.Date( 1, 1, 2013 )

print( A )
print( A.to_iso() )
print( A.to_mdy() )
print( A.is_valid() )
print()

B = date.Date( 12, 31, 2013 )

print( B )
print( B.to_iso() )
print( B.to_mdy() )
print( B.is_valid() )
print()

C = date.Date()

C.from_iso( "2013-11-28" )

print( C )
print( C.to_iso() )
print( C.to_mdy() )
print( C.is_valid() )
print()

D = date.Date()

D.from_mdy( "March 15, 2015" )

print( D )
print( D.to_iso() )
print( D.to_mdy() )
print( D.is_valid() )
print()

E = date.Date()

print( E )
print( E.to_iso() )
print( E.to_mdy() )
print( E.is_valid() )
print()

print("[Testing Area-spaces]")
F = date.Date()
F.from_mdy( "October 31, 1994" )#testing with (random)spaces in function call
print( F )
print( F.to_iso() )
print( F.to_mdy() )
print( F.is_valid() )
print()

G = date.Date()
G.from_iso( "1994- 10- 31" )#testing with (random) spaces in function call
print( G )
print( G.to_iso() )
print( G.to_mdy() )
print( G.is_valid() )
print()

print("[Testing Area-erroneous input]")
H = date.Date()
H.from_mdy( "October 31, 1994" )#testing with erroneous input
print( H )
print( H.to_iso() )
print( H.to_mdy() )
print( H.is_valid() )
print()

I = date.Date()
I.from_iso( "1994- 10- 31" )#testing with erroneous input
print( I )
print( I.to_iso() )
print( I.to_mdy() )
print( I.is_valid() )
print()
