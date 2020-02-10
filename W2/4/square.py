def square(x):
    '''
    x: int or float.
    '''
    epsilon = 0.01
    guess = x/2.0

    while abs(guess*guess - x) >= epsilon:
        guess = guess - (((guess**2) - x)/(2*guess))

    return guess