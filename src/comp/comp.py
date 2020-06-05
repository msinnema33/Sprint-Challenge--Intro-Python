# The following list comprehension exercises will make use of the 
# defined Human class. 

import math

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [human.name for human in humans if human.name[0] == 'D']

# for h in humans:
#     if h.name[0] == 'D':
#         d.append(h.name)

print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [human.name for human in humans if human.name[-1] == 'e']

# for h in humans:
#     if h.name[-1] == 'e':
#         e.append(h.name)

print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
# c = [human.name for human in humans if human.name[0] == 'C' or 'D' or 'E' or 'F' or 'G']
incl = ('C', 'D', 'E', 'F', 'G')
# c = [human.name for human in humans if human.name[0] in incl] #range only works with int
c = [human.name for human in humans if human.name[0]  > 'B' and human.name[0]< 'H']

# for h in humans:
#     if h.name[0] in ['C', 'D', 'E', 'F', 'G']:
#         c.append(h.name)

print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [human.age + 10 for human in humans]

# for h in humans:
#     a.append(h.age + 10)

print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f'{human.name}-{human.age}' for human in humans]

# for h in humans:
#     e.append(f'{h.name}-{h.age}')

print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(human.name, human.age) for human in humans if human.age >= 27 and human.age <= 32]

# for h in humans:
#     if h.age >= 27 and h.age <= 32:
#         n.append((str(h.name), h.age))

print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(human.name.upper(), human.age + 5) for human in humans]

# for h in humans:
#     u.append(Human(h.name.upper(), h.age + 5))

print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
h = [math.sqrt(human.age) for human in humans]

# for h in humans:
#     sr.append(math.sqrt(h.age))

print(h)
