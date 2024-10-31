from colorama import Fore

"""
TODO:

1 Write the following code: a = 1/0

2. Build a corresponding try-expect block to avoid exception

3. Is the following code legal?

try:
    x = 1
finally:
    print("finally")

4. What exception types can be caught by the following handler?

Except:

5. What is wrong with the above type of exception handler?

6. What exceptions can be caught by the following handlers?

..

except IOError

..

except ZeroDivisionError

7. Create a text file named "words.txt" programmatically

8. Write your name into a file

9. Read your file content and print it

10. Write Hebrew content into your text file and print its content programmatically


"""

# Assignment 3, Otir Mesilati


# Q.1
# a = 1 / 0  # this raises a ZeroDivisionError

# Q.2
try:
    a = 1 / 0

except ZeroDivisionError:
    print(Fore.RED + "Aha!! Caught you dividing by zero!😈")  # Adding red for angry parent effects :D


# Q.3
# Yes, The code will compile


# Q.4
# All types, Though if the finally part runs anyway - the idea of using exception tools for this code beats the point...


# Q.5
# It's the most general type of exception, so it lacks specificity for what triggered it


# Q.6
# IOError: If i try to read from a file "gold_puppies.txt" for this module for example, that will throw an IOError as it
# does not exist -> thus having a problem opening it.
# ZeroDivisionError: As we saw in the first question, this kind of error literally pops up when trying to divide by 0


# Q.7
filey = open("words.txt", "x")
filey.close()


# Q.8
filey = open("words.txt", "r+")
filey.write("Otir")
filey.close()


# Q.9

filey = open("words.txt", "r")
print(filey.read())
filey.close()

# Q.10
filey = open("words.txt", "r+", encoding="utf-8")
filey.write("היי")
filey.close()
