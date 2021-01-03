import csv
import random
import os
 
os.chdir("/home/oslab/nlu/output")
 
file = open('Article_unity.csv', 'r', encoding='utf-8')
line = file.readlines()
random.shuffle(line)
rcsv = csv.reader(line)
 
file_write = open('Article_shuffled.csv', 'w', encoding='utf-8', newline="")
wcsv = csv.writer(file_write)
 
for i in rcsv:
    try:
        wcsv.writerow([i[0].strip(), i[1], i[2], i[3]])
    except:
        pass 
