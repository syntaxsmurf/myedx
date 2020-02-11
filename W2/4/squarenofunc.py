epsilon = 0.01
x = 43
guess = x/2.0

while abs(guess*guess - x) >= epsilon:
        guess = guess - (((guess**2) - x)/(2*guess))

print(guess)