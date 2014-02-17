from triangle import Triangle

scalene_triangle=Triangle(10.0,4.0,7.0)

print('A Triangle with side lengths of: ',scalene_triangle)

print('Is this a valid triangle?')
print(scalene_triangle.is_valid())

print('')
print('Is the Triangle equilateral?')
print(scalene_triangle.is_equilateral())

print('Is the Triangle isosceles?')
print(scalene_triangle.is_isosceles())

print('Is the Triangle scalene?')
print(scalene_triangle.is_scalene())

print('')
print('What are the lengths of this Triangle again..?')
print(scalene_triangle.sides())

print('What are the interior angles of this triangle?')
print(scalene_triangle.angles())

print('What is the perimeter of this triangle?')
print(scalene_triangle.perimeter())

print('What is the area of this triangle?')
print(scalene_triangle.area())

print('What is the scale of this triangle with a factor of 1 then 2 then 5 and then 3/4')
scalene_triangle.scale(1.0)
print(scalene_triangle)
scalene_triangle.scale(2.0)
print(scalene_triangle)
scalene_triangle.scale(5.0)
print(scalene_triangle)
scalene_triangle.scale(0.75)
print(scalene_triangle)
