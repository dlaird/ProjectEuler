#===============================================================================
# ProjectEuler.Net
# Problem #005: Smallest Multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 
# to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?
#===============================================================================

from operator import mul
from functools import reduce

def factors(numberToFactor):
    numberToFactor = numberToFactor
    factors = [1]
    factor = 2
    while factor <= numberToFactor:
        while numberToFactor % factor == 0:
            numberToFactor = numberToFactor / factor
            factors.append(factor)
        factor = factor + 1
    return factors

def smallestMultiple(test):
    product = test * (test-1)
    productFactors = factors(product)
    for counter in range(test-2,0,-1):
        if product % counter != 0:
            counterFactors = factors(counter)
            oldProductFactors = sorted(productFactors)
            productFactors = []
            while len(oldProductFactors)> 0 or len(counterFactors)> 0:
                if len(oldProductFactors) > 0 and len(counterFactors) > 0:
                    productFactor = oldProductFactors[0]
                    counterFactor = counterFactors[0]
                    if productFactor == counterFactor:
                        productFactors.append(productFactor)
                        oldProductFactors = oldProductFactors[1:len(oldProductFactors)]
                        counterFactors = counterFactors[1:len(counterFactors)]
                    elif productFactor < counterFactor:
                        productFactors.append(oldProductFactors.pop(0))
                    else:
                        productFactors.append(counterFactors.pop(0))
                elif len(oldProductFactors) > 0:
                    productFactors.append(oldProductFactors.pop(0))
                elif len(counterFactors) > 0:
                    productFactors.append(counterFactors.pop(0))
    return reduce(mul,productFactors)
                    

print(smallestMultiple(10))
print(smallestMultiple(20))

#===============================================================================
# 2520
# 232792560
#===============================================================================
