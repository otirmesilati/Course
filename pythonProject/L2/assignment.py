# print the numbers from 1 to 101, but when the number is divided by or has the digit 7 - don't print it

for boom_index in range(1, 102):
    if (boom_index % 7 == 0) or (int(boom_index / 10) == 7) or (boom_index % 10 == 7):
        continue
    else:
        print(boom_index)
