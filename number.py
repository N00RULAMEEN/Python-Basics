print("Welcome To Expections sessions")

"""
    try:
        x = int(input("What's 'X' : "))
    except ValueError:
        print("X is Not Intiger")
        print(f" x is {x}")  
    else:
        break

     many wrong correct it all   

"""

"""
print("Welcome To Exceptions session")

while True:
    try:
        x = int(input("What's X: "))
    except ValueError:
        print("X is not an integer")
    else:
        print(f"X is {x}")
        break
"""

def main():
    x = get_int("What's X? : ")
    print(f"x is {x}")



def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()