low = 0
high = 100
userN = low + high / 2
userC = ""

print(f"Please think of a number between {low} and {high}")
print("please enter h if your number is higher l if your number is lower c if the number is correct")

while userN != "c" or "C":
    userIn = input(f"Is your secret number {userN}?:")
    if userIn == "c" or userIn == "C":
        userC = userN
        break
    elif userIn == "l" or userIn == "L":
       #what happens if lower
        print("l")
    elif userIn == "h" or userIn == "H":
        #what happens if higher
        print("h")

    else:
        print("I am sorry please select l for lower or h for higher or c if it's the correct number")

print(f"your number is {userC}")
