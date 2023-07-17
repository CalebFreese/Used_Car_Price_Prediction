#This file will be used to store all fucntions to download or generate datasets

import csv
import numpy as np
from sklearn.model_selection import train_test_split
from datetime import datetime

#function to read the raw dataset and adjust to interim
def read_dataset_raw(file_path):

    #initializes output array
    out_arr = []

    #initializes array containing missing features
    none_arr = []

    #opens file to read
    with open(file_path, 'r') as file:

        #creates csv reader
        reader = csv.reader(file)

        #creates count so first row can be ignored
        count = 0

        #tries to read each row
        try:
            #reads file line by line
            for row in reader:

                #ignore first row
                if (count == 0):
                    count += 1
                    continue


                #initializes none variable which will check if row has empty feature
                none = False

                #initializes new_row which will ignore columns
                new_row = []

                #iterate through index of row for better processing
                for i in range(len(row)):

                    #ignore first 5 columns
                    if(i < 5):
                        continue

                    #checks if price is less than 100 or greater than 100000
                    if(i == 5):
                        if(int(row[i]) < 100):
                            none = True
                            new_row.append("None")
                            continue

                        if(int(row[i]) > 50000):
                            none = True
                            new_row.append("None")
                            continue

                    #ignore number of pictures column
                    if(i == 18):
                        continue

                    #gets dates
                    if(i == 17):
                        date1 = datetime.strptime(row[i], '%Y-%m-%d %H:%M:%S').date()
                        continue
                    if(i == 20):
                        date2 = datetime.strptime(row[i], '%Y-%m-%d %H:%M:%S').date()
                        # Calculate the difference between the dates
                        delta = date2 - date1

                        # Extract the number of days
                        days_between = delta.days
                        new_row.append(days_between)
                        continue

                    if(row[i] == ""):
                        none = True
                        new_row.append("None")
                        continue
                    
                    new_row.append(row[i])
                #add row to array depending on if it has a missing feature or not
                if(none):
                    none_arr.append(new_row)

                else:
                    out_arr.append(new_row)
            
        except UnicodeDecodeError:
            # Handle the UnicodeDecodeError and skip the row
            print("UnicodeDecodeError occurred. Skipping the row.")
            pass
    
    #returns output array
    return out_arr, none_arr

#finds all unique values in column and does label_encoding
def label_encoding(arr, column_arr):

    #gets number of columns
    size = len(column_arr)

    #intializes unique value array and output array
    #unique value array contains a list of empty sublists for each input of column_arr
    unique_values = [[] for _ in range(size)]
    out_arr = []

    #iterates through each row
    for row in arr:
        #iterate through column array to check
        for i in range(len(column_arr)):

            #checks if value is unique
            if row[column_arr[i]] in unique_values[i]:
                #if value is seen already replace value with index in unique_values
                row[column_arr[i]] = unique_values[i].index(row[column_arr[i]])
            else:
                #if value has not been seen, add value to unique_values and then replace with index
                unique_values[i].append(row[column_arr[i]])
                row[column_arr[i]] = unique_values[i].index(row[column_arr[i]])
        
        #adds changed row to out_arr
        out_arr.append(row)
    
    #returns adjusted array
    return out_arr

#finds all unique values in column and does one-hot encoding
def one_hot_encoding(arr, col):

    #gets size of data set
    size = len(arr)
    
    #gets unique value array
    unique_values = []

    #iterates through array to find unique values
    for row in arr:
        if row[col] in unique_values:
            continue
        else:
            unique_values.append(row[col])
    
    #initializes one hot array where only the column with the correct value will have value 1, otherwise the value will be 0
    #if the first value in unique_values is the value contained in the row of arr, all columns will be 0
    num_unique_values = len(unique_values)
    col_size = num_unique_values - 1
    one_hot_arr = np.zeros((size, col_size))

    #idx to count row for one_hot_arr
    row_idx = 0

    for row in arr:
        #checks if the this row is the first value in unique values
        if row[col] == unique_values[0]:
            row_idx += 1
            continue

        #if not, set a column to 1
        col_idx = unique_values.index(row[col])

        #changes index to index in unique values
        col_idx = col_idx - 1

        #sets correct value to 1
        one_hot_arr[row_idx][col_idx] = 1

        row_idx += 1
    
    #initializes out_arr
    out_arr = []

    #initializes row_idx to check one_hot_arr
    row_idx = 0

    for row in arr:
        #initializes a new row to be appended to out_arr
        new_row = []

        for col_idx in range(len(row)):

            #checks if this is the column needed to change
            if col_idx == col:

                #iterates through row of one_hot_arr and appends each value to new_row
                for value in one_hot_arr[row_idx]:
                    new_row.append(value)

                #goes to next col_idx
                continue

            #if this is not the column we change, append value in arr to new_row
            new_row.append(row[col_idx])
        
        #adds the new row to the output array
        out_arr.append(new_row)

        row_idx += 1

    return out_arr
            




