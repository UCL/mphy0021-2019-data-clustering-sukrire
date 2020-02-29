import time
import subprocess
from generate import generate_points
import matplotlib.pyplot as plt
import numpy as np

class Timer:    
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start
        
sample_sizes= np.linspace(100,10000,10)
time_cluster = []
time_cluster_num = []

for i in range(len(sample_sizes)):
    generate_points(int(sample_sizes[i]))
    with Timer() as t:
        subprocess.call(["python", "clustering.py", "samples_test.csv"])
    time_cluster.append(t.interval)
    print(sample_sizes[i], 'no numpy done, time taken = ',t.interval)
    with Timer() as t:
        subprocess.call(["python", "clustering_numpy.py", "samples_test.csv"])
    time_cluster_num.append(t.interval)
    print(sample_sizes[i], 'numpy done, time taken = ',t.interval)
    
print('total time for no numpy cluster = ',np.sum(time_cluster))
print('total time for numpy cluster = ',np.sum(time_cluster_num))

plt.plot(sample_sizes,time_cluster, Label='no numpy')
plt.plot(sample_sizes,time_cluster_num, Label='numpy') 
plt.title('Time taken to run clustering tests vs sample size')
plt.ylabel('Time in s') 
plt.xlabel('No of samples')
plt.legend(loc = 'upper left') 
plt.savefig('performance.png')    
plt.show()
     
     
     
     

