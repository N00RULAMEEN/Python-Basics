WORDS = { "Pair" : 4, "HAIR": 4, "CHAIR" : 5 , "GRAPHIC" : 7}


"""
def main():
    print("Welcome To Spelling Bee")
    print("Your letters are : A I P C R H G")

    
    while len(WORDS) > 0:
        print(f"{len(WORDS)} Words left !")
        guess = input("Guess the Answers : \t")


        #TODO
        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good JOB ! YOU SCORED {points} points. ")

        print("That's The Game")    
main()

"""
"""
def main():
    
    print("Welcome To Spelling Bee ")
    print("Your Letters are : A I P C R H G ")


    while len(WORDS) > 0:
        print(f"{len(WORDS)} WORDS LEFT ! ")
        guess = input("Guess The Ansers :\t")



    if guess == "GRAPHIC":
        WORDS.clear()
        print("YU HAVE WON! ")
    if guess in WORDS.keys():
        points = WORDS.pop(guess)
        print(f"GOOD JOB YU HAVE SCORED {points} points. \n")
    else:
        print("WRONG ANSWER TRY AGAIN")    


    print("That's The Game")

main()            

    """

def main():
    
    print("Welcome To Spelling Bee ")
    print("Your Letters are : A I P C R H G ")

    for WORD, points in WORDS.items():
        print(f"{WORD} WAS WORTH {points} points.")

main()            