no_of_student=int(input("enter the number of students:   "))
i=1
student_name={}
while i<=no_of_student:
    name = input("enter the name of the student:  ")
    print("the name of student{}is {}".format(i,name))
    i+=1
    student_name[i]= name
print(student_name)
while True:
    print("this is an infinite loop.press ctrl+c to stop it")