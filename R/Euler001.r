#===============================================================================
# ProjectEuler.Net
# Problem #001: Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#===============================================================================

eul001 <- function(x) {
        v = c(1:x-1)
        m = v %% 3 == 0 | v %% 5 == 0
        s = v[m]
        sum(s)
}

r = eul001(1000)
r

#[1] 233168