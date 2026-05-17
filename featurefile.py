def even_odd(num):
    for i in range(num, num + 1):
        if i & 1:
            print(i, "is Odd")
        else:
            print(i, "is Even")

n = int(input("Enter a number: "))

even_odd(n)