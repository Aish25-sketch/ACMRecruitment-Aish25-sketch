def rotate_array(num,k):
    n=len(num)
    k=k%n  
    return num[-k:]+num[:-k]

num=[1,2,3,4,5,6,7]
k=int(input("Enter a positive integer"))
print("Original array:",num)
print("Rotated array:",rotate_array(num,k))
