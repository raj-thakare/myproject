def even_odd(num):
    while num >= 0:
        if num % 2 == 0:
            print(num, "is Even")
        else:
            print(num, "is Odd")
        break
        
n = int(input("Enter a number: "))
even_odd(n)