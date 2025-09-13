def is_palindrome(n):
    binary=""
    num=n
    while num>0:
        binary=str(num%2)+binary
        num=num//2
    return binary==binary[::-1],binary
numbers = [9, 6]
for n in numbers:
    result,binary=is_palindrome(n)
    print("Binary:",binary)
    if result:
        print("Palindrome\n")
    else:
        print("Not Palindrome\n")
