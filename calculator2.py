import math
"""
This is a calculator program. It will take Users number inputs,
it will also request for the kind of mathematical operations to be performed,
it will perform the calculations and print out the ouput.
"""

print ("Welcome to ZIYTECHS Calculator \n\nLet\'s perform some mathematical operations \n\n")

def get_values(): #Gets user operation option and input and store them as the function get_values()

    while True:
        try:
            maths_operation = int(input("What mathematical operation would you like to perform? \n press 1 for Addition \n press 2 for Subtraction \n press 3 for Multiplication \n press 4 for Division \n press 5 to quit the program \n\n"))
            operations_list = ("an_Addition", "a_Subtraction", "a_Multiplication", "a_Division")
                
        except Exception as e:
            print('\nPlease check your input!, Exception Occurred: {}. \n\nWe don\'t have that mathematical operation!!! \n\n'.format(e))
        else:
            operation = operations_list[(maths_operation-1)]
            num1 = float(input("Input the first number:  "))
            num2 = float(input("Input the first number: "))
            print(f"You are about to carry out {operation} Operation on {num1} and {num2} \n")
            break
    return operation, num1, num2
   

operation, num1, num2 = get_values()

def calculation(operation, num1, num2 ):
    if operation == "an_Addition":
        Add_result = num1+num2
        print(f"\n*****The sum of {num1} and {num2} is {Add_result}*****\n")
    elif operation == "a_Subtraction":
        Subtract_result = num1-num2
        print(f"\n*****The difference between {num1} and {num2} is {Subtract_result}*****\n")
    elif operation == "a_Multiplication":
        Multiply_result = num1*num2
        print(f"\n*****The product of {num1} and {num2} is {Multiply_result}*****\n")
    elif operation == "a_Division":
       Division_result = num1*num2
       print(f"\n*****The division of {num1} by {num2} is {Division_result}*****\n")

def more():
    while True:
        try:
            maths_operation = int(input("\nWill you like to perform another mathematical operation? \n \nPress 1 for Yes and 2 for No \n\n"))
            operations_list = ["Yes", "No"]
            # num3 = float(input("Input the first number:  "))
            # num4 = float(input("Input the first number: "))
    
        except Exception as e:
            print('\nPlease check your input!,\n Exception Occurred: {}, '.format(e))
        else:
            operation2 = operations_list[(maths_operation-1)]
            break
    return operation2

calculation(operation, num1, num2)
operation2 = more()
#print(operation2)

if operation2 == "Yes":
    operation, num1, num2 = get_values()
    calculation(operation, num1, num2)
    operation2 = more()
elif operation2 == "No":
    print("\nThank you for using ZIYTECHS Program \n")
else:
    print("Please enter 1 or 2 \n")
    operation, num1, num2 = get_values()
    calculation(operation, num1, num2)
    operation2 = more()
    
"""
Limitation of this program, If I Type a wrong option as text, it will show a proper error message, but if other wise, it will display weird error message.
The more function currently runs twice, I need to write a while loop for  it to run as many times as possible.
"""