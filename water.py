from soil import sample

def main():
    moisture = sample()
    days = +1
    print(f"Day {days}: Moisture is {moisture}% .")


    while moisture > 20:
               
        moisture = sample()
        days += 1
        print(f"Day {days}: Moisture is {moisture} %.")



    if moisture <5 : 
        print("The Plant Dead -_- Plant New ")
    elif moisture < 10:
        print("Plant is almost Dying Water bit by bit")
    else:            
        print(f"Time to Water ! .")


main()

