import csv

filename = '2011_demo.csv'
csv_reader = csv.reader(open(filename))
for line in csv_reader:
    print line
