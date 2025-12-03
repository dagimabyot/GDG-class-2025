# exercise 36

num = int(input("Enter a number: " ))
def factorial(n):
    i=1
    for j in range (1,n+1):
        i *= j
    return i

print("Factorial of", num , "is" , factorial(num))
