# Asks for users name and then prints it in a file
name = input("Please enter your name: ")
output_file = open("name.txt", 'w')
print(name, file=output_file)
output_file.close()

input_file = open("name.txt", 'r')
name = input_file.read().strip()
input_file.close()
print("Your name is ", name)

input_file = open("numbers.txt", 'r')
number1 = int(input_file.readline())
number2 = int(input_file.readline())
input_file.close()
print(number1 + number2)

input_file = open("numbers.txt", 'r')
total = 0
for line in input_file:
    number = int(line)
    total += number
input_file.close()
print(total)
