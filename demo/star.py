def pattern(n):
    # Base case
    if n == 0:
        return
    
    # Recursive call
    pattern(n - 1)
    
    # Print stars after returning from recursion
    print("* " * n)

# Take input
n = int(input("Enter a number: "))
pattern(n)