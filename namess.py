import csv

name = input("What's your name? ")
home = input("Where's your Home? ")


with open("Students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "home"])
    writer.writerow({"name": name, "home" :home})


"""
import csv

students = []

with open("namess.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name" :row["name"], "home": row["home"]})

for student in sorted(students, key = lambda student: student["name"], reverse= True):
    print(f"{student['name']} is from {student['home']}")  

"""
"""
import csv

students = []

with open("namess.csv") as file:
    reader = csv.reader(file)
    for name,home in reader:
        students.append({"name" : name, "home": home})

for student in sorted(students, key = lambda student: student["name"], reverse= True):
    print(f"{student['name']} is from {student['home']}")  

"""
"""
students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student) 

for student in sorted(students, key = lambda student: student["name"], reverse= True):
    print(f"{student['name']} is on {student['house']}")      
      """

"""
students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student)

def get_name(student):
    return student["name"]        

for student in sorted(students, key = get_name, reverse= True):
    print(f"{student['name']} is on {student['house']}")        

# To Reverse House 
#def get_House(student):
 #   return student["house"]        

#for student in sorted(students, key = get_House, reverse= True):
 #   print(f"{student['name']} is on {student['house']}")        

"""
"""
students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house" : house}
        students.append(student)

for student in students:
    print(f"{student['name']} is on {student['house']}")        

"""
"""
students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is on {student['house']}")        

"""

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