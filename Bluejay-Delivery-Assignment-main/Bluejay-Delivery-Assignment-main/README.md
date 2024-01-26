# Bluejay-Delivery-Assignment

This Python script analyzes employee work data from a CSV file and categorizes employees based on specific criteria. The script identifies employees who have:

1. **Worked for 7 Consecutive Days:** Employees who have worked for seven consecutive days without a break.

2. **Less Than 10 Hours but Greater Than 1 Hour Between Shifts:** Employees who have less than 10 hours but greater than 1 hour between shifts.

3. **Worked for More Than 14 Hours in a Single Shift:** Employees who have worked for more than 14 hours in a single shift.

## How to Use

1. **Clone the Repository:**
  ```
git clone <repository_url>
  ```
2. **Run the Script:**
- Make sure you have Python installed on your system.
- Navigate to the repository directory and run the script:
  ```
  python analyze_work.py
  ```
- The script will prompt you to enter the path to the CSV file.

3. **Output:**
- The script will generate an output containing the categorized employee names.

## Files in the Repository

- `python-scrpit.py`: Python script for analyzing employee work data.
- `Assignment_Timecard.xlsx - Sheet1.csv`: Sample CSV file containing employee work data.
- `output.txt`: Output file containing categorized employee names.

## Dependencies

- Python 3.x
- `pandas` library: Install using `pip install pandas`

