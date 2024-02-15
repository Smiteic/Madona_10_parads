import csv

# Open the CSV file in read mode
with open('data.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    
    # Skip the header row
    next(reader)
    
    # Print the fourth column of each row
    for row in reader:
        print(row[3])