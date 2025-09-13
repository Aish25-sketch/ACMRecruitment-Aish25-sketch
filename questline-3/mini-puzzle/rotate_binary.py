def rotate(binary, k):
    r=binary[k:]+binary[:k]
    decimal=int(r,2)
    return r,decimal
#Example 1
binary="1101"
k=2
a,b=rotate(binary,k)
print("Rotated binary:",a)
print("Decimal value:",b)
#Example 2
binary="1011"
k=3
c,d=rotate(binary,k)
print("Rotated binary:",c)
print("Decimal value:",d)
