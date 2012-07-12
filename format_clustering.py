import csv

fields_reader = csv.reader(open('clustering/demo_fields.csv'))
fields = fields_reader.next() # only one line, actually
print ' '.join(fields)

cluster_reader = csv.reader(open('clustering/0.txt'))
for line in cluster_reader:
    for i in range(len(fields)):
        field_len = len(fields[i])
        print line[i].ljust(field_len),
    print ''
