def print_me():
    print("Welcome to our Action Game 2025")
    print("Follow The Rules To Win")
    return main()

def main():


    history = []

    while True:
        action = input("Action :")


        if action == "Undo":
            undone = history.pop()
            print(f"Undone :  {undone}")
            print(history)    
        elif action == "restart":
            history.clear()
            print("Cleared")
            return print_me()
        else:
            history.append(action)
            print(history)


main()