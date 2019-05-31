import csv, os
from collections import Counter
finallist = []
inputdir = 'input/'
#csvfiles = ['a.csv','b.csv','c.csv','d.csv','e.csv','f.csv','g.csv','h.csv']

for file in os.listdir('input'):
    with open(inputdir+file, encoding='utf8') as collection:
        reader =csv.DictReader(collection )
        for row in reader:
            finallist.append(row['dc.type'])
            finallist.append(row['dc.type[]']) 
            finallist.append(row['dc.type[en]'])

tally = Counter(finallist)

for type in tally:
    print(type, tally[type])
