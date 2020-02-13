def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    num = min(a, b)

    while num > 1:
        if a % num == 0 and b % num == 0:
            break
        else:
            num -= 1
    return num

print(gcdIter(6, 12))

# isinstance(num, type) could be useful maybe? check for type in variable num