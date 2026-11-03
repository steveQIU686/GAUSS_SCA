import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the two trace groups. Filenames identify the sampling/negation cases.
trace_file_001_neg1 = 'C:/REFERENCE_DIR/001neg1-O0.csv'
trace_file_100_neg0 = 'C:/REFERENCE_DIR/100neg0-O0.csv'
sample_limit = 5000
trace_data_001_neg1 = pd.read_csv(trace_file_001_neg1, header=None, nrows=sample_limit, low_memory=False)
trace_data_100_neg0 = pd.read_csv(trace_file_100_neg0, header=None, nrows=sample_limit, low_memory=False)

# Preserve the original CSV handling: exclude the last column and transpose.
# After transposition, each row is a trace and each column is a sample.
traces_001_neg1 = trace_data_001_neg1.iloc[:, :-1].to_numpy(dtype=float).T
traces_100_neg0 = trace_data_100_neg0.iloc[:, :-1].to_numpy(dtype=float).T
combined_traces = np.concatenate((traces_001_neg1, traces_100_neg0), axis=0)

# Artificial HW labels (0 or 64), one per trace in the concatenation order.
# These are already Hamming weights, not plaintext or values to convert to HW.
hw_labels = np.loadtxt('output_values.txt', delimiter=',', dtype=float).reshape(-1)
num_traces, num_samples = combined_traces.shape
if len(hw_labels) != num_traces:
    raise ValueError('Expected one HW label per trace in combined_traces.')
correlations = np.empty(num_samples, dtype=float)

# Correlate the known HW labels with measurements at each sample position.
print('Start calculating POI correlation')
for sample_index in range(num_samples):
    sample_measurements = combined_traces[:, sample_index]
    correlation_matrix = np.corrcoef(sample_measurements, hw_labels)
    correlations[sample_index] = correlation_matrix[0, 1]

# Locate the largest positive and most negative correlations, not key guesses.
max_correlation_sample = np.argmax(correlations)
min_correlation_sample = np.argmin(correlations)
max_correlation = correlations[max_correlation_sample]
min_correlation = correlations[min_correlation_sample]

# Plot correlation across sample positions.
plt.figure(figsize=(15, 3))
plt.plot(correlations, linewidth=2)
plt.xlabel('Sample index', fontsize=14)
plt.ylabel('Correlation', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.suptitle('SHIFT-SNARE POI Correlation', fontsize=16)
plt.savefig('correlation_results.pdf', format='pdf')
plt.show()
