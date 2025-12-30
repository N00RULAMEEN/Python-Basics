



"""
students = []

with open("names.csv") as file:
    for line in file:
       name,house = line.rstrip().split(",")
       students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
    """

"""
with open("names.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

"""
"""
names = []
with open("names.csv") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names , reverse=True):
    print(f" Hello, {name}")
"""

"""
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f" Hello, {name}")

"""

"""
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello", line.rstrip())

"""

"""
name = input("What's Yur Name :")

file = open("names.txt","a")
file.write(f"{name}\n")
file.close()

"""
"""
name = input("What's Yur Name :")

# file = open("names.txt","w") only writes next time forgets 
file = open("names.txt","a")
file.write(name)
file.close()

"""

"""
names = []


for _ in range(3):
    names.append(input("What's Yur Name : "))

for name in sorted(names):    
    print(f" HI, {name}")

"""
"""
name = input("What's Yur Name : ")
print(f" HI, {name}")
"""