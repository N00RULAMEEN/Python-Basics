import re


"""
name = input("What's your name? ").strip()

if matches := re.search(r"^(.+), *(.+)$", name):
            name = matches.group(2) + " " + matches.group(1)       
print(f"hello, {name}")

"""
"""
name = input("What's your name? ").strip()

matches = re.search(r"^(.+), *(.+)$", name)

if matches :
        name = matches.group(2) + " " + matches.group(1)
        ...
print(f"hello, {name}")

"""
"""
name = input("What's your name? ").strip()

matches = re.search(r"^(.+), (.+)$", name)

if matches :
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
print(f"hello, {name}")

"""

"""
name = input("What's your name? ").strip()

matches = re.search(r"^(.+), (.+)$", name)

if matches :
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"hello, {name}")
"""


"""
name = input("What's your name? ").strip()

if " " in name:
    first, last = name.split(" ", 1)
    name = f"{first} {last}"

print(f"hello, {name}")

"""


# A | B
# means: match either A or B

# ( ... )
# means: grouping part of the regex
# used to apply +, *, ? to multiple characters

# (?: ... )
# means: non-capturing group
# used for grouping without storing the match
