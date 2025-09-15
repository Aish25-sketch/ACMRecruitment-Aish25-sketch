def longest_palindrome(s):
    longest=""
    n=len(s)
    for i in range(n):
        for j in range(i,n):
            str=s[i:j+1]
            if str==str[::-1]:
                if len(str)>len(longest):
                    longest=str
    return longest
s="malayalam was my mom 's favourite subject"
print("Longest Plaindrome:",longest_palindrome(s))
