# Exercise 1
def squares(n):
    for i in range(n):
        yield i * i

n = int(input())
square_generator = squares(n)

for square in square_generator: 
    print(square)

# Exersice 2
def even(n):
    if n % 2 == 0:
        yield n

n = int(input())
for i in range(n+1):
    for j in even(i):
        print(j)

# Exercise 3
def dev3_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter the number: "))
for num in dev3_4(n):
    print(num)

# Exercise 4
def square(a):
    yield a*a

a = int(input())
b = int(input())    
for i in range(a, b):
    for j in square(i):
        print(j)

# Exercise 5
def countdown(n):
    while n >= 0:
        yield n
        n = n-1

n = int(input("Enter the number: "))
for num in countdown(n):
    print(num)