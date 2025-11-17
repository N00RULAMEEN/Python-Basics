name = input("What's Your Name ? : ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryfindor")           
    case "Darco":
        print("Slytheryin")
    case _:
        print("Who ?") 

"""
match name:
    case "Harry":
        print("Gryfindor")
    case "Ron":
        print("Gryfindor")
    case "Hermione":
        print("Gryfindor")                
    case "Darco":
        print("Slytheryin")
    case _:
        print("Who ?")    
"""

"""
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryfindor")
elif name == "Darco":
    print("Slytherin")
else:
    print("Whom ? ")
"""
