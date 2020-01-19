# Basic  Python Calculator

print("This is a basic Python calculator!")
print("")


def addition():  # Basic function for simple addition

    try:                                                    #   This is part checks the input
        num1 = float(input("Enter first number: "))         #   it makes sure that the input is a number
    except ValueError:                                      #   this will loop until the first number is suitable
        print("Invalid number")                             #   once the input is checked and confirmed to be a float
        addition()                                          #   the code will move onto the second number

    while True:                                             #   This part of the code also checks the input
        try:                                                #   it does the same as the code above
            num2 = float(input("Enter second number: "))    #   however
        except ValueError:                                  #   it uses a while loop to check
            print("Invalid number")                         #   i had to use a while loop here because
            continue                                        #   calling the function would reset it and
        else:                                               #   call the first input again (num1)
            result = num1 + num2                            #   doing this would permanently loop until
            print("")                                       #   the input given was a float just like the previous one
            print(result)                                   #   once the user gives a good answer
            break                                           #   the codes makes sure that it is a float
    print("")                                               #   and the loop will break


def subtraction():  # Basic function for simple subtraction

    try:                                                    #   This is part checks the input
        num1 = float(input("Enter first number: "))         #   it makes sure that the input is a number
    except ValueError:                                      #   this will loop until the first number is suitable
        print("Invalid number")                             #   once the input is checked and confirmed to be a float
        subtraction()                                       #   the code will move onto the second number

    while True:                                             #   This part of the code also checks the input
        try:                                                #   it does the same as the code above
            num2 = float(input("Enter second number: "))    #   however
        except ValueError:                                  #   it uses a while loop to check
            print("Invalid number")                         #   i had to use a while loop here because
            continue                                        #   calling the function would reset it and
        else:                                               #   call the first input again (num1)
            result = num1 + num2                            #   doing this would permanently loop until
            print("")                                       #   the input given was a float just like the previous one
            print(result)                                   #   once the user gives a good answer
            break                                           #   the codes makes sure that it is a float
    print("")                                               #   and the loop will break



def multiplication():  # Basic function for simple multiplication

    try:                                                    #   This is part checks the input
        num1 = float(input("Enter first number: "))         #   it makes sure that the input is a number
    except ValueError:                                      #   this will loop until the first number is suitable
        print("Invalid number")                             #   once the input is checked and confirmed to be a float
        multiplication()                                    #   the code will move onto the second number

    while True:                                             #   This part of the code also checks the input
        try:                                                #   it does the same as the code above
            num2 = float(input("Enter second number: "))    #   however
        except ValueError:                                  #   it uses a while loop to check
            print("Invalid number")                         #   i had to use a while loop here because
            continue                                        #   calling the function would reset it and
        else:                                               #   call the first input again (num1)
            result = num1 + num2                            #   doing this would permanently loop until
            print("")                                       #   the input given was a float just like the previous one
            print(result)                                   #   once the user gives a good answer
            break                                           #   the codes makes sure that it is a float
    print("")                                               #   and the loop will break


def division():  # Basic function for simple division

    try:                                                    #   This is part checks the input
        num1 = float(input("Enter first number: "))         #   it makes sure that the input is a number
    except ValueError:                                      #   this will loop until the first number is suitable
        print("Invalid number")                             #   once the input is checked and confirmed to be a float
        division()                                          #   the code will move onto the second number

    while True:                                             #   This part of the code also checks the input
        try:                                                #   it does the same as the code above
            num2 = float(input("Enter second number: "))    #   however
        except ValueError:                                  #   it uses a while loop to check
            print("Invalid number")                         #   i had to use a while loop here because
            continue                                        #   calling the function would reset it and
        else:                                               #   call the first input again (num1)
            result = num1 + num2                            #   doing this would permanently loop until
            print("")                                       #   the input given was a float just like the previous one
            print(result)                                   #   once the user gives a good answer
            break                                           #   the codes makes sure that it is a float
    print("")                                               #   and the loop will break


def oper():  # Basic function for selecting the operation

    operation = input("""Pick one of the following
[+]
[-]
[*]
[/]
Enter the operation you want to use: """)
                                                            #   [+], [-] (Addition, subtraction)
                                                            #   [*], [/] (Multiplication, division)
    if operation == "+":
        addition()
    elif operation == "-":
        subtraction()
    elif operation == "*":
        multiplication()
    elif operation == "/":
        division()
    while operation != "+" or "-" or "*" and "/":
        oper()


oper()
