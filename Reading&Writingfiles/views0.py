import csv
import numpy as np
from PIL import Image

def main(): 
    with open("views.csv", "r", encoding="utf-8") as views, open("Analysis.csv", "w",encoding="utf-8") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames +["brightness"])
        writer.writeheader()
        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            row["brightness"] = round(calculate_brightness(f"{row['id']}.jpeg"),2)
            writer.writerow(row)
            
            print(round(brightness, 2))

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness

main() 

"""
def main(): 
    with open("views.csv", "r", encoding="utf-8") as views, open("Analysis.csv", "w",encoding="utf-8") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames +["brightness"])
        writer.writeheader()
        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            writer.writerow({
                    "id": row["id"],
                    "english_title": row["english_title"],
                    "japanese_title": row["japanese_title"],
                    "brightness": round(brightness, 2),
                            })
            
            print(round(brightness, 2))

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness

main() 

"""
"""
def main(): 
    with open("views.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            print(round(brightness,2))

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()            

"""

"""
def main(): 
    with open("views.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["id"])

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()

"""
"""
    with open("views.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)



def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()
  """