#scripts to create exploratory or results drive vizualizations

import csv
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

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



