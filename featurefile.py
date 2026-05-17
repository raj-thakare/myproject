def even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

# User input
n = int(input("Enter a number: "))

# Function call
even_odd(n)