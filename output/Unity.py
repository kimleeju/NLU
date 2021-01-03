import csv
import os
 
os.chdir("/home/oslab/nlu/output")
 
category = ['정치','사회','생활문화','IT과학', '경제']
 
file_unity = open('Article_unity.csv', 'w', encoding='utf-8')
wcsv = csv.writer(file_unity)
 
count = 0
 
for category_element in category:
    file = open('Article_'+category_element+'_201701_201701.csv', 'r', encoding='utf-8', newline="")
    line = csv.reader(file)
    try:
        for line_text in line:
            wcsv.writerow([line_text[0], line_text[1], line_text[2], line_text[3]])
    except:
        pass
 
