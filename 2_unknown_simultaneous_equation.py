"""
        x1 + y1  =  d1
        x2 + y2  =  d2
"""
x1 = int(input('Enter x1 value: '))
y1 = int(input('Enter y1 value: '))
d1 = int(input('Enter d1 value: '))
x2 = int(input('Enter x2 value: '))
y2 = int(input('Enter y2 value: '))
d2 = int(input('Enter d2 value: '))

x = ((d1*y2)-(d2*y1))/((x1*y2)-(x2*y1))
y = ((d2*x1)-(d1*x2))/((x1*y2)-(x2*y1))

print('X = '+str(x)) 
print('Y = '+str(y))