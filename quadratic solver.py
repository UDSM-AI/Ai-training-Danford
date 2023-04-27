import math
def lap_quadratic(a, b, c):
   discriminant = b**2 - 4*a*c
   if discriminant > 0 :
      root1 = (-b + math.sqrt(discriminant))/(2*a)
      root2 = (-b - math.sqrt(discriminant)) / (2 * a)
      return "The two roots are:", root1,root2
   elif discriminant == 0:
      root = -b / (2*a)
      return "The root will be:",root
   else:
      real_part = -b / (2*a)
      imarginary_part = math.sqrt(abs(discriminant))/(2*a)
      return "The roots will be complex roots:", f"{real_part} + {imarginary_part}i",  f"{real_part} - {imarginary_part}i"
a = float(input("Enter the value in X^2: "))
b = float(input("Enter the value in X: "))
c = float(input("Enter the value in constant: "))

roots = lap_quadratic(a, b, c)
print(roots)
