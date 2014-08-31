#===============================================================================
# ProjectEuler.Net
# Problem #004: Largest Palindrom Product
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#===============================================================================

isPalindrome = function(candidate){
        candidate = unlist(strsplit(as.character(candidate),split=""))
        if (length(candidate) == 1) {
                isPal = TRUE
        }
        else {
                if (candidate[1] == candidate[length(candidate)]){
                        if (length(candidate) == 2) {
                                isPal = TRUE
                        }
                        else {
                                candidate = candidate[2:(length(candidate)-1)]
                                isPal = isPalindrome(candidate)
                        }
                }
                else {
                        isPal = FALSE
                }
        }
        isPal
}                

maxPal = function(max){
        maxPal = 0
        n2Pal = 0
        for (n1 in c(max:1)) {
                for (n2 in c(n1:1)){
                        isPal = isPalindrome(n1*n2)
                        if(isPal){
                                if (n1*n2 > maxPal){
                                        n1Pal = n1
                                        n2Pal = n2
                                        maxPal = n1*n2                                        
                                }
                                break
                        } 
                }
                if (n2Pal > n1) break
        }
        c(n1Pal,n2Pal,maxPal)
}

maxPal(999)

# > maxPal(999)
# [1] 993    913    906609
# > 
        