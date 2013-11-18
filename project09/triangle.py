
import math

################################################################################
## Class Triangle
################################################################################

class Triangle( object ):
    
    def __init__( self, sideA=0.0, sideB=0.0, sideC=0.0 ):
        """
        Initialize an object of type Triangle.
        """
        
        self.__sideA = 0.0
        self.__sideB = 0.0
        self.__sideC = 0.0
        self.__valid = False
        
        self.__sideA=sideA
        self.__sideB=sideB
        self.__sideC=sideC
        

    def __validate( self ):
        #
        # Check the three sides to determine if a Triangle is valid.
        #
        sideA=float(self.__sideA)
        sideB=float(self.__sideB)
        sideC=float(self.__sideC)
        perimeter=sideA=sideB+sideC
        largest_side=max(sideA,sideB,sideC)
        if perimeter<0:
            self.__valid=False
            if perimeter-largest_side>largest_side:
                self.__valid=True
    
    def __repr__( self ):
        """
        Return a string (the representation of a Triangle).
        """
        return("{}, {}, {}".format(self.__sideA,self.__sideB,self.__sideC))

    def __str__( self ):
        """
        Return a string (the representation of a Triangle).
        """
        return("( {}, {}, {} )".format(self.__sideA,self.__sideB,self.__sideC))

    def is_valid( self ):
        """
        Return a Boolean (is the Triangle valid?).
        """
        return self.__valid

    def is_equilateral( self ):
        """
        Return a Boolean (is the Triangle an equilateral triangle?)
        """
        #An equilateral triangle has three sides whose lengths are equal. 
        equilateral=False
        if self.__sideA==self.__sideB==self.__sideC:
            equilateral=True
        return equilateral

    def is_isosceles( self ):
        """
        Return a Boolean (is the Triangle an isosceles triangle?)
        """
        #An isosceles triangle has at least two sides whose lengths are equal
        isosceles=False
        if self.__sideA==self.__sideB and self.__sideA==self.__sideC or self.__sideB==self.__sideC and self.__sideA==self.__sideC:
            isosceles=True
        return isosceles

    def is_scalene( self ):
        """
        Return a Boolean (is the Triangle a scalene triangle?)
        """
        #A scalene triangle has no sides whose lengths are equal. 
        scalene=True
        if self.__sideA==self.__sideB or self.__sideA==self.__sideC or self.__sideB==self.__sideC:
            scalene=False
        return scalene

    def sides( self ):
        """
        Return a tuple containing the Triangle's three sides.
        """
        sideA=str(self.__sideA)
        sideB=str(self.__sideB)
        sideC=str(self.__sideC)
        triangle=(sideA,sideB,sideC)
        return triangle
    
    def angles( self ):
        """
        Return a tuple containing the Triangle's three angles (in degrees) 
        """

        pass # REPLACE

    def perimeter( self ):
        """
        Return a float representing the Triangle's perimeter.
        """
        sideA=float(self.__sideA)
        sideB=float(self.__sideB)
        sideC=float(self.__sideC)
        perimeter=sideA=sideB+sideC
        #if the triangle is valid, return perimeter
        if self.is_valid==True:
            return perimeter
    
    def area( self ):
        """
        Return a float representing the Triangle's area.
        """
        sideA=float(self.__sideA)
        sideB=float(self.__sideB)
        sideC=float(self.__sideC)
        s=((sideA+sideB+sideC)/2)
        Area=(s(s-sideA)(s-sideB)(s-sideC))**.5
        return Area

    def scale( self, factor=1.0 ):
        """
        Scale all three of a Triangle's sides by the same factor.
        """
        #if the triangle is valid, then...
        if self.is_valid==True:
            if factor>0:
                sideA=float(self.__sideA)*factor
                sideB=float(self.__sideB)*factor
                sideC=float(self.__sideC)*factor
                #what do we return?

