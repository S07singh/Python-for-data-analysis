# Python writing files (.txt, .json, .csv)
# text
'''
employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
# txt_data = "I like pizza!"

file_path = "output.txt" # "C:/Users/sudhi/OneDrive/Desktop/output.txt" # relative path we can also use absolute path

try:
    # with open(file_path, "w") as file: # it override the content
    with open(file_path, "a") as file: # its append the data and add new text
    # with open(file_path, "x") as file: # "x" it creates file and then write if file is already exists it show error
    #     file.write(txt_data)
    #     file.write(employees) # we can make list in string. or
        for employee in employees:
            file.write(employee + " ")
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")
'''

'''
#json
import json
employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

file_path = "output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")
'''
import csv
import json
employees = [["Name", "Age", "Job"],
            ["Spongebob", 30, "Unemployed"],
            ["Patrick", 37, "Scientist"],
            ["Sandy", 27, "Cook"]]

file_path = "output.csv"
# file_path = "C:/Users/sudhi/OneDrive/Desktop/output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")