"""
TODO:

1.1. create two variables named x and y
1.2 print "big" if x is bigger than y
1.3 print "small" if x is smaller than y

2.1 run a "for" loop 5 times
2.2 print iteration number every time

3.1 create a variable and initialize it with a number 1-4
3.2 create 4 conditions (if-elif) which will check the variable
3.3 print the season name accordingly

4.1 how many times will the following loop run?
4.2 what will be printed last?

count = 1
while count < 11:
    print(count)
    count = count + 1

5. Write a program with variables holding the following
5.1 Your age
5.2 First letter of your last name
5.3 Current Shekels-Dollar currency
5.4 Did you fly aboard (true/false)
5.5 Your apartment number

6.1 Print all variables
6.2 Add the currency to your age, and check the result

7. Create a program which uses input with the following
7.1 Ask user for his phone number
7.2 Print the words "phone number" and the phone number the user entered

8. Write a program with the following
8.1 Method named printHello() that prints the word "hello"
8.2 Method named calculate() which adds 5+3.2 and prints the result

9. Write a program with the following
9.1. Method that receive your name and prints it
9.2. Method that receive a number, divide it by 2, and print the result

10. Write a program with the following
10.1 Method that receive two numbers, add them, and return the the sum
10.2 Method that receive two Strings, add space between them, and return one spaced string

"""

# Assignment 2, Otir Mesilati

# Q.1
x = 27
y = 56
if x > y:
    print("big")
else:
    print("small")


# Q.2
for index in range(5):
    print(index + 1)  # (index + 1) -> make sure the printing is from 1 through 5 instead of 0 through 4


# Q.3
my_var = 3
if my_var == 1:
    print("winter")
elif my_var == 2:
    print("Autumn/fall")


# Q.4
# the 1 ran 1 time, 2 runs 2 times, 3 ran for 3 times ... the n'th number runs n times,
# so for the largest number 10 -> 10 runs! yay! QED :D


# Q.5
age = 1157
letter = 'Z'
coin_value = 3.62
fly_answer = False
apartment_number = 9876


# Q.6
print(f"My age: {age}, my first name's letter: {letter}, Dollar Currency: {coin_value}, Did I ever flew abroad? "
      f"{fly_answer}, and my apartment number is {apartment_number}")
print(coin_value + age)


# Q.7
phone_number = input("Enter phone number: ")
print("phone number: ", phone_number)


# Q.8
def hello():
    print("hello")


def calculate():
    print(5+3.2)


# Q.9
name_given = input("Enter your name: ")
number_given = int(input("Enter number: "))
print(number_given / 2)

# Q.10
pass

"""

10. Write a program with the following
10.1 Method that receive two numbers, add them, and return the the sum
10.2 Method that receive two Strings, add space between them, and return one spaced string

"""