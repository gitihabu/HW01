print('Please input length of three sides of triangle in integer:')
a, b, c = map(int, input().split())
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print('Equilateral triangle')
    elif a==b or b==c or c==a:
        print('isosceles triangle')
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print('right triangle')
    else: print('scalene triangle')
else:print('not a triangle')


