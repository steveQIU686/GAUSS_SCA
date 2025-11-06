import trsfile
import csv
import numpy as np

# Adjusting the previous trs_to_csv code to apply the scaling factor when writing the CSV
def trs_to_csv_with_scaling(trs_file_path, csv_file_path, scaling_factor=0.0007874):
    # Open the .trs file
    with trsfile.open(trs_file_path, 'r') as trs_file:
        # Get the number of traces (columns)
        num_traces = len(trs_file)
        
        # Get the number of samples per trace (using the length of samples in the first trace)
        num_samples = len(trs_file[0].samples)
        
        # Initialize an array to hold the data (rows: samples, columns: traces)
        data = np.zeros((num_samples, num_traces))
        
        # Iterate through the traces and populate the data matrix
        for trace_index, trace in enumerate(trs_file):
            data[:, trace_index] = trace.samples * scaling_factor  # Apply scaling factor to each sample
            
        # Write the scaled data to a CSV file
        with open(csv_file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            
            # Write the rows (each row corresponds to a sample across all traces)
            for sample_row in data:
                csvwriter.writerow(sample_row)
    
    print(f"Successfully converted {trs_file_path} to {csv_file_path} with scaling factor {scaling_factor}.")

# Example usage
trs_file = '100neg0-O3.trs'  # Replace with your actual .trs file path
csv_file = '100neg0-O3.csv'  # Replace with your desired .csv output file path
trs_to_csv_with_scaling(trs_file, csv_file)