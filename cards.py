import random

cards = ["jack", "Queen", "King"]


def main():
    random.seed(0)
   # print(random.sample(cards, k=2))
    print(random.choices(cards, k=2))  
   #  print(random.choices(cards, k=2))  
   # this will get queen queen but in smaple nope 
   # print(random.choices(cards, weights=[1, 0.9, 0.9], k = 2))

main()