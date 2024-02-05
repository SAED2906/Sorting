arr = [1,2,3,3,5,1,6,8]

temp = 0
ls = []
for x in arr:
    c = x-temp # Turn this line into: c = int(10*(x-temp))  this will allow for floats, adjust the multiplier as needed ig
    try:
        s = (c >> 31) & 1
        c /= c
        1/(s)

    except:
        ls.append(x)
    
    temp = x 

print(ls)
