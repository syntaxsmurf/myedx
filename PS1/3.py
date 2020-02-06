s = 'abcabc'

c = ""
d = ""
e = ""

for i in s:
    if c <= i:
        c = i
        d += c
        if len(d) > len(e):
            e = d
    else:
        c = i
        d = c
print('Longest substring in alphabetical order is: ' + e)