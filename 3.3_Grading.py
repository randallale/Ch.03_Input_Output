'''
Grading PROGRAM
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''

print("What's your current semester grade?")
current = int(input())
print("What was the final exam grade?")
final_grade = int(input())
print("What was the final's weight")
weight = int(input())

overall = (100-weight)*current+(weight*final_grade)
overall = overall/100
print("You got a ", end= str(overall))
print('%')