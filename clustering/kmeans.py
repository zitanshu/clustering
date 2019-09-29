from collections import defaultdict
from math import inf
import pandas
import random
import numpy
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    df = pandas.DataFrame(points)
    new_point = df.mean(axis=0).tolist()
    return new_point



def update_centers(data_set, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    k = max(assignments)
    result = []
    for cluster in range(k+1):
        #all_points contains all the points that belongs to the same assignment
        all_points = []
        for i in range(len(assignments)):
            if assignments[i] == cluster:
                point = data_set[i]
                all_points.append(point)
        
        new_center = point_avg(all_points)
        result.append(new_center)
    return result




def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """

    x = numpy.asarray(a)
    y = numpy.asarray(b)
    dist = numpy.linalg.norm(x-y)
    return dist


def generate_k(data_set, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    list_of_idx = random.sample(range(len(data_set)),k)
    result = []
    for element in list_of_idx:
        point = data_set[element]
        result.append(point)
    
    return result


def get_list_from_dataset_file(dataset_file):
    df = pandas.read_csv(dataset_file)
    result = df.values.tolist()
    return result


def cost_function(clustering):
    raise NotImplementedError()


def k_means(dataset_file, k):
    dataset = get_list_from_dataset_file(dataset_file)
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering

#print(k_means("../tests/test_files/dataset_1_k_is_2_0.csv",2))