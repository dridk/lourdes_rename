import os 
import pathlib
import re 
EXTENSION = ["fastq","bam"]
RENAME = True


# Read map 
mapping = {}
with open("map.txt") as file:
    for line in file:
        value, key = tuple(line.strip().split(","))
        mapping[key] = value 
print(mapping)

# Loop all file recursively .. 
data_path = pathlib.Path("data/")

files = []
for extension in EXTENSION:
    files += data_path.rglob(f"*.{extension}")

for file in files:
    file = str(file)
    name = os.path.basename(file)
    
    for key in mapping.keys():
        if re.match(rf"{key}\..+", name):
            value = mapping[key]
            new_file = file.replace(key,value)

            print(f"{file} ==> {new_file}")

            if RENAME:
                os.rename(file, new_file)


