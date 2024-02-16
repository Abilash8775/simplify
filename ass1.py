# Write a python code for converting integer values to Indian currency notations, without
# using the currency libraries

def convertINR(curr):
    if curr < 0 and curr > -1000:
        return curr
    else:
        s, *d = str(curr).partition(".")
        r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
        return "".join([r] + d)
print(convertINR(12345678946))