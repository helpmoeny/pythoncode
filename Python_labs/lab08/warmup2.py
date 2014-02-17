
set1 = set()

set1.add( 900 )
set1.add( 400 )
set1.add( 700 )

print( len( set1 ), set1 )

set1.add( 900 )
set1.remove( 400 )

item = 600
if item in set1:
    set1.remove( item )

print( len( set1 ), set1 )

set2 = { 10, 20, 30, 40 }
set3 = { 20, 30, 40, 50, 60 }

print( set2 & set3 )

print( set2 | set3 )




