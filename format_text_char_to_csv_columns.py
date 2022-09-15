# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:50:53 2022

@author: jpalk
"""
import numpy as np

# Make new CSV file 
new_csv_file = open("risk_dataset_adjusted.csv", "w")

# Open file and get each line (can be csv, text, or any readable file)
orig_file = open("risk_dataset.csv", "r")

# Pulling data
for data_line in orig_file:  
    data_line_split = data_line.split()
    orig_data_row = np.array([int(numeric_string) for numeric_string in data_line_split])
    
    # At this point risk_data_row already ignores spaces
    # print(orig_data_row)
    
    # Write data to a new comma seperated file
    for i in range(np.size(orig_data_row)):
            if i == np.size(orig_data_row)-1:
                new_csv_file.write(str(orig_data_row[i]) + '\n')
            else:
                new_csv_file.write(str(orig_data_row[i]) + ',')
    
orig_file.close()
new_csv_file.close()