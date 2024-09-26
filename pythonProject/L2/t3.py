a = "aviel"

print(list(range(5)))   # from 0 to 5
print(list(range(1, 50, 10)))   # from 1 to 41 in jumps of 10
print(list(range(50, 10, -3)))   # from 50 ro 11 in jumps of 3 downward
for i in range(5):
    print(a)

names = ["dvir", "adi", "tal"]
for name in names:
    if name == "dvir":
        name = "roey"
    print(f"hello {name}")

for i in range(len(names)):
    if names[i] == "dvir":
        names[i] = "roey"
    print(f"hello {names[i]}")

for moshe in range(5):
    print(moshe)
    print(a)
