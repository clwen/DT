import csv
import pylab

filename = 'inertia.csv'
csv_reader = csv.reader(open(filename))
clusters = []
inertias = []
for line in csv_reader:
    clusters.append(line[0])
    inertias.append(line[1])
print clusters
print inertias

pylab.plot(clusters, inertias)
pylab.savefig('output.png')
pylab.show()
