from triangle import Triangle

fo=open("proj09-input.txt")

Lines=0
for line in fo:
    line = "".join(c for c in line if c not in ('(',')'))
    line.strip().replace(' ', '').split(',')
    
    sideA=line[0]
    print(sideA)
    sideB=line[2]
    print(sideB)
    sideC=line[4]
    print(sideC)
    triangle=Triangle(sideA,sideB,sideC)
    if triangle.is_valid()==True:
        print(triangle.is_valid())
        print("This Triangle's perimeter= {}, and area= {}".format(triangle.perimeter(),triangle.area()))
    else:
        print("Triangle is not valid")
    
    Lines+=1
