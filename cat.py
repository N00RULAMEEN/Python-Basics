
"""
x = 4 
while x != 0:
    print("Meow")
    x -= 1
"""

"""
x = 4 
while x != 0:
    print("Meow")
    x = x - 1
"""

"""
x = 0
while x < 3:
    print("Meow")
    x = x + 1
"""
"""    
x = 4 
while x != 0:
    print("Meow")
    x += 1

"""
"""
for x in [0, 1, 2]:
    print("Meow")

"""
"""
# use _ if not variable declared also cariable could be used without declaring 
for _ in range(3):
    print("MEOWWW")
    """
"""
print("\nMeow" * 3, end="")

"""
"""
while True:
    n = int(input("What's n ?"))
    if n > 0:
        break

for _ in range(n):
    print("Meow")    

"""
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's N : "))
        if n > 0:
             return n

def meow(n):
    for _ in range (n):
        print("meow")
main()




