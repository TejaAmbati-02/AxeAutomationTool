from selenium import webdriver
from axe_selenium_python import Axe
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import xlrd
import shutil
import os
import json
import csv

driver = webdriver.Chrome(ChromeDriverManager().install())
loc = ("aaa2797.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)

lis = []
for i in range(0, sheet.nrows):
	a = sheet.cell_value(i, 0)
	lis.append(a)

def test_google():
	count = 1
	for i in lis:
		driver.get(i)
		axe = Axe(driver)
		axe.inject()
		results = axe.run()
		axe.write_results(results, f'axeIntegration{count}{i[12:16]}.json')
		count+=1

	driver.close()
	# assert len(results["violations"]) == 0, axe.report(results["violations"])

test_google()

jsonfiles = os.listdir()
os.mkdir('json_files')

for jsonfile in jsonfiles:
	if jsonfile.endswith(".json") == True:
		new_path = 'json_files/' + jsonfile
		shutil.move(jsonfile, new_path)

csv_file = os.listdir('./json_files/')

for files in csv_file:
	print(files)
# 	with open(files) as json_file_to_csv:
# 		data = json.load(json_file_to_csv)
		
# 	json_data = data['violations']
# 	data_file = open(f'{files}.csv', 'w')
# 	csv_writer = csv.writer(data_file)
# 	count = 0

# 	for data in json_data:
# 		if count == 0:
# 			header = data.keys()
# 			csv_writer.writerow(header)
# 			count += 1

# 		csv_writer.writerow(data.values())

	data_file.close()
