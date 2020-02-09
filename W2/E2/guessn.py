low = 0
high = 100
userN = abs(int((low + high) / 2))
userC = ""
userIn = ""

print(f"Please think of a number between {low} and {high}")
print("please enter h if your number is higher, l if your number is lower, c if the number is correct")

while userIn != "c" or "C":
    userIn = input(f"Is your secret number {userN}?:")
    if userIn == "c" or userIn == "C":
        userC = userN
        break
    elif userIn == "l" or userIn == "L":
       #what happens if lower
        high = userN
        userN = abs(int((low + high) / 2))
        #print(f"this is l test output {userN} low: {low} high: {high}")
    elif userIn == "h" or userIn == "H":
        #what happens if higher
        low = userN
        userN = abs(int((low + high) / 2))
        #print(f"this is h test output {userN} low: {low} high: {high}")

    else:
        print("I am sorry please enter h if your number is higher, l if your number is lower, c if the number is correct")

print(f"your number is {userC}")
