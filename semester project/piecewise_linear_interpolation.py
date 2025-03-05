import os

def piecewise_linear_interpolation(parse_temps, output_dir = "output files"):
    """
    Piecewise linear interpolation is generated/computed using Least Sqaure Approximation.
    Each result is saved to a text output file; 1 per core 

    Args:
        parse_temps: acts as x-value; computed from parse_raw_temps
        output_dir: directory to save output files for each core
    """
  
  
    times = []
    core_data = []
    
    for time, cores in parse_temps:
        times.append(time)
        if not core_data:
            core_data = [[] for _ in range(len(cores))]
        for i, temp in enumerate(cores):
            core_data[i].append(temp)
    
    num_cores = len(core_data)
    for core_idx in range(num_cores):
        output_file = os.path.join(output_dir, f"core_{core_idx}.txt")
        with open(output_file, "w") as f:
            for k in range(len(times) - 1):
                x_k, x_k1 = times[k], times[k + 1]
                y_k, y_k1 = core_data[core_idx][k], core_data[core_idx][k + 1]
                
                # Compute coefficients
                c1 = (y_k1 - y_k) / (x_k1 - x_k)  # Slope
                c0 = y_k - c1 * x_k  # Intercept
                
                # Write to file
                f.write(f"{x_k}<=x<{x_k1}; y={c0:.6f}+{c1:.6f}x; interpolation\n")
    
    print(f"Interpolation results saved in '{output_dir}' directory.") 