def main():
    pace = get_pace(miles = 24.2, minutes = 0)
    print(f"You Need to Run each mile in {round(pace, 2)} Minutes. ")


def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError ("Value of Minutes Must Be Greater Than 0 ! Boom")
    return minutes / miles


main()
