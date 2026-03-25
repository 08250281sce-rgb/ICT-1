marks1=float(input("enter the marks for first subject:"))   
marks2=float(input("enter the marks for second subject:"))
marks3=float(input("enter the marks for third subject:"))
average=(marks1+marks2+marks3)/3
print ("average marks: ", average)
if (average >= 90 and marks1 >= 50 and marks2 >= 50 and marks3 >= 50):
    print("Grade: A")
elif (average >= 80 and marks1 >= 50 and marks2 >= 50 and marks3 >= 50):
    print("Grade: B")
elif (average >= 70 and marks1 >= 50 and marks2 >= 50 and marks3 >= 50):
    print("Grade: C")
elif (average >= 60 and marks1 >= 50 and marks2 >= 50 and marks3 >= 50):
    print("Grade: D")
elif (average >= 50 and marks1 >= 50 and marks2 >= 50 and marks3 >= 50):
    print("Grade: E")
else:
    print("you need to work harder.")
