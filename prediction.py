import csv
import numpy
from sklearn import svm
from sklearn import datasets

# import demo data from file
demo_reader = csv.reader(open('demographic/2011_demo_normalized.csv'))
lines = list(demo_reader)
demos = []
for line in lines:
    cur_demo = [float(n) for n in line]
    demos.append(cur_demo)

# import venue data from file
att_reader = csv.reader(open('demographic/2011_att.csv'))
lines = list(att_reader)
att_dim = len(lines[0])
atts = [[] for i in range(att_dim)]
for line in lines:
    # add different to different list (represent different venue) accordingly
    for i in range(att_dim):
        atts[i].append(int(line[i]))

# for each venue, test the prediction accuracy
accs = []
for i in range(att_dim):
    print 'predicting venue %s' % i
    venue = atts[i]
    classifier = svm.SVC(gamma=0.001, C=100.0)
    classifier = classifier.fit(demos[:-130], venue[:-130])
    prediction = classifier.predict(demos[-130:])
    matched = 0.0
    for i in range(130):
        if prediction[i] == venue[i]:
            matched += 1
    acc = matched / 130.0
    print ' accuracy: %s' % acc
    accs.append(acc)
print 'average accuracy: %s' % (sum(accs) / len(accs))