#function to write the dataset to interim
def write_to_interim(arr, file_path):

    #gets adjsuted output array
    out_arr = label_encoding(arr, [1,2,4,6,9,10,11])

    #opens new file as csv file
    with open(file_path, 'w', newline='') as file:

        #creates csv writer
        writer = csv.writer(file)

        #writes rows to csv file
        writer.writerows(out_arr)

#writes to none in interim
def write_to_interim_none(arr,file_path):
    #opens new file as csv file
    with open(file_path, 'w', newline='') as file:

        #creates csv writer
        writer = csv.writer(file)

        #writes rows to csv file
        writer.writerows(arr)

#function to read and change interim data set
def read_data_interim(file_path):

    #initializes output array
    out_arr = []

    #opens file to read
    with open(file_path, 'r') as file:

        #creates csv reader
        reader = csv.reader(file)

        # Add a small constant to zero values
        small_constant = 1e-9

        #iterate through row
        for row in reader:

            #creates a new_row to be appended
            new_row = []
            
            #iterate through values in row
            for i in range(len(row)):

                #log transform applied to this row
                if((i == 0) or (i == 3) or (i == 5) or (i == 7) or (i == 13)):
                    row[i] = int(row[i])
                    if(row[i] == 0):
                        row[i] = small_constant
                    new_row.append(np.log(row[i]))
                    continue

                #ignore these rows
                if((i == 1) or (i == 6) or (i == 8) or (i == 10) or (i == 12)):
                    continue

                new_row.append(int(row[i]))

            if(new_row == []):
                continue
            out_arr.append(new_row)
    
    #returns new output
    return out_arr

#writes to processed data
def write_to_processed(arr, file_path):

    out_arr = one_hot_encoding(arr, 1)

    #opens new file as csv file
    with open(file_path, 'w', newline='') as file:

        #creates csv writer
        writer = csv.writer(file)

        #writes rows to csv file
        writer.writerows(out_arr)

def read_processed(file_path):

    #intialize output array
    out_arr = []

    #opens file
    with open(file_path, 'r') as file:

        #creates csv reader
        reader = csv.reader(file)

        #iterates through rows
        for row in reader:

            #iterate through values
            for i in range(len(row)):

                row[i] = float(row[i])
            
            out_arr.append(row)
    
    #checks if dimensions are wrong for y
    if(len(out_arr) == 1):
        out_arr = out_arr[0]

    #return output array
    return out_arr

#read processed y arrays as float values instead of integer
def read_y(file_path):

    #intialize output array
    out_arr = []

    with open(file_path, 'r') as file:

        #creates csv reader
        reader = csv.reader(file)

        #iterates through rows
        for row in reader:

            #iterate through values
            for i in range(len(row)):

                row[i] = float(row[i])
            
            out_arr.append(row)
    
    #checks if dimensions are wrong for y
    if(len(out_arr) == 1):
        out_arr = out_arr[0]
    
    #returns output
    return out_arr

def test_train(arr):

    #convert to numpy
    arr = np.array(arr)

    #gets attributes and outputs
    y = arr[:, 0]
    X = arr[:, 1:]

    #Splits data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    #returns all
    return X_train, X_test, y_train, y_test

#writes prices to a single row
def write_output(arr, file_path):

    #opens new file as csv file
        with open(file_path, 'w', newline='') as file:

            #creates csv writer
            writer = csv.writer(file)

            #writes rows to csv file
            writer.writerow(arr)

