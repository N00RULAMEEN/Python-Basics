Distances = {
    "Voyager 1": 22263,
    "Voyager 2": 1423,
    "Voyager 3": 42443,
    "Voyager 4": 944453,
    "Voyager 5": 37432,
    "Voyager 6": 3233,
    "Voyager 7": 233
}

def main():
    '''
    for name in Distances.keys():
        print(f"{name} is {Distances [name] } AU From Earth")
              '''
    
    for Distance in Distances.values():
        print(f"{Distance} AU is {convert(Distance)} m")

def convert(au):
    return au * 149597870700
main()              
