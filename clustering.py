import csv
from numpy import *
from sklearn.cluster import KMeans

n_clusters = 5

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

da_array = array(demo_att)
print da_array
print type(da_array)
print da_array.shape

k_means = KMeans(k=n_clusters)
k_means.fit(da_array)
k_means_labels = k_means.labels_
k_means_cluster_centers = k_means.cluster_centers_
print k_means_labels
for l in k_means_labels:
    print l,
print k_means_cluster_centers
