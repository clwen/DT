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
        else:
            s += pow((vec1[i] - vec2[i]), 2)
    s = math.sqrt(s)
    return s

def load_data():
    # load demographic data
    # demo_reader = csv.reader(open('demographic/2011_demo_normalized.csv'))
    # demos = []
    # for row in demo_reader:
    #     d = [float(field) for field in row]
    #     demos.append(d)

    # load attendance data
    att_reader = csv.reader(open('demographic/2011_att.csv'))
    attendances = []
    for row in att_reader:
        a = [int(field) for field in row]
        attendances.append(a)
    
    # assert(len(demos) == len(attendances))
    # demo_att = [demos[i] + attendances[i] for i in range(len(demos))]
    da_array = numpy.array(attendances)

    return da_array

def output_to_file(filename, arr):
    with open(filename, 'w') as of:
        for row in arr:
            of.write(','.join(row) + '\n')

def load_date_device():
    dd_array = []
    # load csv file
    dd_reader = csv.reader(open('demographic/2011_am.csv'))
    lines = list(dd_reader)
    lines = lines[1:] # skip headers
    for line in lines:
        date = line[0]
        device = line[2]
        dd_array.append([date, device])
    return dd_array

def kmeans_clustering(da_array):
    n_clusters = 6
    # conduct kmeans clustering
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
        l = labels[i]
        groups[l].append(dd_array[i] + list(da_array[i].astype('|S5'))) # |S5: float format strings
    # output the groups to file
    for i in range(n_clusters):
        output_file = 'clustering/%s.txt' % i
        output_to_file(output_file, groups[i])

def dbscan_clustering(da_array):
    # conduct dbscan clustering
    # D2 = distance.squareform(distance.pdist(da_array)) # distance
    # initialize D: matrix n by n where n is number of row in test data
    n = len(da_array)
    D = [[0.0 for i in range(n)] for j in range(n)]
    D = numpy.array(D)
    # calculate distance for each pair
    for i in range(n):
        for j in range(n):
            print i, j
            D[i][j] = demo_distance(da_array[i], da_array[j])
    S = 1 - (D / numpy.max(D)) # similarity
    print S
    db = DBSCAN().fit(S, eps=0.95, min_samples=15)
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
        groups[l].append(dd_array[i] + list(da_array[i].astype('|S5')))
    # output the groups to file
    for i in range(len(groups)):
        filename = 'clustering/%s.txt' % i
        output_to_file(filename, groups[i])

if __name__ == '__main__':
    da_array = load_data() # data array
    dd_array = load_date_device() # date and device array: dd_array

    kmeans_clustering(da_array)
    # dbscan_clustering(da_array)

