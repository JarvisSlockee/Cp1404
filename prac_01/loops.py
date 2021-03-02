# odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# every 10 numbers between 0 and 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# counting down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# printing the number of stars the user asks for
num_stars = int(input("Number of stars: "))
for i in range(num_stars):
    print('*', end=' ')
print()

# lines of increasing stars
for i in range(1, num_stars + 1):
    print('*' * i)
print()
