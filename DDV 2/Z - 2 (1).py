import math
x = 0.0374
y = -0.825
z = 16
s1 = 0
s1 =(1+((math.sin(x+y))**2)) / abs(x-(2*y)/(1+(x**2)*(y**2))) * (x**(abs(y))) + (math.pow(math.cos(math.atan(1/z)),2))
print(s1)