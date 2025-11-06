# Open a file in write mode
with open('output_values.txt', 'w') as file:
    # Write the first 15k rows with value 0
    for _ in range(249999):
        file.write('0\n')
    
    # Write the following 15k rows with value -1
    for _ in range(249999):
        file.write('64\n')

print("File generated successfully with 250k rows.")