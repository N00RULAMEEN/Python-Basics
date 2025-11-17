
def main():
    difficulty = input("Difficult or Casual? ").strip().title()
    if not(difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return
    players = input("Multiplayer or Single-Player? ").strip().title()
    if not(players == "Multiplayer" or players == "Single-Player"): 
        print("Enter a valid number of players")
        return
    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        else:
            recommend("Klondike")
    else:
        if players == "Multiplayer":
            recommend("Hearts")
        else:
            recommend("Clock")  
def recommend(game):
    print("You should try playing " + game + "!")
    print("It's a great game!")
    print("Have fun!")

main()

    
    