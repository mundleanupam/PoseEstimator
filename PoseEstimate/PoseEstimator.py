import numpy as np
import csv

# Author - Anupam Mundale
# Problem - Tricycle Model Pose Estimator


class PoseEstimate(object):


    @staticmethod
    def estimate(current_time, steering_angle, encoder_ticks, angular_velocity, last_time=0):
        # Initialize the heading angle to 0 radians
        th = 0

        # Radius(meters) of the wheel from dataset.txt
        wheel_radius = 0.1250

        # Calculate the circumference of the wheel
        # Circumference = 2 * PI * r (meters)

        wheel_circumference = 2 * wheel_radius * 3.14

        # Calculate the distance travel per revolution based on encoder ticks 35136/rev
        # distance = circumference * (encoder ticks / 35136)
        # Ref - (dataset.txt)
        # Unit - Meters

        wheel_travel_distance = wheel_circumference * (encoder_ticks / 35136)

        # Calculate the x and y co-ordinates using the steering angle given
        # Ref - http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.25.1219&rep=rep1&type=pdf

        x = wheel_travel_distance * np.cos(steering_angle)
        y = wheel_travel_distance * np.sin(steering_angle)

        # Angular velocity given in dataset
        # Unit - Radians/sec
        vth = angular_velocity

        # Difference in time(sec)
        # Current time - last time from the previous row in the dataset
        # Used to calculate position based on time intervals and angular velocity

        dt = (current_time - last_time)
        delta_x = (np.cos(vth) - np.sin(vth)) * dt
        delta_y = (np.sin(vth) + np.cos(vth)) * dt
        delta_th = vth * dt

        # Adding the delta calculated from last time
        x += delta_x
        y += delta_y
        th += delta_th

        # Returning the tuple of 'x' and 'y' coordinates and 'th' heading angle
        return x, y, th


# Using main() to run the sample dataset -
# 1. dataset0
# 2. dataset1
# 3. dataset2
# 4. dataset3
# 5. dataset4
# 6. dataset5

# Created corresponding output dataset files in PoseEstimationTest for running the pytest

# 1. dataset0_output
# 2. dataset1_output
# 3. dataset2_output
# 4. dataset3_output
# 5. dataset4_output
# 6. dataset5_output

if __name__ == '__main__':
    print("""Generating the output dataset estimate files in ../PoseEstimateTests/datasets for
    dataset0,
    dataset1,
    dataset2,
    dataset3,
    dataset4,
    dataset5""")
    last_time = 0.0
    fieldnames = ['time', ' encoder', ' angular_velocity', ' steering_angle', ' X', ' Y', ' Th']
    datasetFileList = ['dataset0', 'dataset1', 'dataset2',
                       'dataset3', 'dataset4', 'dataset5']
    for file in datasetFileList:
        last_time = 0.0
        rowDict = []
        with open('datasets/'+file+'.csv') as csvfile:
            readCSV = csv.DictReader(csvfile, delimiter=',')
            for row in readCSV:
                lists = PoseEstimate.estimate(float(row.get('time')),
                                              float(row.get(' steering_angle')),
                                              int(row.get(' encoder')),
                                              float(row.get(' angular_velocity')), last_time)
                last_time = float(row.get('time'))
                rowDict.append({'time': row.get('time'), ' encoder': row.get(' encoder'),
                                ' angular_velocity': row.get(' angular_velocity'),
                                ' steering_angle': row.get(' steering_angle'),
                                ' X': lists[0], ' Y': lists[1], ' Th': lists[2]})
        outputDatasetFile = file + '_output.csv'
        with open('../PoseEstimateTests/datasets/'+outputDatasetFile, "w") as csvWritefile:
            writeCSV = csv.DictWriter(csvWritefile, delimiter=',', fieldnames=fieldnames)
            writeCSV.writeheader()
            writeCSV.writerows(rowDict)


