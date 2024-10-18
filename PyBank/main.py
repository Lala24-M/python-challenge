# Import libraries
import csv  # To read CSV files
import os   # To manage file paths

# Set the path
file_path = os.path.join('Resources', 'budget_data.csv')

# Declare variables to start with empty numbers
month_count = 0  # Number of months in the data
profit_total = 0  # Sum of all the profits/losses
last_month_profit = None  # Profit from the previous month to calculate difference

# Lists to hold profit changes and the corresponding months
profit_changes = []  
change_months = []

# Track the biggest increase and decrease in profits
biggest_gain = {"month": "", "amount": float('-inf')}  # Start very low
biggest_loss = {"month": "", "amount": float('inf')}   # Start very high

# Open the data file to read it
with open(file_path) as data_file:
    # Create a reader to go through each row
    csv_reader = csv.reader(data_file)
    next(csv_reader)  # Skip the first row (the header)

    # Loop through the rows in the data
    for row in csv_reader:
        # Get the month name and profit value from the row
        month_name = row[0]  
        profit_amount = int(row[1])  

        # Add to the month count and the total profit
        month_count += 1  
        profit_total += profit_amount  

        # If this isn't the first row, find the change in profit
        if last_month_profit is not None:
            profit_change = profit_amount - last_month_profit  # Calculate difference
            profit_changes.append(profit_change)  # Save the change
            change_months.append(month_name)  # Save the month

            # See if this is the biggest gain so far
            if profit_change > biggest_gain["amount"]:
                biggest_gain = {"month": month_name, "amount": profit_change}

            # See if this is the biggest loss so far
            if profit_change < biggest_loss["amount"]:
                biggest_loss = {"month": month_name, "amount": profit_change}

        # Save this month’s profit for the next loop
        last_month_profit = profit_amount  

# Find the average change by dividing total changes by the number of changes
average_profit_change = sum(profit_changes) / len(profit_changes)

# Create a summary report as a text block
report = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {month_count}\n"
    f"Total: ${profit_total}\n"
    f"Average Change: ${average_profit_change:.2f}\n"
    f"Greatest Increase in Profits: {biggest_gain['month']} (${biggest_gain['amount']})\n"
    f"Greatest Decrease in Profits: {biggest_loss['month']} (${biggest_loss['amount']})\n"
)

# Print the report
print(report)

# Set the path to save the report
save_path = os.path.join('analysis', 'financial_report.txt')

# Save the report to file
with open(save_path, 'w') as save_file:
    save_file.write(report)  # Write the report to the file
