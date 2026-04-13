for i in range(1,4):
    for j in range(1,4):
        print(f"outer loop iteration {i}, inner loop iteration {j+1}")
for i in range(4):
    for j in range(i):
        print("*", end = " ")
    print()