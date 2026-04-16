i=10      #count down from 10 to 1
while i>=1:
    print(i)
    i-=1
print("times up !")

#2 sum until user enter 0
num=int(input("Enter a number (0 to stop): "))
sum=0
while num!=0:
    sum+=num
    num=int(input("Enter a number (0 to stop): "))
print("The sum is:", sum)

#3 
i=1
while i<=3:
    username=input("Enter username: ")
    password=input("Enter password: ")
    if username=="admin" and password=="1234":
        print("Login successful!")
        break
    else:
        print("Invalid credentials. Try again.")