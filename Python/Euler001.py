#===============================================================================
# ProjectEuler.Net
# Problem #001: Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#===============================================================================

def eul001(x):
    sum35 = 0
    for i in range(1,x):
        if i % 3 == 0 or i % 5 == 0:
            sum35 = sum35 + i
    return sum35

r = eul001(1000)
print(r)

#===============================================================================
# 233168
#===============================================================================
