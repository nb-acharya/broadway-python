#operators

print(2.0 == 2) #result is True

# ==,<,<=,>,>=

print("------------comparison operators--------------")
#examples of comparison operators
a = 21
b = "Random"
c = False

print(21 == a)
print("random" != b)
print(True != c)

#logical operators (and,or,not)
#use case -> traffic light, electrical circuit

# and examples
print("-------logical operators---------")
age = 20
is_citizen = True
print(age>=18 and is_citizen)

is_weekend = False
is_holiday = True
print(is_weekend or is_holiday)

logged_in = False
print( not logged_in)

# print("-------------input function---------------------")
# print("Entered value from user will always be in string")
# a = input("enter a value: ")
# print("Entered number is",a, "and its type is", type(a))
# input("PRESS ANY KEY TO CONVERT TO INTEGER AND PRESS ENTER: ")
# print(a := int(a),"now the type is changed", type(a))


# print("-------------------task given-----------------")
# name = "Suman"
# age = 14
# address = "nepal"

# print("my name is" , name , "my age is" , age , "i live in" , address)
# output = f'my name is {name}. my age is {age}. I live in {address}'
# print(output)

#if condition
# print("-----------if condition---------------")

# if(1 == 1 and "Ram" == "Ram"):
#     print("I am ok")
# else:
#     print("I am not ok")


print("----------check odd or even---------------")
number = input("Enter your number: ")

if(isinstance(number,int)):

    if(number % 2 == 0):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

else:
    print("Please enter a valid number")





