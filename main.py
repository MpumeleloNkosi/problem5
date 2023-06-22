def prime_factor(x):
    divisor = 2  # this is the lowest prime number

    while divisor >= 2:
        if x % divisor == 0: # if the number can be divided with no remainder
            x = x / divisor  # if the number given is divisible by 2 then it is the largest prime factor)
        else:
            divisor += 1  # add one to the divisor to find the next pf if not divisible

    return x


print(prime_factor(34))
