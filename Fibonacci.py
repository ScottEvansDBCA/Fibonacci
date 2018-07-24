'''Displays the fibonacci value for an integer'''

value = input("Enter your integer: ")
print("You have selected: ", value)

if value < 3:
    print("Please choose a larger number")

def fib_this(val):
    fib = 0
    for i in range(val + 1):
        fib += i
    return fib


print("Total is: ", fib_this(value))