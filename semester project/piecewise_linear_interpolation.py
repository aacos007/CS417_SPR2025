import os

"""  
Piecewise linear interpolation is generated/computed using Least Sqaure Approximation.
Each result is saved to a text output file; 1 per core 

Args:
    parse_temps: acts as x-value; computed from parse_raw_temps; is a tuple/pair of objects that includes the time and core_date
        ^ generator (the python equivalence of an iterator)
    input_filename: used to get the name of the input file (for basename)
    output_dir: directory to save output files for each core
        ^ default parameter
""" 

def piecewise_linear_interpolation(core_data, num_cores, input_filename, list_of_times, output_dir = "output files"):

    #extracts the plain filename without all the extra stuff/exetension after the period 
    basename = os.path.splitext(os.path.basename(input_filename))[0]

    #loop to iterate and go through each core
    for core_idx in range(num_cores):
        output_file = os.path.join(output_dir, f"{basename}--core-{core_idx}.txt") #creates output file name
                        #{basefilename}-core-{core-number}.txt format
        with open(output_file, "w") as f: #opens the file so we can write in it
            for k in range(len(list_of_times) - 1):
                #interpolation formula/calculations!! ***
                #interpolation will be computed with adjacent time values/points
                x_k, x_k1 = list_of_times[k], list_of_times[k + 1] 
                y_k, y_k1 = core_data[core_idx][k], core_data[core_idx][k + 1] 
                    
                #compute the coefficients/slope (the 'm' and 'b' in y = mx + b)
                c1 = (y_k1 - y_k) / (x_k1 - x_k)  #calculates slope (x-value coefficient); (the 'm' in y = mx + b)
                c0 = y_k - c1 * x_k  #calculates the intercept (the 'b' in y = mx + b)
                    
                #write to the file 
                f.write(f"{x_k}<=x<={x_k1}; y={c0:.6f}+{c1:.6f}x; interpolation\n")
        
    #print(f"Interpolation results saved in '{output_dir}' directory.") 

