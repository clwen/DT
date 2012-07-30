import csv
import numpy
from sklearn import svm
from sklearn import datasets

# import demo data from file
demo_reader = csv.reader(open('demographic/2011_demo.csv'))
lines = list(demo_reader)
demos = []
for line in lines:
    cur_demo = [int(n) for n in line]
    demos.append(cur_demo)

# improt venue data from file
att_reader = csv.reader(open('demographic/2011_att.csv'))
lines = list(att_reader)
att_dim = len(lines[0])
atts = [[] for i in range(att_dim)]
for line in lines:
    # add different to different list (represent different venue) accordingly
    for i in range(att_dim):
        atts[i].append(int(line[i]))

# for each venue, test the prediction accuracy
for i in range(att_dim):
    print 'predicting venue %s' % i
    venue = atts[i]
    classifier = svm.SVC(gamma=0.001, C=100.0)
    classifier = classifier.fit(demos[:-100], venue[:-100])
    prediction = classifier.predict(demos[-100:])
    matched = 0
    for i in range(100):
        if prediction[i] == venue[i]:
            matched += 1
    print ' matched: %s' % matched
