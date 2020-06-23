from math import sin,pi
r=int(input('Enter radius of circle: '))
angle = float(input("Input angle: "))
area=  pi * r*r* (angle/360) - 1/2 * r*r * sin(angle*pi/180)
print('Area of minor segment:',area)
print('Area of major segment:',pi*r*r-area)