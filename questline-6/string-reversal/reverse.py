# Iterative method
def rev_iterative(s):
    s=list(s) 
    start,end=0,len(s)-1
    while start<end:
        s[start],s[end]=s[end],s[start]
        start+=1
        end-=1
    return "".join(s)

# Recursive method
def rev_recursive(s):
    if len(s)<=1:
        return s
    return rev_recursive(s[1:])+s[0]

str=input("Enter a string: ")
print("Reversed(Iterative):",rev_iterative(str))
print("Reversed(Recursive):",rev_recursive(str))
