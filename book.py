
def main():
    with open("alice.txt", "r", encoding="utf8") as f:
        content = f.readlines()

    chapter1 = content[53:212]
    with open("chapter1.txt", "w", encoding="utf8") as file:
        file.writelines(chapter1)

main()    


"""
def main():
    with open("alice.txt", "r", encoding="utf8") as f:
        content = f.readlines()

    chapter1 = content[53:212]
    print(chapter1)

main()    

"""

"""
def main():
    with open("alice.txt", "r", encoding="utf8") as f:
        content = f.readlines()


    print(content)

main()    
"""