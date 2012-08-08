import csv
import os
from pprint import pprint

# read name of venues
names = [s[4:-4] for s in os.listdir('../GeoFences/15M') if s.endswith('.mif')]
names = [name.replace('&', '\\&') for name in names] # replace & for latex usage
names = [name.replace('\'', '\\\'') for name in names] # replace ' for latex usage

# read accuracies
acc_reader = csv.reader(open('svm.csv'))
lines = list(acc_reader)
n_venue = len(lines) # number of lines imply the number of venues
n_test = len(lines[0])
avgs = []
for line in lines:
    accs = [float(s) for s in line]
    avg = sum(accs) / len(accs)
    avg = str(avg * 100) + '\%'
    avgs.append(avg)

# print formatted output
assert len(names) == len(avgs)
for i in range(n_venue):
    print '%s & %s \\\\ \\hline' % (names[i], avgs[i])
