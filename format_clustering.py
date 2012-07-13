import csv
import os
import random

fields_reader = csv.reader(open('clustering/demo_fields.csv'))
fields = fields_reader.next() # only one line, actually
print ' '.join(fields)

# get all filename under clustering folder
cluster_files = [f for f in os.listdir('clustering/') if f.endswith('.txt')]

# for each file, choose randomly 15 lines to print
for cf in cluster_files:
    filename = 'clustering/' + cf
    with open(filename) as f: 
        csv_reader = csv.reader(f)
        items = list(csv_reader)
        random.shuffle(items)
        items = items[:15]
        for item in items:
            for i in range(len(fields)):
                field_len = len(fields[i])
                print item[i].ljust(field_len),
            print ''
    # between each cluster, print blank lines to seperate
    print '\n\n\n'
