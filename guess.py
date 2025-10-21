'''
 OK, now here, we're going
to take a look at one other building block of our programs.
In this case, variables.
And variables are simply containers for some value that can change over time.
So let's say I want to make a guessing game, where
the user can guess some number.
And I'll tell them if they guessed correctly or incorrectly.
Now, it would be probably worthwhile to have some way of referring
to the user's guess in my program.
What number did they guess?
And that is a great use case for a variable.
So I want to make a variable in Python.
Now, I'll say python of guess.py, and I should see 10 printed back out to me
on the screen.
Now, variables come-- really powerful when we combine them
with things like functions.like above
'''

"""

def getguess():
    guess = input("Enter A Guess\t:")
    return guess


print(getguess())

"""


'''
guess = 10 
print(guess)
'''

def get_guess():
    guess = int(input("Enter A Guess \t:"))
    return guess

def main():
    guess = get_guess()
    if guess >= 50:
            print("Correct")
    else:
            print("Very Wrong")

main()











