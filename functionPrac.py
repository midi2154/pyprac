# function = block of reusable code
#place() after the function name to invoke it

# return is statement used to 
# end a function and send a result back to the caller


def happy_birthday(name, age):
    print(f"happy birthday to {name}!")
    print(f"you are {age} old!")
    print("Happy birthday to you!")
    print()
happy_birthday("Mohammed", 29) 
happy_birthday("asmau", 18)
happy_birthday("umar",19)


def display_invoice(username, amount, due_date):
    print(f"Hello  {username}")
    print(f"your Bill of ${amount:.2f} is due on:{due_date}")

display_invoice("Moh", 20, "15/17/2026")


def add(x, y):
    z = x + y
    return z
def divide(x,y):
    b = x/y
    return b
def minus(x,y):
    j = x-y
    return j
def times(x, y):
    l = x*y
    return l


print(add(1,7))
print(divide(4,2))
print(minus(20,15))
print(times(980, 250))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("mohammed", "idi")

print(full_name)


def rec_area(length,  width):
    area = length * width
    return area
print(rec_area(14,10))


def rec_area(length,  width):
    area = length * width
    print(area)

rec_area(14, 10)


counter = 10

def increment(value):
    global counter
    counter += value
    return counter

print(increment(5))
print(increment(3))
print(counter)

