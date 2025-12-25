def main():
    pace = get_pace(miles = 24.2, Minutes = 180)
    print(f"You Need to Run each mile in {round(pace, 2)} Minutes. ")


def get_pace(miles, minutes):

    return minutes / miles

main()
