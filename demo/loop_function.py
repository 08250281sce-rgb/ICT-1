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
lenmy_tuple=len(new_tuple) # calculating the length of the tuple
for x in range(lenmy_tuple):
    print(new_tuple[x])
# iterating over set and tuple 
tub = ("john","jane","alice")
for x in tub:
    print(x)
set1={"apple","banana","cherry"}
for x in set1:
    print(x)
bookdetails=dict({"python programming": "john", "python fundamentals": "alice johnson", "python interview question": "jane doe"})
for key in bookdetails:
    print(key,bookdetails[key])

#nested loop