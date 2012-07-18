import csv

csv_reader = csv.reader(open('2011_demo.csv'))
lines = list(csv_reader)
max_list = [0 for i in range(len(lines[1]))]

# first pass: get info for max list
for line in lines:
    # for each field, if it's bigger than current value, update the max list
    assert len(line) == len(max_list)
    for i in range(len(line)):
        if float(line[i]) > float(max_list[i]):
            max_list[i] = float(line[i])
print max_list

# second pass: divide all field by max value; also output to csv file
csv_writer = csv.writer(open('2011_demo_normalized.csv', 'w'))
for line in lines:
    for i in range(len(line)):
        line[i] = float(float(line[i]) / float(max_list[i])) if int(max_list[i]) != 0 else line[i] # avoid dividing by zero
    print line
    csv_writer.writerow(line)
