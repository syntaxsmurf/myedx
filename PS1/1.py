s = "azcbobobegghakl"
var = 0
for char in s:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        var += 1
print("Number of vowels:" + " " + str(var))
