import numpy as np

# Given data
marks = [60, 89, 78, 65, 97, 65, 45, 78, 65, 34,
         23, 34, 55, 67, 88, 90, 76, 34, 32, 33,
         54, 67, 87, 90, 45, 56, 24, 34, 56, 45,
         76, 87, 91, 65, 65, 74, 53, 57, 84, 88,
         32, 34, 36, 33, 76, 50, 76, 65, 45, 56]

# Part (a): Calculate the range of marks
range_marks = np.ptp(marks)  # ptp() returns the range of values (maximum - minimum)

# Part (b): Find the 3rd quartile (75th percentile) of marks
third_quartile = np.percentile(marks, 75)

# Part (c): Find the 80th percentile of this data
percentile_80 = np.percentile(marks, 80)

print(range_marks, third_quartile, percentile_80)
