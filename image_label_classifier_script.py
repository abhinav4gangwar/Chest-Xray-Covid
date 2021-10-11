# importing csv module
import csv
import os
import shutil
  
# csv file name
filename = "metadata.csv"
  
# initializing the titles and rows list
fields = []
rows = []
  
# reading csv file
with open(filename, 'r', encoding = "utf8") as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
  
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
  


filename = []
result=[]
index = []

#  printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:]:
    # parsing each column of a row
    filename.append(row[23])
    result.append(row[4])

for i in range(len(result)):
    #print (i)
    if result[i] == 'Pneumonia/Viral/COVID-19':
        index.append(i)
covid_images = []
for i in index:
    covid_images.append(filename[i])
    


entries = os.listdir('raw_data/')

for entry in entries:
    if entry in covid_images:
        original = 'D:\\machine_learning_ex\\chest\\raw_data\\' + str(entry)
        target = 'D:\\machine_learning_ex\\chest\\2\\covid\\' + str(entry)
        shutil.copyfile(original, target)

    else :
        original = 'D:\\machine_learning_ex\\chest\\raw_data\\' + str(entry)
        target = 'D:\\machine_learning_ex\\chest\\2\\normal\\' + str(entry)
        shutil.copyfile(original, target)
        



 
