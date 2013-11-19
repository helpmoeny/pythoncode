from triangle import Triangle

def main():
    Lines=1
    Lines_valid=0
    total_perimeter=0
    total_area=0

    largest_perimeter=0
    largest_perimeters_area=0

    largest_area=0
    largest_areas_perimeter=0

    triangle_perimeter=''
    triangle_area=''

    for line in fo:
        line = "".join(c for c in line if c not in ('(',')',' '))
        linelist=line.strip().replace(' ', '').split(',')
        print("Line ",Lines,": ",line)
        
        sideA=linelist[0]
        sideB=linelist[1]
        sideC=linelist[2]
        
        triangle=Triangle(sideA,sideB,sideC)
        if triangle.is_valid()==True:
            Lines_valid+=1
            total_perimeter+=triangle.perimeter()
            total_area+=triangle.area()
            if triangle.perimeter()>largest_perimeter:
                largest_perimeter=triangle.perimeter()
                largest_perimeters_area=triangle.area()
                triangle_perimeter=line
            if triangle.area()>largest_area:
                largest_area=triangle.area()
                largest_areas_perimeter=triangle.perimeter()
                triangle_area=line
            print("This Triangle's perimeter= {}, and area= {}".format(triangle.perimeter(),triangle.area()))
        else:
            print("Triangle is not valid")
        Lines+=1

    print("")
    print("Total lines processed: ",Lines)
    print("Total valid triangles processed: ",Lines_valid)
    avg_perimeter=total_perimeter/Lines_valid
    avg_area=total_area/Lines_valid
    print("Average perimeter: ",avg_perimeter)
    print("Average area: ",avg_area)
    print("The Triangle with the largest perimeter= ",largest_perimeter," had a area= ",largest_perimeters_area," with sides: ",triangle_perimeter)
    print("The Triangle with the largest area= ",largest_area," had a perimeter= ",largest_areas_perimeter," with sides: ",triangle_area)

try:
    fo=open("proj09-input.txt")
    main()
except IOError:
    print("Can not open/find file")
