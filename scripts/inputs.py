import re
import os

from pathlib import Path

path = Path("inputs/split")
for filename in os.listdir(path):
    filepath = path/filename
    filename_noext = filename.split(".")[0]
    with open(filepath) as file:
        curr_file_i = 0
        chunk_file = open(path/f"{filename_noext}-{curr_file_i}.txt", "w")
        for word in " ".join(file).split(" "):
            if chunk_file.tell() > 500:
                chunk_file.close()
                curr_file_i += 1
                chunk_file = open(
                    path/f"{filename_noext}-{curr_file_i}.txt", "w")
            chunk_file.write(f"{word} ")
        chunk_file.close()
