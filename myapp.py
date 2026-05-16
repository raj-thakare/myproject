# write a function to print table of given user input
def table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
n = int(input("Enter a number: "))
print_table(n)
