import csv

filename = '2011_demo.csv'
csv_reader = csv.reader(open(filename))
lines = list(csv_reader)
max_list = [0 for i in range(len(lines[1]))]
# first pass: get info for max list
for line in lines:
    # for each field, if it's bigger than current value, update the max list
    assert len(line) == len(max_list)
    for i in range(len(line)):
        if line[i] > max_list[i]:
            max_list[i] = line[i]
print max_list
# second pass:
for line in lines:
    for i in range(len(line)):
        line[i] = float(float(line[i]) / float(max_list[i])) if int(max_list[i]) != 0 else line[i] # avoid dividing by zero
    print line
