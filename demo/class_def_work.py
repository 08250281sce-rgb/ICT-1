#total or sum of three marks 
def calculate_total(m1, m2, m3):
    total = m1 + m2 + m3
    return total

#average 
def calculate_average(total):
    average = total / 3
    return average

#checking result 
def check_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"

#taking input from user
m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))

#calculating total, average and result
total = calculate_total(m1, m2, m3)
average = calculate_average(total)
result = check_result(average)

#displaying output
print("Total Marks:", total)
print("Average Marks:", average)
print("Result:", result)

#even and odd checking
def check_even_or_odd():
    num = int(input("Enter a number: "))
    if num % 2==0:
        return "Even"
    else:
        return "Odd"
# Call the function and display the result
print("The number is:", check_even_or_odd())