# Factorial for a given range of number
# Use index in for loop as guide to multiplication
fact = 1
for factor in range(1,15):
    fact = factor * fact
    print('{:<02d}'.format(factor), '=', fact)
print(fact)