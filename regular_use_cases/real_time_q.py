# Python Data Engineering UseCase:
# --------------------------------
# Python Programme related to data engineering that focuses on handling CSV files, along with a relevant business use case:
# Use Case: E-commerce Sales Analysis
# An e-commerce company wants to analyze its sales data to improve inventory management and customer satisfaction. They have a CSV file (sales_data.csv) with the following structure:

# sales_data.csv:
# OrderID, ProductID, ProductName, QuantitySold, SaleDate, CustomerID, Price
# 1, 101, Widget A, 2, 2024-10-01, C001, 10.00
# 2, 102, Widget B, 1, 2024-10-01, C002, 20.00
# 3, 101, Widget A, 1, 2024-10-02, C001, 10.00
# 4, 103, Widget C, 3, 2024-10-02, C003, 15.00
# 5, 102, Widget B, 2, 2024-10-03, C004, 20.00

# data = {
#     "OrderID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
#     "ProductID": [101, 102, 101, 103, 102, 101, 104, 101, 105, 102, 103, 104, 106, 102, 105],
#     "ProductName": [
#         "Widget A", "Widget B", "Widget A", "Widget C", "Widget B", 
#         "Widget A", "Widget D", "Widget A", "Widget E", "Widget B", 
#         "Widget C", "Widget D", "Widget F", "Widget B", "Widget E"
#     ],
#     "QuantitySold": [2, 1, 1, 3, 2, 4, 5, 3, 2, 3, 2, 1, 3, 4, 2],
#     "SaleDate": [
#         "2024-10-01", "2024-10-01", "2024-10-02", "2024-10-02", 
#         "2024-10-03", "2024-10-04", "2024-10-05", "2024-10-06", 
#         "2024-10-06", "2024-10-07", "2024-10-07", "2024-10-08", 
#         "2024-10-09", "2024-10-10", "2024-10-10"
#     ],
#     "CustomerID": [
#         "C001", "C002", "C001", "C003", "C004", 
#         "C005", "C006", "C007", "C008", "C009", 
#         "C001", "C002", "C003", "C010", "C001"
#     ],
#     "Price": [10.00, 20.00, 10.00, 15.00, 20.00, 10.00, 25.00, 10.00, 30.00, 20.00, 15.00, 25.00, 35.00, 20.00, 30.00]
# }

# Task:

# Write a Python function that performs the following tasks:

#     1. Read the CSV file into a Pandas DataFrame.
    
#     2. Calculate the total sales for each product based on the QuantitySold and Price columns.
    
#     3. Identify the product with the highest sales and return its name, total sales amount, and the total quantity sold.
    
#     4. Filter the sales data to only include sales that occurred in the last week from todayâ€™s date (use datetime for date handling).
    
# Example Output:
# For instance, if today's date is 2024-10-04, the function should return:

# Product with highest sales: Widget A
# Total Sales Amount: $30.00
# Total Quantity Sold: 3

import pandas as pd
import logging  # Still using the built-in logging module
logging.basicConfig(level=logging.ERROR)

file_path = r'C:\ENV\PREP\DE_class\regular_use_cases\sales_data.csv'

try:
    df = pd.read_csv(file_path)
    print(df)
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

#df = pd.read_csv('C:\ENV\Virual_Env\DE_class\regular_use_cases\sales_data.csv.csv')

#df = pd.DataFrame('C:\ENV\Virual_Env\DE_class\regular_use_cases\sales_data.csv')
#df = pd.DataFrame(data)

