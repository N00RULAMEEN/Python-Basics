import re

email = input("What's Your Email Id : ").strip()


# if re.search(r"^.+@.+\.edu$", email):     
# if re.search(r"^[^@]+@[^@]+\.edu$", email):     
# if re.search(r".*@.*", email):  
# if re.search(r"[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#if re.search(r"^\w+@\w+\.edu$", email):    
#if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
#if re.search(r"^\w+@\w+\.\w+\.edu$", email, re.IGNORECASE):    # doenst work in only 1 dot 
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):

    print("valid")
else:
    print("Invalid")   


"""
email = input("What's Your Email Id : ").strip()

if re.search(".+@.+\.edu",email):
        
        print("valid")
else:
    print("Invalid")   
# Here Only Isue You could type .edu anywhere to prenvent
# it add ^ in begning $ and in end
#  Next Problem Above
    """
"""
email = input("What's Your Name : ").strip()

username, domain = email.split("@")


if username and domain.endswith(".edu"):
    print("valid")
else:
    print("Invalid")   
"""

"""
email = input("What's Your Name : ").strip()

if "@" in email and "." in email:
    print("valid")
else:
    print("Invalid")    
    """

#Here is the content from the image converted to clear, readable text:
'''

| Regex | Meaning                                                 |
|-------|---------------------------------------------------------|
| \d    | decimal digit                                           |
| \D    | not a decimal digit                                     |
| \s    | whitespace characters                                   |
| \S    | not a whitespace character                              |
| \w    | word character ... as well as numbers and the underscore|
| \W    | not a word character                                    |

Here is the content from the image converted to clear, readable text:

| Regex       | Meaning                  |
|-------------|--------------------------|
| .           | any character except a newline |
| *           | 0 or more repetitions   |
| +           | 1 or more repetitions   |
| ?           | 0 or 1 repetition       |
| {n}         | n repetitions           |
| {m,n}       | m–n repetitions         |

'''