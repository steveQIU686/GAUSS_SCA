import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# File paths
file_path_0 = 'C:/Users/jqiu2/Desktop/HOST_2025/Original_Materials/100neg0-O0.csv'
file_path_1 = 'C:/Users/jqiu2/Desktop/HOST_2025/Original_Materials/001neg1-O0.csv'
label_file_path = 'C:/Users/jqiu2/Desktop/HOST_2025/Original_Materials/Attack-O0/t.f/Accuracy/labels.txt'

poi = 3300  # Row of interest

# Load only the POI row from each CSV file
measurements_0 = pd.read_csv(file_path_0, header=None, skiprows=poi - 1, nrows=1).values.flatten()
measurements_1 = pd.read_csv(file_path_1, header=None, skiprows=poi - 1, nrows=1).values.flatten()

print("Data import completed.")

# Combine POI measurements
all_poi_measurements = np.concatenate((measurements_0, measurements_1))

# Calculate mean and variance
mean_0 = np.mean(measurements_0)
var_0 = np.var(measurements_0)
mean_1 = np.mean(measurements_1)
var_1 = np.var(measurements_1)

print(f"Mean for input 0: {mean_0}, Variance for input 0: {var_0}")
print(f"Mean for input 1: {mean_1}, Variance for input 1: {var_1}")

# Create Gaussian models
gaussian_0 = norm(loc=mean_0, scale=np.sqrt(var_0))
gaussian_1 = norm(loc=mean_1, scale=np.sqrt(var_1))

# Predict labels for each POI measurement step by step
predicted_labels = []
for measurement in all_poi_measurements:
    pdf_0 = gaussian_0.pdf(measurement)
    pdf_1 = gaussian_1.pdf(measurement)
    if pdf_1 > pdf_0:
        predicted_labels.append(64)  # Case 1
    else:
        predicted_labels.append(0)  # Case 0

predicted_labels = np.array(predicted_labels)
print("Prediction completed step by step.")

# Load true labels
true_labels = pd.read_csv(label_file_path, header=None).values.flatten()

# Ensure sizes match
if len(predicted_labels) != len(true_labels):
    raise ValueError("Mismatch between number of predictions and true labels.")

# Calculate accuracy
accuracy = np.mean(predicted_labels == true_labels)

print(f"Overall Accuracy: {accuracy * 100:.2f}%")

# Visualize the Gaussian models
x_min = min(all_poi_measurements)
x_max = max(all_poi_measurements)
x = np.linspace(x_min, x_max, 1000)
pdf_0 = gaussian_0.pdf(x)
pdf_1 = gaussian_1.pdf(x)

plt.plot(x, pdf_0, label='Case 0')
plt.plot(x, pdf_1, label='Case -1')
plt.xlabel('Power Measurement')
plt.ylabel('Probability Density')
plt.title('Univariate Gaussian Models')
plt.legend()

# Save the figure as an SVG file for editing in Visio
plt.savefig('Univariate_Gauss(t.f).svg', format='svg')
plt.show()
