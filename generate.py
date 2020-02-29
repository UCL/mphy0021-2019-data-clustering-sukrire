import csv
import random


def generate_points(no_points):
    with open("samples_test.csv", 'w', newline='') as f:
        thewriter = csv.writer(f)
        for _ in range(no_points):
            rand_num_x = random.uniform(-5.0, 5.0)
            rand_num_y = random.uniform(-5.0, 5.0)
            thewriter.writerow([rand_num_x, rand_num_y])