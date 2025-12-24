#write a function to check whether a number is palindrome or not

def check_palindrome(str):
    revstring = str[::-1]
    if (str == revstring):
        print("Your input is a palindrome")
    else:
        print("Your input is not a palindrome")

string = input("Enter a word/sentence/number : ")
check_palindrome(string)