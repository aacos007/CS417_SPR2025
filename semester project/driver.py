import os
from parse_temps import parse_raw_temps
from piecewise_linear_interpolation import piecewise_linear_interpolation
from least_squares_approximation import least_square_approximation 


def driver(parse_temps, input_filename, output_dir = "output files"):

    list_of_times = []

    #loop that goes through a time values and creates a list of the core temps associated with that time
    for time, cores in parse_raw_temps:
        list_of_times.append(time) #adds time value to the time list
        if not core_data:
            core_data = [[] for _ in range(len(cores))] #creates an empty list for each CPU core (bascially like initalizing core_data with empty data)
        for i, temp in enumerate(cores):
            core_data[i].append(temp) #each temp is added to its corresponding core's list
            
    num_cores = len(core_data) #stores number of CPU cores
    n = len(list_of_times)
    
    #call functions
    piecewise_linear_interpolation(core_data, num_cores, input_filename, list_of_times, output_dir = "output files")
    least_square_approximation(core_data, num_cores, input_filename, list_of_times, n, output_dir = "output files")

