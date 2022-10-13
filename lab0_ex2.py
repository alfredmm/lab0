import math   #Library (Set of Functions that are used to do a particular 

def introduction_message():
    print("This program prints the roots of a second order equation")
    print("    ax^2 + bx + c = 0")
    print()
   

def input_and_solve():
    a = int(input("Please enter a: "))
    b = int(input("Please enter b: "))
    c = int(input("Please enter c: "))

    delta = b*b - 4*a*c #Negative delta gives value error / Delta Value should always be Positive
                        # b*b > 4*a*c
                        # a = 5, b = 15, c = 20

    x1 = -b + (math.sqrt(delta))
    x2 = -b - (math.sqrt(delta))
   
    print("The Roots are:")
    print("x1 = ", x1)
    print("x2 = ", x2)

def final_message():
    print("Thank you for using this Program...")
    print("----------------------------------")
    print("All Rights Preserved.")

introduction_message() #Calling a function 
input_and_solve() #Calling a function 
final_message() #Calling a function


#Error handling
    
    
