import numpy as np
import pandas as pd
pd.get_option("display.max_columns")

rng = np.random.default_rng(494)
rints = rng.integers(low=0, high=500, size=10)  # get a list of 10 random integers to use for indexing into generated text files

files = ['RNNbaseline-.txt', 'RNNadjusted-.txt', 'SeqGAN-generated.txt', 'TextGAN-generated.txt','LeakGAN-generated.txt']  #  
outputs = []
for file in files:
    with open(file) as text_file:
        method_name = file[:file.index('-')] # get the name of method from text file name
        text_lines = text_file.readlines()
        temp_list = [method_name]
        for i in rints:
            line = text_lines[i].strip('\n')
            #print(line)
            temp_list.append(line)
        outputs.append(temp_list)                

outputs_df = pd.DataFrame(outputs)
outputs_df = outputs_df.transpose()
outputs_df.columns = outputs_df.iloc[0] 
outputs_df = outputs_df[1:]
#print(outputs_df.head())
outputs_df.to_csv('generated texts.csv')

ncols = int(outputs_df.size/len(outputs_df))
nrows = len(outputs_df)

eval_matrix = np.zeros((nrows,ncols)) # empty matrix with 10 rows, 4 columns

def check_array_empty(array):
    for col in array:
        for row in col:
            if row == 0:
                return True
    return False

empty_flag = True
counter = 1
while empty_flag:
    rng_eval = np.random.default_rng()
    rand_col = rng_eval.integers(low=0, high=ncols, size=1)[0] 
    rand_row = rng_eval.integers(low=0, high=nrows, size=1)[0]
    if eval_matrix[rand_row, rand_col] == 0:
        #print('col:', rand_col, ', row:', rand_row) # for testing, print the col and row
        #print(outputs_df.columns[rand_col]) # for testing, print the model type
        eval_sample = outputs_df.iloc[rand_row, rand_col]
        eval_matrix[rand_row, rand_col] = input(f'# {counter} - Input score for:\n {eval_sample}\n')
        counter += 1
    if check_array_empty(eval_matrix) == False: # check if array is empty yet, check_array_empty will return False when it is
        empty_flag = False
import time
print(eval_matrix)

average_scores = []
for column_idx in range(ncols):
    col_subtotal = 0
    for row in eval_matrix:
        col_subtotal += row[column_idx]
    col_mean = col_subtotal/len(eval_matrix)
    average_scores.append(col_mean)

print(average_scores)