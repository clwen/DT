import csv

# load demo data
demo_reader = csv.reader(open('demographic/2011_demo.csv'))
demos = []
for row in demo_reader:
    d = [int(field) for field in row]
    demos.append(d)

# load attendance data
att_reader = csv.reader(open('demographic/2011_att.csv'))
attendances = []
for row in att_reader:
    a = [int(field) for field in row]
    attendances.append(a)

assert(len(demos) == len(attendances))
demo_att = [demos[i] + attendances[i] for i in range(len(demos))]

