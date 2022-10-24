import math

try:
  input = input("What is the diameter?\n")
  r = float(input)/2.0
except ValueError:
  exit("Invalid input, please restart program")
π = math.pi
A = π*(r**2)
C = 2.0*π*r
print('The area is: ', A)
print('The circumference is: ', C)