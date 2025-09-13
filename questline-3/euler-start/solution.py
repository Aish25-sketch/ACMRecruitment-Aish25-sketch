#Problem 1: Multiples of 3 or 5
def p1():
    sum=0
    for i in range(1000):
        if i%3==0 or i%5==0:
            sum+=i
    return sum
print("Sum of Multiples=",p1())



# Problem 6: Sum Square Difference
def p6():
    n=100
    sum_of_n=sum(range(1,n+1))
    square=sum_of_n**2
    sum_of_sq=0
    for i in range(1,n+1):
        sum_of_sq+=i*i
    return square-sum_of_sq
print("Difference=",p6())
