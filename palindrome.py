#checking given number palindrome or not

str = input("Enter the string: ")
if (str == str[::-1]):
    print("This string is palindrome.")
else:
    print("This string is not palindrome.")

