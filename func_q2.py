#create a function to calculate average of three numbers, take input from users

#function definition
def print_average(a,b,c):
    average = (a+b+c)/3
    return average

#main program
n1 = int(input("Enter First Number  :"))
n2 = int(input("Enter Second Number :"))
n3 = int(input("Enter Third Number  :"))

avg = print_average(n1,n2,n3)
print("The Average is :",avg)
