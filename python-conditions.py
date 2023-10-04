#check given number is even or not

num = "Enter the number: "
a = input(num)
a = int(a)

if (a % 2) == 0:
    print("Given number is even.")
else:
    print("Given number is odd.")



#Address validation
dno = input("Enter Address: ")

if not (dno.isnumeric()):
    print("Door number should be a number.")
else:
    print("Door number is valid.")

village = input("Enter Your Village: ")
if not (village.isalpha()):
    print("village name is not valid.")
else:
    print("village name is valid.")

dist = input("Enter Your District: ")
if not (dist.istitle()):
    print("district name should be string.")
else:
    print("district name is valid.")

state = input("Enter Your State: ")
if not (state.istitle()):
    print("state name should be string.")
else:
    print("state name is valid.")

country = input("Enter Your Country: ")
if not (country.isalpha()):
    print("country name should be string.")
else:
    print("country name is valid.")



#checking given number palindrome or not

str = input("Enter the string: ")
if (str == str[::-1]):
    print("This string is palindrome.")
else:
    print("This string is not palindrome.")
