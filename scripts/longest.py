import csv
import re

with open("./inputs/longest.txt") as file:
    with open("./outputs/longest.txt", "w") as out_file:
        word_pattern = re.compile("\w+")
        words = word_pattern.findall("".join(file.readlines()))
        longest_word = max(words, key=lambda word: len(word))
        longest_length = len(longest_word)

        for word in words:
            if len(word) == longest_length:
                out_file.write(f"**{word}** ")
            else:
                out_file.write(f"{word} ")
