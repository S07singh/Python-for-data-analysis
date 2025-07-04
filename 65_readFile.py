# Python reading files (.txt, .json, .csv)
'''
file_path = "output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")
'''

'''

import json
file_path = "output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
        # print(content["name"])
        # print(content["job"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")
'''
import csv
file_path = "output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            # print(line)
            # print(line[0])
            print(line[1])
            print(line[2])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")