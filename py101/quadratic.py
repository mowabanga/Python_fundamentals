# A program that computes value of x using the famous quadratic equation
# Using the math lib
import math
def main():
    print("This program finds the solution of a quadratic expression")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    root = math.sqrt(b * b - 4 * a * c)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)
    
    print("The value of x is: ", x1, x2)
main()