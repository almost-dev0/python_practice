#write a function to calculate factorial of user input n

def calc_fact(num):
    fact = 1
    for i in range (1,num+1):
        fact *= i
    return fact


n = int(input("Enter your number: "))

factorial = calc_fact(n)
print("The factorial of",n,"is :",factorial)
