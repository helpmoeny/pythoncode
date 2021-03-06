
################################################################################
## Class Vector
################################################################################

import math
class Vector( object ):
 
    def __init__( self, x=0, y=0 ):

        self.__x = 0.0
        self.__y = 0.0

        if type( x ) == float or type( x ) == int and type( y ) == float or type( y )== int:
        
            self.__x = x
            self.__y = y

    def __repr__( self ):

        return "Vector: {:.2f},{:.2f}".format( self.__x,self.__y )
       
    def __str__( self ):
            
        out_str = ("{:.2f},{:.2f}").format(self.__x,self.__y)
        
        return out_str

    def magnitude( self ):
        
        # calculates magnitude which is a scalar, returns a float
       
        return math.hypot(self.__x,self.__y)

    def __add__( self, other ):
        
        # a,b + c,d  ==>  (a+c,b+d)

        if type( other ) != Vector:
            other = Vector( other )
            
        x = (self.__x + other.__x)
        y = (self.__y + other.__y)
       
        return Vector( x, y )

    def __sub__( self, other ):

        # a,b - c,d  ==>  (a-c,b-d)

        if type( other ) != Vector:
            other = Vector( other )
            
        x = (self.__x - other.__x)
        y = (self.__y - other.__y)
        
        return Vector( x, y )

    def __mul__( self, other ):

        # (a,b) * n  ==>  (x*n,y*n)
        # (a,b) * (c,d) ==> a*c + b*d
        #Vector multiplication by a scalar:  if V is (x,y), then V*n (and n*V) is the vector (x*n,y*n)
        #Vector multiplication by another vector (dot product): if V=(x,y) and W=(a,b), then V*W = x*a + y*b, which is a scalar.
        
        if type( other ) != Vector:
            x = (self.__x * other)
            y = (self.__y * other)
            return Vector( x, y )#returns new vector
            
        if type( other ) == Vector:
            value = (self.__x * other.__x) + (self.__y * other.__y)
            return value#returns scalar
        return none
        

    
    def __eq__( self, other ):
        valid=False
        if type( other ) != Vector:
            other = Vector( other )
        
        if self.__x == other.__x and other.__y == self.__y:
            valid=True
        else:
            valid=False
        return valid

def main():
    print("Vector1: (3,2.5)")
    vector1=Vector(3,2.5)
    print("Vector2: (4.5,6)")
    vector2=Vector(4.5,6)

    print("")

    print("Vector1 + Vector2")
    print(vector1.__add__(vector2))
    print("Vector1 - Vector2")
    print(vector1.__sub__(vector2))
    print("Vector2 - Vector1")
    print(vector2.__sub__(vector1))

    print("")

    print("Vector1 * Vector2")
    print(vector1.__mul__(vector2))
    print("Vector1 * 5")
    print(vector1.__mul__(5))
    print("Vector2 * 3.5")
    print(vector2.__mul__(3.5))

    print("")

    print("Magnitude of Vector1: ",vector1.magnitude())
    print("Magnitude of Vector2: ",vector2.magnitude())

    print("")

    print("Does Vector1 = Vector2?")
    print(vector1.__eq__(vector2))

    print("")

    print("Vector3= (2,2) and Vector4= (2,2)")
    vector3=Vector(2,2)
    vector4=Vector(2,2)
    print("Does Vector3 = Vector4?")
    print(vector3.__eq__(vector4))

main()
