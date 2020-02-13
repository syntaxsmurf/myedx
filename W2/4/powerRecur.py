def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # This function should take in two values
    # base can be a float or an integer; exp will be an integer ≥0. It should return one numerical value. 
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

print(recurPower(2, 1))