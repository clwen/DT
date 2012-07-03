import csv
import numpy
from scipy.spatial import distance
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

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

da_array = numpy.array(demo_att)
print da_array
print type(da_array)
print da_array.shape

# conduct kmeans clustering
# k_means = KMeans(k=n_clusters)
# k_means.fit(da_array)
# k_means_labels = k_means.labels_
# k_means_cluster_centers = k_means.cluster_centers_
# print k_means_labels
# for l in k_means_labels:
#     print l,
# print k_means_cluster_centers

# conduct dbscan clustering
D = distance.squareform(distance.pdist(da_array)) # distance
S = 1 - (D / numpy.max(D)) # similarity
db = DBSCAN().fit(S, eps=0.95, min_samples=10)
labels = db.labels_
for label in labels:
    print label,
