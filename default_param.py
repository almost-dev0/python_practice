#we can also assign default parameters to our function, in case no argument is passed

def calc_sum(a=0,b=1):      #here, default values of a ad b are 0
    sum = a + b
    return sum

n2=5

addition = calc_sum(n2)      #if second argument is not written then by default values of a/b will be assumed
print(addition)

addition = calc_sum()                  #if no argument is given the it willl return sum of by dfaylt values of parameters
print(addition)