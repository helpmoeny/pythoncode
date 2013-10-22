
map1 = { 200: "EE", 100: "ME", 500: "CS" }

print( map1 )

print( map1[ 100 ] )

map1[ 400 ] = "AE"

flag = 500 in map1
print( flag )

for key in map1.keys():
    print( key )
    
for value in map1.values():
    print( value )

for key, value in map1.items():
    print( key, value )

map2 = {}

map2[ "Joyce" ] = 7
map2[ "Mike" ] = 12
map2[ "Bea" ] = 9

print( map2 )

map2[ "Mike" ] = 33
map2[ "Bea" ] = map2[ "Bea" ] + 5
map2[ "Joyce" ] += 10

print( map2 )

if "William" in map2:
    print( map2[ "William" ] )

if "Bea" in map2:
    print( map2[ "Bea" ] )



