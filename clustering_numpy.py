import numpy as np
from numpy import random
from argparse import ArgumentParser

def cluster():
    parser = ArgumentParser(description='clustering_numpy.py')
    parser.add_argument('samplesfile', type=str, help='Please give file path to samples.csv')
    parser.add_argument('--iters', default=10, type=int,help='Please give number of iterations')
    arguments = parser.parse_args()

    #implement a way to opent the file and read the data points

    #implement the fucntion

    datapoints = np.genfromtxt(arguments.samplesfile, delimiter=",", dtype='unicode')

    
    
    point1 = np.random.randint(len(datapoints))
    point2 = np.random.randint(len(datapoints))
    point3 = np.random.randint(len(datapoints))

    startingpoints = [datapoints[point1,0],datapoints[point1,1],
                      datapoints[point2,0],datapoints[point2,1],
                      datapoints[point3,0],datapoints[point3,1],]

    #storing array
    str_ary = np.empty(datapoints.shape)
 

if __name__ == "__main__":
    cluster()