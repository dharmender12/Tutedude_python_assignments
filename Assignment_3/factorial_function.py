def factorial(n):
    if n < 0 : 
        return "Factorial is not defined for negative numbers."
    elif n < 2 : 
        return 1 
    else : 
         return n * factorial(n-1) ## Recursion 
    
num = int(input("Enter a number: "))

fact = factorial(5)
print(f"Factorial of {num} is: {fact}")
