import os
import json
import csv
import shutil

for files in os.listdir():
    if(files.endswith(".json")):
        with open(files) as json_file:
            data = json.load(json_file)
            json_data = data['violations']
            data_file = open(f'data_file{files}.csv', 'w')
            csv_writer = csv.writer(data_file)

        count = 0
        for emp in json_data:
            if count == 0:
                header = emp.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(emp.values())
data_file.close()

os.mkdir("csv_files")
for file in os.listdir():
    if file.endswith(".csv"):
            new_path = 'csv_files/' + file
            shutil.move(file, new_path)
