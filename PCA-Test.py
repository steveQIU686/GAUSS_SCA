import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


# Specify the file paths
file1 = 'C:/Users/jqiu2/Desktop/HOST_2025/Original_Materials/001neg1-O0.csv'
file2 = 'C:/Users/jqiu2/Desktop/HOST_2025/Original_Materials/100neg0-O0.csv'

# Load only the 3300th row from each file
row_3300_file1 = pd.read_csv(file1, skiprows=19585, nrows=10, header=None)
row_3300_file2 = pd.read_csv(file2, skiprows=19585, nrows=10, header=None)

# Combine the two rows into a single dataset
combined_data = pd.concat([row_3300_file1, row_3300_file2], axis=1)

# Perform PCA
pca = PCA(n_components=2)  # Adjust components as needed
pca_result = pca.fit_transform(combined_data)

# Convert PCA result to a DataFrame for easier handling
pca_df = pd.DataFrame(pca_result, columns=[f'PC{i+1}' for i in range(pca_result.shape[1])])

# Plotting the PCA result
plt.figure(figsize=(8, 6))
plt.scatter(pca_df['PC1'], pca_df['PC2'])
plt.title('PCA Result')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid(True)

# Save the figure as SVG (compatible with Visio)
plt.savefig('pca_result_neg.svg', format='svg')

plt.show()