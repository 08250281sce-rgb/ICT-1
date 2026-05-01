#name = input("Enter your name: ")
#greet = lambda x: print("hello",x)
#greet(name)

even_odd = lambda x: "even" if x % 2 == 0 else "odd"
num = int(input("enter a number:"))
print(even_odd(num))

arith = lambda x,y: (x+y, x-y, x*y, x/y)
num1 = int(input("enter first number:  "))
num2 = int(input("enter second number:  "))
print(arith(num1,num2))
    #filter function with lambda
mylist = [1,2,3,4,5]
even = filter(lambda x: x%2 == 0, mylist)
print(list(even))
    #map function with lambda
#mylist = [1,2,3,4,5]
double = map(lambda x: x*2, mylist)
result1 = list(double)
print(result1)
orginal_list = map(lambda x: x//2, result1)
print(list(orginal_list))

      #reduce function with lambda
from functools import reduce
mylist = [1,2,3,4]
mul = reduce(lambda x,y: x*y, mylist)
print(mul)
