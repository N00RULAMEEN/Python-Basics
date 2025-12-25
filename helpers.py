def get_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read().lower()
        words = text.split()
    return words


def save_counts(counts):
    for word, count in counts.items():
        print(word, count)
import csv

def save_counts(counts):
    with open("counts.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["word", "count"])   # header

        for word, count in counts.items():
            writer.writerow([word, count])
