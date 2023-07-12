#scripts to create exploratory or results drive vizualizations

import csv
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import sys
import os

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

def data_values(file_name):

    #output array
    out_arr = []


    with open(file_name, 'r') as file:
        #creates csv reader
        reader = csv.reader(file)

        #iterate through rows
        for row in reader:

            #temporary list for row
            out_row = []

            #iterate through row
            for value in row:
                #append integer value
                out_row.append(int(value))
            
            #append row to array
            out_arr.append(out_row)

    
    #returns output array
    return out_arr

#returns value of single attribute
def attribute_values(file_name, attribute):
    #output array
    out_arr = []


    with open(file_name, 'r') as file:
        #creates csv reader
        reader = csv.reader(file)

        #iterate through rows
        for row in reader:

            #adds house value to array
            out_arr.append(int(row[attribute]))
    
    #returns output array
    return out_arr


#gets skewness
def skew(arr):
    skewness = stats.skew(arr)
    print(f"Skewness: {skewness:.2f}")

#gets kurtosis
def kurtosis(arr):
    kurtosis = stats.kurtosis(arr)
    print(f"Kurtosis: {kurtosis:.2f}")

#plots frequency of house values
def plot_frequency(arr):

    # Assuming you have the data of numbers from 0 to 10,000,000 stored in a list called 'data'

    # Create the frequency counts for each range
    ranges = []
    for i in range(0, 14000000, 50000):
        ranges.append(i)

    frequency = [sum(start <= num < start + 50000 for num in arr) for start in ranges]

    # Find the maximum frequency
    max_frequency = max(frequency)

    plt.figure(figsize=(15, 3))  # Adjust the width and height as needed

    # Create the bar plot
    plt.bar(ranges, frequency, width=50000)

    # Set the x-axis tick locations
    x_ticks = np.arange(0, 14000000, 1000000)
    plt.xticks(x_ticks)
   
    # Set the x-axis tick format to display whole integers
    plt.gca().get_xaxis().set_major_formatter(plt.FormatStrFormatter('%d'))

    # Set the x-axis tick label font size
    plt.tick_params(axis='x', labelsize=8)

    # Set the y-axis tick locations and labels
    y_ticks = np.arange(0, max_frequency + 1, 10)
    plt.yticks(y_ticks)

    # Set the plot title and labels
    plt.xlabel("House Value")
    plt.ylabel("Frequency")

    # Display the plot
    plt.show()

def correlation_heat_map(arr):

    # Get the current working directory
    current_directory = os.getcwd()

    # Add the main folder to the sys.path list
    main_folder_path = os.path.abspath(os.path.join(current_directory, '..'))
    sys.path.append(main_folder_path)
    
    #Get File Path
    file_path_read = os.path.join(current_directory, '..', 'Data', 'Raw', 'Housing.csv')

    #make data frame
    df = pd.DataFrame(arr)

    #list of names for each item
    name_row = []

    #open raw data to get column names
    with open(file_path_read, 'r') as file:
        #creates csv reader
        reader = csv.reader(file)

        #count to check if first row
        count = 0
        for row in reader:
            if(count == 0):
                name_row = row
                count += 1
                break
    
    df.columns = name_row

    # Compute the correlation matrix
    correlation_matrix = df.corr()

    # Create the heatmap
    plt.figure(figsize=(10,10))  # Adjust the figure size as desired
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)

    # Set the plot title
    plt.title("Correlation Heatmap of Features")

    # Display the plot
    plt.show()

#gives a scatter plot comparing an attribute to price
def scatter(attribute_arr, price_arr):
    # Create the scatterplot
    plt.scatter(attribute_arr, price_arr)

    # Set the y-axis tick format to display whole integers
    plt.gca().get_yaxis().set_major_formatter(plt.FormatStrFormatter('%d'))

    # Set the plot title and labels
    plt.title("Scatterplot of Attribute vs Price")
    plt.xlabel("Attribute")
    plt.ylabel("Price")

    # Display the plot
    plt.show()

#creates a box and whisker plot
def box_whisker(attribute_arr, num_dif_attr, price_arr):

    # Create an empty list for each number of bathrooms
    data = [[] for _ in range(1, num_dif_attr)]

    # Group the house prices based on the number of bathrooms
    for price, bathrooms in zip(price_arr, attribute_arr):
        data[bathrooms - 1].append(price)

    # Create the box and whisker plot
    plt.boxplot(data, labels=[str(i) + " bathrooms" for i in range(1, num_dif_attr)])

    # Set the y-axis tick format to display whole integers
    plt.gca().get_yaxis().set_major_formatter(plt.FormatStrFormatter('%d'))

    # Set the plot title and labels
    plt.title("House Prices by Number of Bathrooms")
    plt.xlabel("Number of Bathrooms")
    plt.ylabel("House Prices")

    # Display the plot
    plt.show()




