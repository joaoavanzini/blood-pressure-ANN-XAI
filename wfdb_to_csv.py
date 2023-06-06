import wfdb
import csv

# Load the WFDB record
record = wfdb.rdrecord('path/to/record')

# Get the signal data
signal_data = record.p_signal

# Get the field names for the CSV file
field_names = record.sig_name

# Write the signal data to a CSV file
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the field names as the first row of the CSV file
    writer.writerow(field_names)
    
    # Write each row of signal data to the CSV file
    for row in signal_data:
        writer.writerow(row)
