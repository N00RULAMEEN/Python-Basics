# function-based program
# The “system” your code uses is function definition and calling,
# and the style is called procedural or functional programming.

"""

emoticon = "v.v"

def main():
    say("Is There Any One")
    say("Is it")

def say(phrase):
        print(phrase + " " + emoticon)




main()
"""

# ANOTHER WAY

emoticon = "v.v"

def main():
    global emoticon
    say("Is There Any One")
    name = input("pleas Name :\t")
    emoticon = name
    say("Is it")

def say(phrase):
        print(phrase + " " + emoticon)




main()





"""
Step-by-Step Explanation

emoticon = "v.v"
→ This creates a global variable named emoticon with the string "v.v".

def main():
→ Defines a function called main.
Inside main, you call another function named say() twice:

say("Is There Any One")

say("Is it")

def say(phrase):
→ Defines another function that takes one argument called phrase.
Inside, it prints the phrase plus a space and the emoticon.

So effectively:

If phrase = "Is There Any One", it prints "Is There Any One v.v"

If phrase = "Is it", it prints "Is it v.v"

main()
→ This line calls the main function to start the program.
"""