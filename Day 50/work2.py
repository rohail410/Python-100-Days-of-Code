import numpy as np
from scipy import stats

# Given data
ages = [24, 23, 25, 23, 30, 29, 28, 26, 33, 29,
        24, 37, 25, 23, 22, 27, 28, 25, 31, 29,
        25, 22, 31, 29, 22, 28, 27, 26, 23, 21,
        25, 21, 25, 24, 22, 26, 25, 32, 26, 29]

# Part (a)
mean_age = np.mean(ages)
median_age = np.median(ages)
mode_age = stats.mode(ages).mode[0]

# Part (b)
std_dev_age = np.std(ages, ddof=1)

# Part (c)
percentile_77_age = np.percentile(ages, 77)

print(mean_age, median_age, mode_age, std_dev_age, percentile_77_age)
