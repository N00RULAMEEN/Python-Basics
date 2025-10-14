#In this learn to print 
#learn input & output
#learn to remove string Space
#learn to capitaliaze first letter /last letter /completely small/completely Capital/
# Split users name into last and first

"""
This is my First Programme under David J Milan
"""
#This and above is an comment
name = input ("What's Your Name : ").strip().title()
# Split users name into last and first
first , last = name.split(" ")
print(f"Hello, {first}")
print(f"{last}")

"""
name = input ("What's Your Name : ")
print(f"Hello,  {name}")
# so printing this makes a lot of space
"""
"""
# space in string 
# To remove it 
# After input only you ould modify input

name = input ("What's Your Name : ")
name = name.strip()
name = name.title()
# you could join the space and capitilazation as this
# name = name.strip().title()
# or in one line
#name = input ("What's Your Name : ").strip().title()

print(f"Hello, {name}")

"""
"""
# using sep //
# When you want to change or remove the separator between values

name= input("Whom Are You ? :")
#print("Hello ",end ="")
print("Hello ",name, sep ="")
"""
"""

# using end //
# When you want to continue printing on the same line

name= input("Whom You Are?")
print("Hello ",end ="")
print(name)
"""
"""
print("Your Name ?")
name = input(":" )
print("It's Me",name)
"""
"""
If yu want input and output in one line 
name = input(":" )
print("It's Me")
print(name)

"""