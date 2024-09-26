current_name = input("what is your name: ")
while current_name != "quit":
    if current_name == "eden":
        continue
        # inputting eden will make an infinite loop logic
    if current_name == "ronen":
        break
    print(f"hello {current_name}")
    current_name = input("what is your name: ")
else:  # else for while -> if there's an early exit of the loop because of false condition
    print("Thank you for playing")

for i in range(5):
    print(i)

print("*******************************")
print(i)
print("*******************************")

# list comprehension
result = [i for i in range(1, 101) if i % 7 != 0 and "7" not in str(1)]
print(result)

names = ["natan", "shay", " ronen", "aaron"]
search = [i.upper() for i in names if "n" in i]
print(search)
