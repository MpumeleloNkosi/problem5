def prime_factor(x):
    primeFactor = 2  # this is the lowest prime number

    while primeFactor*primeFactor<=x: #sq factor of lowest prime factor that is greater than number
        if x % primeFactor == 0: # if the number can be divided with no remainder
            x= x//primeFactor# if the number given is divisible by 2 then it is the largest prime factor)
        else:
            primeFactor += 1  # add one to the divisor to find the next pf if not divisible

    return x
largest = prime_factor(600851475143) #input the largest number into a variable
print(largest)
