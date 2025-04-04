#!/usr/bin/env python3
import pandas as pd
import numpy as np

### DATA TYPES ###
integer_1 = 5
float_1 = 5.0
float_2 = 3.5
string_1 = 'hello world'

bool_1 = True
bool_2 = False

list_1 = [integer_1, bool_1, string_1, bool_2, float_1]

print('this is the entire list = ' + str(list_1))
print('this is the first item in the list = ' + str(list_1[0]))
print('this is the second item in the list = ' + str(list_1[1]))

### READING AND WRITING FILES ####
# Step 1: Create a variable that stores the input file path 
in_file = 'alignment_ex.sam'

# Step 2: Create a variable that stores the file handle
handle = open(in_file, 'r') # Step 3. Open the input file with the built-in function open()

### ITERATORS ###
# Step 1: instantiate data structure of choice
test_list = [] # instantiate a list with brackets
test_dict = {} # instantiate a dictionary with curly brackets

# Step 2: iterate over file contents
for line in handle:

    # Step 3: use a conditional statement to skip header lines
    if not line.startswith('@'): 
        
        split_line = line.split('\t') # use tab delimiter to split up lines with data

        sample_ID = split_line[2] # assign variable "sample_ID" 
        sequence_length = split_line[4] # assign variable "sequence_length"
        sequence = split_line[9] # assign variable "sequence"

        test_list.append(sample_ID) # put stuff in your list 
        test_dict[sample_ID] = sequence # put stuff in your dictionary 

# Now you can iterate over your dictionary or list
for key_sample_ID, value_sequence in test_dict.items():
    get_sequence = test_dict.get(key_sample_ID)

### PANDAS ###
# Read file in as a dataframe 
sam_file = pd.read_csv('alignment_ex.sam', sep = '\t', skiprows = 9) 

# Iterate over SAM file dataframe:
for result, data in sam_file.iterrows():
    alignment_hit = result[0]
    data_point = data[0]
    
# Use groupby function to manipulate dataframe 
diamond_output_df = pd.read_csv('diamond_output_ex.m8', sep = '\t', index_col = False, header = None,\
                                names = ['Gene', 'Protein', 'Pident', 'Length', 'Mismatch', \
                                        'Gapopen', 'Qstart', 'Qend', 'Sstart', 'Send', 'E-value', \
                                        'Bitscore', 'Taxon', 'Taxon_ID'])

grouped_df = diamond_output_df.groupby('Gene').mean()

