
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

        if isinstance(self.__sideA, (int, float)):
            if isinstance(self.__sideB, (int, float)):
                if isinstance(self.__sideC, (int, float)):
                    self.__sideA=sideA
                    self.__sideB=sideB
                    self.__sideC=sideC
                    self.__valid = self.__validate()
        

    def __validate( self ):
        #
        # Check the three sides to determine if a Triangle is valid.
        #
        sideA=float(self.__sideA)
        sideB=float(self.__sideB)
        sideC=float(self.__sideC)
        
        perimeter=sideA+sideB+sideC
        triangle=[sideA,sideB,sideC]
        triangle.sort()
        
        if perimeter>0:
            if (triangle[0]+triangle[1])>triangle[-1]:
                return True
            else:
                return False
        else:
            return False
    
    def __repr__( self ):
        """
        Return a string (the representation of a Triangle).
        """
        return("{}, {}, {}".format(self.__sideA,self.__sideB,self.__sideC,'.2f'))

    def __str__( self ):
        """
        Return a string (the representation of a Triangle).
        """
        return("( {}, {}, {} )".format(self.__sideA,self.__sideB,self.__sideC,'.2f'))

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
        sideA=float(self.__sideA)
        sideB=float(self.__sideB)
        sideC=float(self.__sideC)
        angleA=math.acos((-sideA**2+sideB**2+sideC**2)/(2*sideB*sideC))
        angleB=math.acos((sideA**2-sideB**2+sideC**2)/(2*sideA*sideC))
        angleC=math.acos((sideA**2+sideB**2-sideC**2)/(2*sideA*sideB))
        angleA_degrees=angleA*(180/math.pi)
        angleB_degrees=angleB*(180/math.pi)
        angleC_degrees=angleC*(180/math.pi)
        return(angleA_degrees,angleB_degrees,angleC_degrees)

    def perimeter( self ):
        """
        Return a float representing the Triangle's perimeter.
        """
        sideA=float(self.__sideA)
        sideB=float(self.__sideB)
        sideC=float(self.__sideC)
        perimeter=sideA+sideB+sideC
        #if the triangle is valid, return perimeter
        if self.__valid==True:
            return perimeter
    
    def area( self ):
        """
        Return a float representing the Triangle's area.
        """
        s=((self.__sideA+self.__sideB+self.__sideC)/2)
        Area=math.sqrt(s*(s-self.__sideA)*(s-self.__sideB)*(s-self.__sideC))
        return Area

    def scale( self, factor=1.0 ):
        """
        Scale all three of a Triangle's sides by the same factor.
        """
        #if the triangle is valid and the scale factor is greater than 0, than change the sides accordingly
        
        if self.__valid==True:
            if factor>0:
                self.__sideA=self.__sideA*factor
                self.__sideB=self.__sideB*factor
                self.__sideC=self.__sideC*factor


