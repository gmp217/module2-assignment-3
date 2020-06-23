from  math import tan ,pi
n  = int(input("Enter the number of sides: "))
l = int(input("Enter the length of each side: "))
area = (n* l** 2)/(4 * tan(pi/n))
print('Area of polygon is:',area)