#scripts to create exploratory or results drive vizualizations

import csv
import scipy.stats as stats

#get house values from interim data
def house_values(file_name):

    #output array
    out_arr = []


    with open(file_name, 'r') as file:
        #creates csv reader
        reader = csv.reader(file)

        #iterate through rows
        for row in reader:

            #adds house value to array
            out_arr.append(int(row[0]))
    
    #returns output array
    return out_arr


#gets skewness
def skew(arr):
    skewness = stats.skew(arr)
    print("Skewness: %.2f", skewness)

#gets kurtosis
def kurtosis(arr):
    kurtosis = stats.kurtosis(arr)
    print("Kurtosis: %.2f", kurtosis)



