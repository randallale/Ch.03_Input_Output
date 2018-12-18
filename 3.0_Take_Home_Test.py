'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: ______________________
1. Write a line of code that will print your name.
'''
print("Alex")

'''
2. Write a program that asks someone for their name and then prints their name to the screen?
'''
print(input("What's your name? "))

'''
3. Predict the ouput of the following lines of code and then test them? Write down your prediction and the output.
print (17/9)
print (17//9)
print (17%9)
'''
# I predict that the first one would do 17/9 OUTPUT: 1.888
# I predict the second one will do 17/9 then floor the answer OUTPUT: 1
# The third one would do the remainder of 17/9 OUTPUT: 8

'''
4. Write a a program where a user enters a base and height and you print the area of a triangle.
'''
b = int(input("Base:  \n"))
h = int(input("Height:  \n"))
print("The area of the triangle is", ((h*b)/2))
'''
5. Change this program so it works.
A=May the Force be with you!
print(a)
'''
a=("May the Force be with you!")
print(a)
'''
6. Write a line of code that will ask the user for the length of a square's
side and then print the area of the square
'''
side = int(input("What's the length of the square's side? \n"))
print("The area is", (side**2))

'''7. Ask a user for the length of radii of an ellipse and then print its area. 
Area=pi*a*b where a and b are the lengths of the major radii.
'''
a = float(input("What is the first length of the ellipse? \n"))
b = float(input("What is the second length of the ellipse? \n"))
print("The area of the ellipse is", (3.14*a*b))

'''
8. Ask a user for moles, volume and temperature of a gas and print out the pressure. PV=nRT where n is the number of moles, T is the absolute temperature, V is the
volume, and R is the gas constant 8.3144.
'''
n = int(input("What's are the moles?"))
t = int(input("What's the absolute temperature?"))
v = int(input("What's the volume?"))
print((n*8.3144*t)/v)
'''
9. Ask a user for an integer and then print the square root.
'''
import math
root=int(input("Enter a number: \n"))
print(math.sqrt(root))
'''
10. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. Ask the user for mass and acceleration
and then print out the Force on one line and "Get it?" on the next.
'''
mass=float(input("What is the mass? \n"))
acceleration=float(input("What is the acceleration \n"))
print(mass*acceleration, ("\nGet it?"))