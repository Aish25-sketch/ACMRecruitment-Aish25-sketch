num=int(input("Enter a number"))
bits=8
pos_eq=(1<<bits)+num  
binary=""
n=pos_eq
for i in range(bits):
    binary=str(n%2)+binary
    n=n//2
print("2's complement:",binary)
