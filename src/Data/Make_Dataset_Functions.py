#This file will be used to store all fucntions to download or generate datasets

import csv
import numpy as np

#function to read the raw dataset
def read_dataset_raw(file_path):

    #initializes output array
    out_arr = []

    #opens file to read
    with open(file_path, 'r') as file:

        #creates csv reader
        reader = csv.reader(file)

        #creates count so first row can be ignored
        count = 0

        #reads file line by line
        for row in reader:

            #ignore first row
            if (count == 0):
                count += 1
                continue
            
            #iterate through index of row for better processing
            for i in range(len(row)):

                #checks if this is a row containing non numerical values and converts
                if(((i >= 5) and (i <= 9)) or (i == 11)):
                    if(row[i] == 'no'):
                        row[i] = 0
                    else: 
                        row[i] = 1
                
                elif(i == 12):
                    if(row[i] == 'furnished'):
                        row[i] = 2
                    elif(row[i] == 'semi-furnished'):
                        row[i] = 1
                    elif(row[i] == 'unfurnished'):
                        row[i] = 0
                
                #otherwise convert string to integer
                else:
                    row[i] = int(row[i])
            
            #add row to output array
            out_arr.append(row)
    
    #returns output array
    return out_arr

#function to write the changed dataset to interim
def write_to_interim(arr, file_path):

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

        #iterate through row
        for row in reader:

            #creates a new_row to be appended
            new_row = []
            
            #iterate through values in row
            for i in range(len(row)):

                #checks for outliers
                if(int(row[3]) == 4):
                    break

                if(int(row[3] == 1) and int(row[0]) > 900000):
                    break

                if(int(row[3] == 2) and int(row[0]) > 1000000):
                    break
                
                #ignore these attributes
                if (i == 6 or i == 7 or i == 8):
                    continue

                new_row.append(row[i])

            if(new_row == []):
                continue
            out_arr.append(new_row)
    
    #returns new output
    return out_arr

#writes to processed data
def write_to_processed(arr, file_path):

    #opens new file as csv file
    with open(file_path, 'w', newline='') as file:

        #creates csv writer
        writer = csv.writer(file)

        #writes rows to csv file
        writer.writerows(arr)



