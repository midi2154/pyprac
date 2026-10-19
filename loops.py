#for loop executes a block of code a fixed number of times.
#you ca iterate over a range, string, sequence, etc.

#x in this case is more like the counter
# continue skips over an iteration as giving in the example
#break stops it entirely

#for the third number in cases like(1, 10, 2) the 2 means step,
#  meaning it should count in twos 



#for loop
for x in range(1, 11, 2,):
    print(x)
print("happy new year")


for x in reversed(range(1, 11, 2,)):
    print(x)
print("happy new year")



for x in range(1, 30):
    if x == 13:
        continue
    else:
        print(x)

for x in range(1, 5):
    if x == 3:
        break
    print(x)


def hello():
    print ("hello")



#while loop
#Executes  some code WHILE some condition remain true.

#while loops are naturally infinite loops
#so you must insert a strategy to escape like in the
#example below we used  name = input("Enter your name ") if not it loops
#forever

name = input("Enter your name:")
while name =="":
    print("You did not enter your name")
    name = input("Enter your name ")
print(f"Hello {name}")

age = int(input("Enter your age"))

while age < 0:
    print("age cannot be negative")
    age = int(input("Enter your Age"))
print(f"{name} is {age} years old")


food = input("Enter a food you like(q to quit): ")

while not food == "q":
    print(f"you like {food}")
    food = input("Enter another food you like(q to quit): ")

print("bye")