#write a function that takes a number as input , return "odd" if odd and "even if even"

def check_odd_even(num):
    if(num % 2 == 0):
        print("Even")
    else:
        print("Odd")

n = int(input("Enter a number :"))
check_odd_even(n)