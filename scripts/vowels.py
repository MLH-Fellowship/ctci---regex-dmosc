import csv
import re

with open("./inputs/vowels.txt") as file:
    text = "".join(file.readlines())
    word_pattern = re.compile("[AaEeIiOoUu]")
    words = word_pattern.findall(text)
    vowel_count = len(words)
    with open(f"./outputs/vowels-{vowel_count}.txt", "w") as out_file:
        for word in text.split(" "):
            out_file.write(f"{word} ")
