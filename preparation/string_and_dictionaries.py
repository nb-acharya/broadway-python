print("-----------Strings and dictionaries-------------")

# strings are sequence of characters stored in memory

x = "Artemis is right now doing something"
y = 'Artemis is right now doing something'

print(x == y)

print("*****OPERATIONS IN STRING*****")
print("indexing")
planet = "Mercury"

print(planet[0])

print("looping in string")
given_string_1 = "broadwayinfosys"
print([char+'!' for char in given_string_1])

# print("experiment 1")
# given_string_2 = "niroj"
# given_string_2[0] = "c"
# print(given_string_2)


print("*****string methods*****")
string_1 = "niroj"
print(string_1.upper())
print(string_1)


# Text colors
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"
RESET   = "\033[0m"

print(RED + "Error!" + RESET)
print(GREEN + "Success!" + RESET)
print(YELLOW + "Warning!" + RESET)


BOLD      = "\033[1m"
UNDERLINE = "\033[4m"
DIM       = "\033[2m"

print(BOLD + "Important!" + RESET)
print(UNDERLINE + "Heading" + RESET)


CYAN  = "\033[36m"
GREEN = "\033[32m"
BOLD  = "\033[1m"
RESET = "\033[0m"

print(BOLD + CYAN + "┌" + "─"*15 + "┬" + "─"*7 + "┬" + "─"*15 + "┐" + RESET)
print(BOLD + CYAN + f"│ {'Name':<14}│ {'Age':<6}│ {'City':<14}│" + RESET)
print(BOLD + CYAN + "├" + "─"*15 + "┼" + "─"*7 + "┼" + "─"*15 + "┤" + RESET)
print(f"│ {GREEN}{'Alice':<14}{RESET}│ {25:<6}│ {'Kathmandu':<14}│")
print(f"│ {GREEN}{'Bob':<14}{RESET}│ {30:<6}│ {'Pokhara':<14}│")
print(BOLD + CYAN + "└" + "─"*15 + "┴" + "─"*7 + "┴" + "─"*15 + "┘" + RESET)