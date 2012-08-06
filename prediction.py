import csv
import numpy
from sklearn import svm
from sklearn import datasets
from sklearn import cross_validation

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
n_samples = len(demos)
for i in range(att_dim):
    print 'predicting venue %s' % i
    venue = atts[i]
    clf = svm.SVC(gamma=0.001, C=100.0)
    kf = cross_validation.KFold(n_samples, 10, indices=False)
    scores = cross_validation.cross_val_score(clf, demos, venue, cv=kf)
    print '     %s' % scores
    print '     %s' % scores.mean()
    accs.append(scores.mean())
print 'accuracies from all venues: %s' % accs
print 'average of accuracies: %s' % (sum(accs) / len(accs))
