# factorial for an unknown number
def main():
    print("Finding fatorial of a n")
    n = int(input("Please put in a digit: "))
    fact = 1
    for factor in range(n,1,-1):
        fact *= factor
        print("{:2d}".format(factor), "=", fact)
main()