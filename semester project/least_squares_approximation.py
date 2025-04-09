import os

#f(x) = = time, x_i = temps

def least_square_approximation(parse_temps, input_filename, output_dir = "output files"):
#using presolved Ab method
     
#copied from previous itertion to extract data 
# lists that will store parsed time values (list_of_times) & readings of CPU core temperatures (core_data)
    list_of_times = []
    core_data = []

#extracts the plain filename without all the extra stuff/exetension after the period 
    basename = os.path.splitext(os.path.basename(input_filename))[0] 
    
#loop that goes through a time values and creates a list of the core temps associated with that time
    for time, cores in parse_temps:
        list_of_times.append(time) #adds the time value to the time list
        if not core_data:
            core_data = [[] for _ in range(len(cores))] #creates an empty list for each CPU core (bascially like initalizing core_data with empty data)
        for i, temp in enumerate(cores):
            core_data[i].append(temp) #each temp is added to its corresponding core's list
        
    num_cores = len(core_data) #stores number of CPU cores


#LSA math 
    sum_times = 0 #x
    sum_temps = 0 #y
    sum_times_squared = 0 #x^2
    sum_1 = 0 #number of points
    sum_xy = 0 #xy (time_temps * temperatures)


    #loop to iterate and go through each core
    for core_idx in range(num_cores):
        output_file = os.path.join(output_dir, f"{basename}--core-{core_idx}.txt") #creates the output file name
                        #{basefilename}-core-{core-number}.txt format
        with open(output_file, "w") as f: #opens the file so we can write in it
            for k in range(len(list_of_times) - 1):
                x_k, x_k1 = list_of_times[k], list_of_times[k + 1] 
                y_k, y_k1 = core_data[core_idx][k], core_data[core_idx][k + 1] 
                
                sum_times += list_of_times[k]
                sum_temps += core_data[core_idx][k]
                sum_times_squared += list_of_times[k]**2
                sum_1 += parse_temps.__length_hint__()
                sum_xy += list_of_times[k] * core_data[core_idx][k]

    #compute the determinants
    det = sum_1 * sum_times_squared - 2(sum_times)
    detX = sum_temps * sum_times_squared - sum_times * sum_xy
    detY = sum_1 * sum_xy - sum_temps * sum_times 

#compute the coefficients/slope (the 'm' and 'b' in y = mx + b)
    c0 = (detX)/det 
    c1 = (detY)/det 


#write to the file 
f.write(f"{x_k}<=x<={x_k1}; y={c0:.6f}+{c1:.6f}x; least-squares\n")

#print(f"Least squares approximation results saved in '{output_dir}' directory.") 
    

     

"""
def linear(times: list[float], core_temps: list[float]):
    
    T.B.W.

    Returns:
        one tuple in the form...

        (start time, end time, y-intercept, slope)
    

    start_time =
    end_time = 
    y_int = reading_end - (slope * time_end)
    slope = (reading_end - reading_start) / (time_end - time_start)

    return(start_time, end_time, y_int, slope)

    raise NotImplementedError() """

