#Math Functions
print(round(a))
print(abs(b))#abs->absolute value means the distance between from 0 to that mentioned whole number                                                        
print(pow(a, b))
print(max(a,b,c))
print(min(a,b,c))

#Math Functions
import math
print(math.pi)
print(math.e)#exponent
print(math.sqrt(8))
print(math.floor(8))
print(math.ceil(8))

#Circumference of circle
import math
radius=float(input("Enter the radius of the circle:"))
Circumference=2*math.pi*radius
print(f"The circumference is:{Circumference}")

#Area of the Circle
radius=float(input("Enter the radius of a circle:"))
area=math.pi*pow(radius, 2)
printf(f"The area of  the  circle is: {round(area, 2)}")

#Hypotyhesis of right angle triangle
import math
a=float(input("Enter side A:"))
b=float(input("Enter side B:"))
c=math.sqrt(pow(a, 2)+pow(b,2))
print(f"Side C= {c}")
