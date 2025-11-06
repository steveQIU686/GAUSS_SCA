import pandas as pd
import matplotlib.pyplot as plt

# File paths
file_path1 = 'C:/Users/jqiu2/Desktop/HOST_2025/Original_Materials/001neg1-O0.csv'
file_path2 = 'C:/Users/jqiu2/Desktop/HOST_2025/Original_Materials/100neg0-O0.csv'

# User-specified point and range
point = 3300  # Example point
range_value = 400  # Example range

# Calculate the start and end indices
start_index = max(0, point - range_value // 2)
nrows = range_value

# Load only the specific rows from both CSV files
data1 = pd.read_csv(file_path1, header=None, skiprows=start_index, nrows=nrows)
data2 = pd.read_csv(file_path2, header=None, skiprows=start_index, nrows=nrows)

# Calculate the average power trace for the specified rows
average_trace_0 = data1.mean(axis=1)
average_trace_1 = data2.mean(axis=1)

# Plot the average power traces
plt.figure(figsize=(6, 6))
plt.plot(average_trace_1, label='Case 0')
plt.plot(average_trace_0, label='Case -1')
plt.title(f'Average Power Trace (Point: {point}, Range: {range_value})')
plt.xlabel('Time')
plt.ylabel('Power')
plt.legend()

# Save the figure as an SVG file for editing in Visio
plt.savefig('Avg_Trace_t.f.svg', format='svg')

plt.show()