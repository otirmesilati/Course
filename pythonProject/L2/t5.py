age = int(input("Enter your age "))
if 31 < age < 41:
    print("you are ok")

years_of_experience = int(input("Enter your years of experience "))
if 2 < years_of_experience < 10:
    print("you have experience")


def square(n):
    print(n * n)


def check_in_interval(what_to_ask, min_value, max_value, what_to_print):
    current_value = int(input(what_to_ask))
    if min_value < current_value < max_value:
        print(what_to_print)


square(5)

check_in_interval("enter your age: ", 0, 20, "you are ok")
check_in_interval("enter your experience: ", 0, 20, "nice")
