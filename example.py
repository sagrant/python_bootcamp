#!/usr/bin/env python3
import pandas as pd
import numpy as np

### DATA TYPES
integer_1 = 5
float_1 = 5.0
float_2 = 3.5
string_1 = 'hello world'

bool_1 = True
bool_2 = False

math_equation_1 = integer_1 + float_1
print(math_equation_1)

### READING AND WRITING FILES
# Step 1: Create a variable that stores the input file path 
in_file = 'alignment_ex.sam'

# Step 2: Create a variable that stores the file handle
handle = open(in_file, 'r') # Step 3. Open the input file with the built-in function open()

### ITERATORS
# Step 1: instantiate list 
lst = [] 

 # Step 2: iterate over file contents
for line in handle:

  # Step 3: use conditional statements to parse lines of interest from file
  if not line.startswith('@'):
    lst.append(line)
  

