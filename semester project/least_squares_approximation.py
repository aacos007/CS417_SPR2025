import os

#f(x) = = time, x_i = temps

def least_square_approximation(core_data, num_cores, input_filename, list_of_times, n, output_dir = "output files"):
  
    #extracts the plain filename without all the extra stuff/exetension after the period 
    basename = os.path.splitext(os.path.basename(input_filename))[0] 

   
    #LSA math starts
    for core_idx in range(num_cores):
        sum_times = 0 #x
        sum_temps = 0 #y
        sum_times_squared = 0 #x^2
        sum_1 = 0 #number of points
        sum_xy = 0 #xy (time_temps * temperatures)

        #summation calculations
        for i in range(n):
            x = list_of_times[i]
            y = core_data[core_idx][i]
            sum_times += x
            sum_temps += y            
            sum_times_squared += x ** 2
            sum_xy += x * y
        
        #finding determinatns
        det = n * sum_times_squared - sum_times ** 2
        detX = sum_temps * sum_times_squared - sum_times * sum_xy
        detY = n * sum_xy - sum_times * sum_temps

        #compute c0 & c1...if statement steers clear of division by 0
        if det == 0:
            c0 = c1 = 0
        else:
            c0 = (detX)/det 
            c1 = (detY)/det

        #writing to output file
        output_file = os.path.join(output_dir, f"{basename}--core-{core_idx}.txt")
        with open(output_file, "a") as f:
            f.write(f"{list_of_times[0]}<=x<={list_of_times[-1]};y={c0:.6f}+{c1:.6f}x; least-squares\n")
            print(f"DEBUG: Successfully wrote line for core {core_idx}")


