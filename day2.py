#Data types and variables
"""
    string
    integer
    float
    compplex
    boolean
    None  -> doesnt occupy any memory  !! more info needed
"""

a = 10
print(type(a))

b = "10"
print(type(b))

c = 10.44
print(type(c))

d = "PROGRESS"
print(type(d))

e = 3+4j
print(type(e))

f = None
print(type(f))

# arithmetic operations

a = 15
b = 4
print(a+b)
print(a-b)
print(a/b)
print(a // b)   #nearest low whole number, it doesn't round
print(a % b)
print(a ** b)

print("niroj" + "bajracharya")  # two strings are added then it is concatenated

first_name = "Hari"
second_name = "Sharma"

output = first_name + " " + second_name
print(output)

first = 23
second = "asdf"

first_name_v2 = "Kim"
value = 5

print(first_name_v2 * value)

#type casting
a  = "10"
a = int(a)
print(type(a))

# c = "11.98"
# c = int(c)
# print(type(c))

new_1 = "10"
print(new_1)
print(str(new_1))

new_2 = True
print(new_2)
print(int(new_2))

new_3 = False
print(new_3)
print(int(new_3))

# True -> 1, False -> 0
print("----------------")

new_4 = 123.2323
print(bool(new_4))


print("----classroom activity-------")

x1 = int("5")
y1 = float("3.14")
z1 = str(100)

print(type(x1),type(y1),type(z1))

#type checking
print(isinstance(x1,int)) # True
















