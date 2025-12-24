#take input from user n and find its factorial

n = int(input("Enter your number : "))

fact = 1
for i in range(1,n+1):
    fact = fact*i

print("The factorial of",n,"is ",fact)