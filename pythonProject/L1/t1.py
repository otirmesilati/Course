print("hi")
a = 4
b = "aviel"
c = True
d = ["aviel", "buskila", 34, True]
e = {"fname": "aviel", "lname": "buskila", "age": 34}
f = dict(fname="aviel", lname="buskila", age=34)
list_of_people = [e, f]
print(d[2])
print(e["lname"])
print(list_of_people)
print("name is" + b)
r = 4 + 4
s = "aviel" + "buskila"
u = "aviel" + str(4)
t = "aviel" * 4
v = int(5.4)
fname = "aviel"
lname = "buskila"
first = fname + lname

# These are all the sames

second = "{} {}".format(lname, fname) # concat strings
third = f"{lname} {fname}"
forth = "%s %s" % (lname, fname)
print(t)
print(u)
