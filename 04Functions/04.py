import math

def circle(radius):
    area= 3.14*(radius ** 2)
    circumference=2*3.14*radius
    return(area,circumference)
a,c=(circle(5))
print("Area of Circle:",round(a,2) ,"Circumference of Circle:",round(c,2))