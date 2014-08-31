#===============================================================================
# ProjectEuler.Net
# Problem #003: Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#===============================================================================
        
greatestPF = function(originalNumberToFactor) {
        numberToFactor = originalNumberToFactor
        greatestPrimeFactor = 1
        currentPrimeFactor = 1
        factor = 2
        while (factor <= numberToFactor) {
                while (numberToFactor %% factor == 0) {
                        numberToFactor = numberToFactor / factor
                        currentPrimeFactor = factor
                        if (currentPrimeFactor > greatestPrimeFactor) {
                                greatestPrimeFactor = currentPrimeFactor
                        }
                }
                factor = factor + 1
        }
        greatestPrimeFactor
}

greatestPF(600851475143)

#[1] 6857
        