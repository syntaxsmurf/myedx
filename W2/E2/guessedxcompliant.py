low = 0
high = 100
userN = int((low + high) / 2)
userC = ""
userIn = ""

print("Please think of a number between" , low , "and" , high)
while userIn != "c" or "C":
    userIn = input("Is your secret number " + str(userN) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if userIn == "c" or userIn == "C":
        userC = userN
        break
    elif userIn == "h" or userIn == "H": 
        #what happens if higher
        high = userN
        userN = int((low + high) / 2)
        #print(f"this is h test output {userN} low: {low} high: {high}")
    elif userIn == "l" or userIn == "L":

        #what happens if lower
        low = userN
        userN = int((low + high) / 2)
        #print(f"this is l test output {userN} low: {low} high: {high}")

    else:
        print("I am sorry please enter h if your number is higher, l if your number is lower, c if the number is correct")

print("Game over. Your secret number was: " + str(userC))