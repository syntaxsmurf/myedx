s = "azcbobobegghakl"
total = 0
for i in range(len(s)-2):
    if s[i:i+3] == "bob":
        total += 1
    
print ("Number of times bob occours is: ", total)