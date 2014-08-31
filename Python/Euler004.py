#===============================================================================
# ProjectEuler.Net
# Problem #004: Largest Palindrom Product
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#===============================================================================

def isPalindrome(candidate):
    candidate = str(candidate)
    if len(candidate) == 1:
        isPal = True
    else:
        if candidate[0] == candidate[len(candidate)-1]:
            if len(candidate) == 2:
                isPal = True
            else: 
                candidate = candidate[1:(len(candidate)-1)]
                isPal = isPalindrome(candidate)
        else:
            isPal = False
    return isPal

def maxPal(upBound):
    n1Pal = 0
    n2Pal = 0
    maxPal = 0
    for n1 in range(upBound,0,-1):
        for n2 in range(n1,0,-1):
            isPal = isPalindrome(n1*n2)
            if isPal:
                if n1*n2 > maxPal:
                    n1Pal = n1
                    n2Pal = n2
                    maxPal = n1 * n2
                break
        if n2Pal > n1: 
            break
    return n1Pal, n2Pal, maxPal

print(maxPal(999))
        
#===============================================================================
# (993, 913, 906609)
#===============================================================================
            
    
    
