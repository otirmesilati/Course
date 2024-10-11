import requests
with open("input.txt", "r") as my_file:
    names = my_file.read().splitlines()
    for name in names:
        print(name)
my_file.close()


with open("names.txt", "r") as my_file:
    names = my_file.read().splitlines()
    for name in names:
        print(name)
with requests.get("https://en.wikipedia.org/wiki/Main_Page") as response:
    response.raise_for_status()
