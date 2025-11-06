import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import pointbiserialr

# Load data
file_path_0 = 'C:/Users/jqiu2/Desktop/HOST_2025/Original_Materials/001neg1-O0.csv'
file_path_1 = 'C:/Users/jqiu2/Desktop/HOST_2025/Original_Materials/100neg0-O0.csv'

data_0 = pd.read_csv(file_path_0, header=None, nrows=5000, low_memory=False)
data_1 = pd.read_csv(file_path_1, header=None, nrows=5000, low_memory=False)

power_measurements_0 = data_0.iloc[:, :-1].values
power_measurements_1 = data_1.iloc[:, :-1].values

# Save power measurements as a numpy array
power_trace_0 = np.array(power_measurements_0).T  
power_trace_1 = np.array(power_measurements_1).T  
power_trace = np.concatenate((power_trace_0, power_trace_1), axis=0)

# Load plain text
plaintext = np.loadtxt("output_values.txt", delimiter=",", dtype=int)

power_trace = power_trace.astype(float)

# Set data
total_length = len(plaintext) # the length is 30k
total_data_length = 1
power_trace_length = power_trace.shape[1] #5000
save_data = np.empty((1,1,5000), dtype=float)

# Get each byte in input data
print('Start calculating correlation') # to show the process
each_byte = np.empty((0,0), dtype=int)
for byte in range(total_length):
    each_text = plaintext[byte]
    each_byte = np.append(each_byte, each_text)  # get byte 

hamming_weight = np.empty((0,0))
for hw_counter in range(total_length):
    hamming_weight = np.append(hamming_weight, each_byte[hw_counter])

# Calculate the correlation
for timestamp in range(power_trace_length):
    power_model = np.empty((0,0))
    power_model = np.append(power_model, power_trace[:, timestamp])
    
    corr_result = np.corrcoef(power_model, hamming_weight[:])
    save_data[0,0,timestamp] = corr_result[0,1]

# Get two best possible keys' positions
get_highest_position = np.empty((0), dtype=int)
get_lowest_position = np.empty((0), dtype=int)
get_max = np.empty((0))
get_min = np.empty((0))

get_highest_position = np.append(get_highest_position, np.argmax(save_data[0, :, :]))
get_lowest_position = np.append(get_lowest_position, np.argmin(save_data[0, :, :]))
get_max = np.append(get_max, np.max(save_data[0, :, :]))
get_min = np.append(get_min, np.min(save_data[0, :, :]))

# Plot figure 2
plt.figure(figsize=(15, 3))  # Adjust the aspect ratio
plt.plot(np.transpose(save_data[0, :, :]), linewidth=2)  # Make lines bold

# Set labels with editable font sizes
plt.xlabel('Time', fontsize=14)  # Standard size for academic and PDF viewing
plt.ylabel('Correlation', fontsize=14)

# Make all ticks adjustable
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()
plt.subplots_adjust(top=0.9)

# Set the title
plt.suptitle('Correlation Results', fontsize=16)

# Save the figure as a PDF file for editing in Visio and Overleaf
plt.savefig('correlation_results.pdf', format='pdf')

plt.show()