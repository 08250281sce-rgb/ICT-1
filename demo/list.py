my_list = [1,2,3, "hello",3.4,True]
my_reapeated_list = [3]*3
print(type(my_list))
print (my_reapeated_list)
print (my_list[1])
my_list.append("world")
print(my_list)
my_list.extend([5,6,7])
print(my_list)  
my_list.insert(0,"start")
print(my_list)
my_list.remove(3)
print(my_list)  
my_list.pop()
print(my_list)
del my_list[-1]
print(my_list)
del my_list[5]  
print(my_list)
my_list.insert(5, "false")
print(my_list)  
my_reapeated_list.clear()
print(my_reapeated_list)