import os

def piecewise_linear_interpolation(parse_temps, output_dir = "output files"):
    """
    Piecewise linear interpolation is generated/computed using Least Sqaure Approximation.
    Each result is saved to a text output file; 1 per core 

    Args:
        parse_temps: acts as x-value; computed from parse_raw_temps; is a tuple/pair of objects that includes the time and core_date
            ^ generator (the python equivalence of an iterator)
        output_dir: directory to save output files for each core
            ^ default parameter
    """
  

    # lists that will store parsed time values (time) & readings of CPU core temperatures (core_data)
    time = []
    core_data = []
    
    #loop that goes through a time values and creates a list of the core temps associated with that time
    for time, cores in parse_temps:
        time.append(time) #adds the time value to the time list
        if not core_data:
            core_data = [[] for _ in range(len(cores))] #creates an empty list for each CPU core (bascially like initalizing core_data with empty data)
        for i, temp in enumerate(cores):
            core_data[i].append(temp) #each temp is added to its corresponding core's list
    
    num_cores = len(core_data) #stores number of CPU cores

    #loop to iterate and go through each core
    for core_idx in range(num_cores):
        output_file = os.path.join(output_dir, f"core_{core_idx}.txt") #creates the output file name
        with open(output_file, "w") as f: #opens the file so we can write in it
            for k in range(len(time) - 1):
                #interpolation formula/calculations!! ***
                #interpolation will be computed with adjacent time values/points
                x_k, x_k1 = time[k], time[k + 1] 
                y_k, y_k1 = core_data[core_idx][k], core_data[core_idx][k + 1] 
                
                #compute the coefficients/slope (the 'm' and 'b' in y = mx + b)
                c1 = (y_k1 - y_k) / (x_k1 - x_k)  #calculates slope (x-value coefficient); (the 'm' in y = mx + b)
                c0 = y_k - c1 * x_k  #calculates the intercept (the 'b' in y = mx + b)
                
                #write to the file 
                f.write(f"{x_k}<=x<{x_k1}; y={c0:.6f}+{c1:.6f}x; interpolation\n")
    
    #print(f"Interpolation results saved in '{output_dir}' directory.") 