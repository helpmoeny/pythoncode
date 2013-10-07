print( "Richter   Joules         TNT")

Joules = (10**((1.5*1)+4.8))
Joules_float = float(Joules)

TNT = (Joules/(4.184*10**9))
TNT_float = float(TNT)
print("1 ", Joules_float, TNT_float)

Joules = (10**((1.5*5)+4.8))
Joules_float = float(Joules)

TNT = (Joules/(4.184*10**9))
TNT_float = float(TNT)
print("5 ", Joules_float, TNT_float)

Joules = (10**((1.5*9.1)+4.8))
Joules_float = float(Joules)

TNT = (Joules/(4.184*10**9))
TNT_float = float(TNT)
print("9.1 ", Joules_float, TNT_float)

Joules = (10**((1.5*9.2)+4.8))
Joules_float = float(Joules)

TNT = (Joules/(4.184*10**9))
TNT_float = float(TNT)
print("9.2 ", Joules_float, TNT_float)

Joules = (10**((1.5*9.5)+4.8))
Joules_float = float(Joules)

TNT = (Joules/(4.184*10**9))
TNT_float = float(TNT)
print("9.5 ", Joules_float, TNT_float)

num_str = input( "Please enter a Richter scale value: " )
Richterinput = float( num_str ) 
print("Richter scale value: ",Richterinput)
Joulesinput = (10**((1.5*Richterinput)+4.8))
print("Equivalence in joules: ",Joulesinput)
TNTinput = (Joulesinput/(4.184*10**9))
print("Equivalence in tons of TNT: ",TNTinput)

















