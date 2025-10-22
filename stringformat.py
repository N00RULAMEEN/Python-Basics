# HERE WE CHECKING HOW IS A PROPER STIRNG FORMATION IS DONE IN  PYHTON 
# SO UNDERSCORES < CAPITALAZIATION ETC >>>>


shows = [
    "Do Yu Think Yu Won ",
    "Or SucCeeded",
    "Think Everything is from almighty ",
    "first to my self",
    "Develop Your Self"

]
"""

def main():
    for show in shows:
        print(show)
        #print(show.calpitalze())
        #print(show.title())
        #print(show.strip())
        #print(show.strip().title())
"""
"""
But let's say I want to put them in a new list.
I'll do just that here.
I'll do cleaned-shows is first an empty list.
And I'll then append.
I'll append each new string to, in this case, my cleaned_shows list.
Now, if I go down below and print cleaned_shows,
I should see, fingers crossed, a new list of shows,
in this case ones that are appropriately title cased and also removed
of their leading and trailing whitespace.
"""
"""
def main():
    cleaned_SHOWS = []
    for show in shows:
        cleaned_SHOWS.append(show.strip().title())

        print(cleaned_SHOWS)
        #print(show.calpitalze())
        #print(show.title())
        #print(show.strip())
        #print(show.strip().title())
        """
def main():
    cleaned_SHOWS = []
    for show in shows:
        cleaned_SHOWS.append(show.strip().title())

    print(' '.join(cleaned_SHOWS))
    # if yu just added more tab\ space it will goes to under append means becomes for loop 
        
main()
