"""
for _ in range(3):
    print("#")
print("#")
print("#")
print("#")

"""
"""
def main():
    print_column(9)

def print_column(height):
    for _ in range(height):
        print("#")
        

main()        

    """
"""
def main():
    print_column(3)

def print_column(height):
   print("#\n" * height, end="")
        

main()        

"""
"""

def main():
    print_row(4)

def print_row(width) :
    print("?" * width)

main()        

"""
"""
def main():
    print_square(3)

def print_square(size):

    #Row 
    for i in range(size):
        # Brick in row
        for j in range(size):

             print("&", end="")   
        print()     


main()        
"""

"""
def main():
    print_square(3)

def print_square(size):

    #Row 
    for i in range(size):
       print("$" * size)
main()     

"""

def main():
    print_square(3)

def print_square(size):

    #Row 
    for i in range(size):
        print_row(size)
def print_row(width):
    print("&" * width)       


main()        