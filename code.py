import re

def main():
    code = input("Hexadecimal Color Code : ")

    pattern = r"^#[a-fA-F0-9]{6}$"
    match = re.search(pattern , code)
    if match:
        print(f"Valid Matched With {match.group()}")
    else:
        print("Invalid Code ")    


main()        