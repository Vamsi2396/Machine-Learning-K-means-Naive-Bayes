from __future__ import division
from collections import defaultdict
import random, sys
import numpy as np

def loadData():
    data = [l.strip() for l in open('iris.csv') if l.strip()]
    features = [tuple(map(float, i.split(',')[:-1])) for i in data]
    labels = [i.split(',')[-1] for i in data]
    return dict(zip(features, labels))  #returns features and lables dictionary

#Kmeans Algorithm.
def kmeans(features, k):
    center = dict((c, [c]) for c in features[:k])
    center[features[k - 1]] += features[k:]
    centroid_same = True
    while  centroid_same:
        new_center = data_cluster(center)
        new_center = centroid_new(new_center)
        if center == new_center:
            centroid_same = False
            break
        else:
            center = new_center
    return center

#Clusters data using Centroid
def data_cluster(center):
    new_center = defaultdict(list)
    for cc in center: #foreach cluster centroid
        for i in center[cc]: #foreach cluster member
            low_dis = min(center, key=lambda c:calculate_Distance(i,c))
            new_center[low_dis] += [i]
    return new_center

#Distance between vectors
def calculate_Distance(a,b):
    x = np.array
    y = x(a) - x(b)
    return np.sqrt(np.dot(y,y))

#New centroid 
def centroid_new(center):
    new_center = {}
    for c in center:
        new_center[mean(center[c])] = center[c]
    return new_center

def mean(features):
    return tuple(np.mean(features, axis=0))

#Counts the members of each cluster
def print_clusters(clist):
    count = defaultdict(int)
    for i in clist:
        count[i] += 1
    return dict(count)

def main():
    data = loadData() #Loads the data
    features = list(data.keys())
    labels = list(data.values())
    random.shuffle(features)
    clusters = kmeans(features,3)   #Calling kmeans with features and k value  
    #Printing the clusters
    for c in clusters:
        print (print_clusters([data[i] for i in clusters[c]]))

if __name__ == "__main__":
    main()