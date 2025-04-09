# this line is running python code without a variable
print("hello world")
print ('I am learning python')


# Declaring a variable
first_name = "Emmanuel"
last_name = "David"

#concatenation
print(first_name + " " + last_name)

# Types of variables
# integer whole numbers (eg: 0-9)
# floating-point (float) - decimal numbers (e.g 0.1)
# string (str) - text data ("hello", "python",)
# Boolean (bool) - True/false values

age = 18
sentence = "The legal age to vote in"
country = "Nigeria"

full_sentence = sentence + " " + country

print(full_sentence + " is " + str(age))



# creating a function 
def greet ():
    print("Good morning")

    # calling a function 
    greet()

    # pass an argument to a function
    def greet(name):
        print("Good morning " + name)

        # Passing an arguement to a function
        greet("Emmanuel")
        greet("David")

        # A parameter is a variable in a function definition
        # An argument is a value you pass to a function when you call it
        # Funtion with multiple parameters

        def greet(first_name, last_name):
            print("Good morning " + first_name + " " + last_name)

            # calling a function with multiple parameters
                greet("Emmanuel", "David")

# python try except
# handling exceptions
# The 'try'block lets you test a block of code for errors
# The 'except' block lets you handle the error
# The 'else' block lets you exceute code when there is no error
# The 'finally' block lets you execute code regardless of the result of the try-except block

# Example of try except
try: 
    print(x) # This will cause an error because x is not defined
except:
    print("An error occurred") # This will be executed if there is an error

# Many exceptions
try:
    print(x)
except NameError:
    print("variable x is not defined")
except: 
    print("something else went wrong")

    # Else statement
    # Else is executed when there is no error
    try:
        print("Hello")
except:
    print("An error occurred")
else:
    Print("No  error occurred")

    # Finally statement
    # The finally block is always executed, regardless of whether an error occurred or not
try:
    print(x)
except:
    print("An error occurred")
finally:
    print("x will not always execute as long as it's not defined")

# practicalizing everything
# we will create a file that is not writable and try to modify it
try:
    f = open("demo.txt")
    try: 
        f.write("Hello world")
    except: 
        print("something went wrong when editing this file.")
    finally:
        f.close()
except:
    print("File not found")

finally:
    Print("Any file that does not have write permission will not be able to be modified")

    # if conditional statement
    # if statement is used to check a condition
    # if the condition is true, the code inside the if block will be executed
    # if the condition is false, the code inside the else block will be executed

    age = 18
    if age < 18:
        if age == 18:
            print("You ")