import csv
import numpy
import math
from scipy.spatial import distance
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

# nominal fields: resort (3), country (7)
nominal_fields = [3, 7]

def demo_distance(vec1, vec2):
    assert len(vec1) == len(vec2)
    s = 0.0
    for i in range(len(vec1)):
        if i in nominal_fields:
            s += 1.0 if vec1[i] != vec2[i] else 0.0
        s += pow((vec1[i] - vec2[i]), 2)
    s = math.sqrt(s)
    return s

if __name__ == '__main__':
    # load demo data
    demo_reader = csv.reader(open('demographic/2011_demo.csv'))
    demos = []
    for row in demo_reader:
        d = [float(field) for field in row]
        demos.append(d)
    da_array = numpy.array(demos)
    print da_array.shape

    # load attendance data
    # att_reader = csv.reader(open('demographic/2011_att.csv'))
    # attendances = []
    # for row in att_reader:
    #     a = [int(field) for field in row]
    #     attendances.append(a)
    # 
    # assert(len(demos) == len(attendances))
    # demo_att = [demos[i] + attendances[i] for i in range(len(demos))]

    # n_clusters = 6
    # # conduct kmeans clustering
    # k_means = KMeans(k=n_clusters)
    # k_means.fit(da_array)
    # labels = k_means.labels_
    # centers = k_means.cluster_centers_
    # inertia = k_means.inertia_
    # print '%s, %s' % (n_clusters, inertia)
    # # create a list of list, each list contains items match to label l
    # groups = [[] for i in range(n_clusters)]
    # # append da_array to groups according to label
    # for i in range(len(labels)):
    #     label = labels[i]
    #     groups[label].append(da_array[i])
    # # output the groups to file
    # for i in range(n_clusters):
    #     output_file = 'clustering/%s.txt' % i
    #     numpy.savetxt(output_file, groups[i], fmt='%3.3f', delimiter=',')

    # conduct dbscan clustering
    # D2 = distance.squareform(distance.pdist(da_array)) # distance
    # initialize D: matrix n by n where n is number of row in test data
    n = len(da_array)
    D = [[0.0 for i in range(n)] for j in range(n)]
    D = numpy.array(D)
    for i in range(n):
        for j in range(n):
            print i, j
            D[i][j] = demo_distance(da_array[i], da_array[j])
    S = 1 - (D / numpy.max(D)) # similarity
    print S
    db = DBSCAN().fit(S, eps=0.95, min_samples=20)
    labels = db.labels_
    label_list = []
    for label in labels:
        l = int(label)
        if l not in label_list:
            label_list.append(l)
        print label,
    label_list.sort()
    print label_list
    if label_list[0] == -1: # if noise presents, remove it from list
        label_list = label_list[1:]
    print label_list
    # create a list of list, each list contains items match to label l
    groups = [[] for i in range(len(label_list))]
    # traverse labels again, append da_array according to label
    for i in range(len(labels)):
        l = int(labels[i])
        groups[l].append(da_array[i])
    # output the groups to file
    for i in range(len(groups)):
        output_file = 'clustering/%s.txt' % i
        numpy.savetxt(output_file, groups[i], fmt='%1d', delimiter=',')
