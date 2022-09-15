# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
# import torch

# Open file and get each line
risk_text_file = open("risk_dataset.txt", "r")
# risk_text_file = open("risk_dataset_v2_rand.txt", "r")

# Make risk_data a class with menopause and other things as members
# menopause = np.array([0])
age_group = np.array([0])
# bi_rads_density = np.array([0])
# race = np.array([0])
# hispanic = np.array([0])
# bmi = np.array([0])
# age_first_birth = np.array([0])
# relatives_with_bc = np.array([0])
# prev_breast_proc = np.array([0])
# last_mammogram = np.array([0])
# surgical_menopause = np.array([0])
# hormone_therapy = np.array([0])
# invasive_cancer = np.array([0])
cancer_diag = np.array([0])
# training = np.array([0])
# count = np.array([0])

# Pulling data
for data_line in risk_text_file:  
    data_line_split = data_line.split()
    risk_data_row = np.array([int(numeric_string) for numeric_string in data_line_split])
    
    # menopause = np.append(menopause, [risk_data_row[0]], axis=0)
    age_group = np.append(age_group, [risk_data_row[1]], axis=0)
    # bi_rads_density = np.append(bi_rads_density, [risk_data_row[2]], axis=0)
    # race = np.append(race, [risk_data_row[3]], axis=0)
    # hispanic = np.append(hispanic, [risk_data_row[4]], axis=0)
    # bmi = np.append(bmi, [risk_data_row[5]], axis=0)
    # age_first_birth = np.append(age_first_birth, [risk_data_row[6]], axis=0)
    # relatives_with_bc = np.append(relatives_with_bc, [risk_data_row[7]], axis=0)
    # prev_breast_proc = np.append(prev_breast_proc, [risk_data_row[8]], axis=0)
    # last_mammogram = np.append(last_mammogram, [risk_data_row[9]], axis=0)
    # surgical_menopause = np.append(surgical_menopause, [risk_data_row[10]], axis=0)
    # hormone_therapy = np.append(hormone_therapy, [risk_data_row[11]], axis=0)
    # invasive_cancer = np.append(invasive_cancer, [risk_data_row[12]], axis=0)
    cancer_diag = np.append(cancer_diag, [risk_data_row[13]], axis=0)
    # training = np.append(training, [risk_data_row[14]], axis=0)
    # count = np.append(count, [risk_data_row[15]], axis=0)   
    
risk_text_file.close()

# Filter cancer to positive and neg
pos_cancer_diag = cancer_diag[np.where(cancer_diag == 1)]
pos_diag_age_group = age_group[np.where(cancer_diag == 1)]

neg_cancer_diag = cancer_diag[np.where(cancer_diag == 0)]
neg_diag_age_group = age_group[np.where(cancer_diag == 0)]

age_group_dist = np.zeros(11, dtype = int)

for i in range(11):
    age_group_dist[i] = np.size(np.where(pos_diag_age_group == i))

print("Age Group Distribution:", age_group_dist)
print("DONE")

# Build histogram
n_bins = 10
# labels = ['Out of Range','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84']
N, bins, patches = plt.hist(pos_diag_age_group, n_bins, density = 1, color = 'green')

# Setting color
for thispatch in patches:
    color = (np.random.random(), np.random.random(), np.random.random())
    thispatch.set_facecolor(color)

# x = np.array(range(11))
# y = age_group_dist
# plt.plot(x,y)

plt.title('Age Groups with Positive Cancer Diagnosis\n',fontweight = "bold")
plt.xlabel('Age Groups')
plt.ylabel('Probability')

plt.show()




















