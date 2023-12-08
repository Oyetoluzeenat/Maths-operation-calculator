"""
ZIYTECHS CALCULATOR PROGRAM
	Welcome the user
	Inform the user about the available mathematical operations
	List the available operations (Addition, Subtraction, Multiplication, Division, Square, square root, Exit program (Alert, are you sure you want to exit this program?))
	Ask the user the kind of operation they intend to perform and take their response
	Convert the response to float, and save the response in a variable.
	*** Handle user input errors ***
	Request for the numbers intended for mathematical operation (num1, num2)
	Handle user input errors
	Save the responses in a variable
	Write a function to perform the operations and display the results. For the division function, check for zero denominator error. You can’t perform divide by zero operation. Use conditional statement to handle zero input for denominator.
	Print the result
	Thank the user  
	Request if the user intends to perform another operation (If yes, rerun the program, if no Terminate the program safely)
	Exit the program

Note: Use line breaks and comments where necessary.

"""

#
print ("\n***********  Welcome to ZIYTECHS Calculator  *********** \n\n")
print("Here are some mathematical operations you can perform: \n")

print("press 1 for Addition") 
print("press 2 for Subtraction") 
print("press 3 for Multiplication") 
print("press 4 for Division")
print("press 5 for power")
print("press 6 for Squareroot")
print("press 7 to Quit the program \n")

while True: 
    try:
        maths_operation = int(input("What mathematical operation would you like to perform? -->  "))

    except Exception as e:
         print('\nPlease check your input!, Exception Occurred: {}. \n\nWe don\'t have that mathematical operation!!! \n\n'.format(e))

    if maths_operation ==1:
        def add():
            pass

    if maths_operation == 2:
        def subtract():
            pass
    
    if maths_operation ==3:
        def multiply():
            pass
    
    if maths_operation ==4:
        def division():
            pass
    
    if maths_operation ==5:
        def power():
            pass
        
    if maths_operation ==6:
        def squre_root():
            pass

    if maths_operation == 7:
        break

print("\nThank you for using ZIYTECHS Program \n")

# print("\nWill you like to perform another mathematical operation? --> \n")

# Yes = input("press Y for Yes")
# No = input("press N for No")

# if Yes.upper == "Y":