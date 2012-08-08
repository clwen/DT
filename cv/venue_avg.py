import csv

# read name of venues

# read accuracies
acc_reader = csv.reader(open('svm.csv'))
lines = list(acc_reader)
n_venue = len(lines) # number of lines imply the number of venues
n_test = len(lines[0])
avgs = []
for line in lines:
    print line
    accs = [float(s) for s in line]
    avg = sum(accs) / len(accs)
    avgs.append(avg)
    print avg
