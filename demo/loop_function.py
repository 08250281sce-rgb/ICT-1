#name=input("enter your name:   ")
#for i in name:
 #   print(i)
li=[ "python programming", "python fundamentals", "python interview questions"]
for x in li:
    print(x)
lenli = len(li)
for x in range(lenli):
    print(li[x])
new_tuple = tuple(li) #converting list to tuple
print(new_tuple)
new_set = set(li)
print(new_set)
for x in new_tuple:
    print(x)
#for y in new_set:
 #   print(y)
lenmy_tuple=len(new_tuple) #
for x in range(lenmy_tuple):
    print(new_tuple[x])