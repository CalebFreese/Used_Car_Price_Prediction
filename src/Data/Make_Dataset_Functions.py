#This file will be used to store all fucntions to download or generate datasets

import csv

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
            for i in len(row):

                #checks if this is a row containing non numerical values and converts
                if(((i >= 5) and (i <= 9)) or (i == 11)):
                    if(row[i] == 'no'):
                        row[i] = 0
                    else: 
                        row[i] = 1
                
                elif(i == 12):
                    if(row[i] == 'furnished'):
                        row[i] = 1
                    elif(row[i] == 'semi-furnished'):
                        row[i] = 0.5
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
        writer = csv.write(file)

        #writes rows to csv file
        writer.writerows(arr)

