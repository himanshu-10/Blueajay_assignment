import pandas as pd

# Prompt user for file path
file_path = "/Users/bhavyrahangdale/Downloads/Assignment_Timecard.xlsx - Sheet1.csv"

# Read the CSV file and let pandas infer datetime format
data = pd.read_csv(file_path, parse_dates=['Time', 'Time Out', 'Pay Cycle Start Date', 'Pay Cycle End Date'], infer_datetime_format=True)

# Initialize empty lists for different categories
consecutive_seven_days = []
less_than_10_hours = []
more_than_14_hours = []

# Check conditions and categorize employees
for index, row in data.iterrows():
    # Check for 7 consecutive days
    if (data['Time'][index + 6:index - 1:-1] - data['Time Out'][index + 7:index][::-1]).dt.days.sum() == 7:
        consecutive_seven_days.append(data['Employee Name'][index])
    
    # Check for less than 10 hours between shifts but greater than 1 hour
    if index > 0 and (row['Time'] - data['Time Out'][index - 1]).seconds / 3600 > 1 and (row['Time'] - data['Time Out'][index - 1]).seconds / 3600 < 10:
        less_than_10_hours.append(data['Employee Name'][index])
    
    # Check for more than 14 hours in a single shift
    if (row['Time Out'] - row['Time']).seconds / 3600 > 14:
        more_than_14_hours.append(data['Employee Name'][index])

# Print the results
print("Employees who have worked for 7 consecutive days:")
if consecutive_seven_days:
    print(consecutive_seven_days)
else:
    print("No employee found.")

print("\nEmployees who have less than 10 hours but greater than 1 hour between shifts:")
if less_than_10_hours:
    print(less_than_10_hours)
else:
    print("No employee found.")

print("\nEmployees who have worked for more than 14 hours in a single shift:")
if more_than_14_hours:
    print(more_than_14_hours)
else:
    print("No employee found.")
