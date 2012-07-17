import csv
import numpy
from scipy.spatial import distance
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

# load demo data
demo_reader = csv.reader(open('demographic/2011_demo.csv'))
demos = []
for row in demo_reader:
    d = [int(field) for field in row]
    demos.append(d)

# load attendance data
# att_reader = csv.reader(open('demographic/2011_att.csv'))
# attendances = []
# for row in att_reader:
#     a = [int(field) for field in row]
#     attendances.append(a)
# 
# assert(len(demos) == len(attendances))
# demo_att = [demos[i] + attendances[i] for i in range(len(demos))]

da_array = numpy.array(demos)
# conduct kmeans clustering
for n_clusters in range(1, 21):
    k_means = KMeans(k=n_clusters)
    k_means.fit(da_array)
    labels = k_means.labels_
    centers = k_means.cluster_centers_
    inertia = k_means.inertia_
    print '%s, %s' % (n_clusters, inertia)
    # create a list of list, each list contains items match to label l
    groups = [[] for i in range(n_clusters)]
    # append da_array to groups according to label
    for i in range(len(labels)):
        label = labels[i]
        groups[label].append(da_array[i])
    # output the groups to file
    for i in range(n_clusters):
        output_file = 'clustering/%s.txt' % i
        numpy.savetxt(output_file, groups[i], fmt='%1d', delimiter=',')

# # conduct dbscan clustering
# D = distance.squareform(distance.pdist(da_array)) # distance
# S = 1 - (D / numpy.max(D)) # similarity
# db = DBSCAN().fit(S, eps=0.95, min_samples=5)
# labels = db.labels_
# label_list = []
# for label in labels:
#     l = int(label)
#     if l not in label_list:
#         label_list.append(l)
#     print label,
# label_list.sort()
# print label_list
# if label_list[0] == -1: # if noise presents, remove it from list
#     label_list = label_list[1:]
# print label_list
# # create a list of list, each list contains items match to label l
# groups = [[] for i in range(len(label_list))]
# # traverse labels again, append da_array according to label
# for i in range(len(labels)):
#     l = int(labels[i])
#     groups[l].append(da_array[i])
# # output the groups to file
# for i in range(len(groups)):
#     output_file = 'clustering/%s.txt' % i
#     numpy.savetxt(output_file, groups[i], fmt='%1d', delimiter=',')
