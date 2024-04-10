import os
import pandas as pd # type: ignore

# # Dữ liệu mẫu
# data = {
#    'TransactionID': [101, 102, 103,104, 105, 106, 107],
#     'ProductNumber': [1, 2, 3, 4, 5, 6, 7],
#     'ProductName': ['Product x', 'Product y', 'Product z, Product W', 'Product V', 'Product U', 'Product T'],
#     'OrderDate': ['2024-04-01', '2024-04-02', '2024-04-03, 2024-04-04', '2024-04-05', '2024-04-06', '2024-04-07'],
#     'Quantity': [10, 20, 30, 40, 50, 60, 70],
#     'UnitPrice': [50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 110.0],
#     'TotalPrice': [500.0, 1200.0, 2100.0, 3200.0, 4500.0, 6000.0, 7700.0]
# }

# Read data from CSV files
data = pd.read_csv('sales_data.csv', )

# # Tạo thư mục nếu chưa tồn tại
# os.makedirs('E:\\Download\\kỳ cuối\\mon thay dong\\asm2', exist_ok=True)



# Handle missing values
# Check for missing values
missing_values = data.isna().sum()
# Remove rows with missing values
data.dropna(inplace=True)

# Remove duplicate data
# Remove duplicate data based on all columns
data.drop_duplicates(inplace=True)

# Data normalization
# Normalize the 'ProductName' column to capitalize the first letter
data['ItemName'] = data['ItemName'].str.capitalize()

# Handle outliers
# Handle outliers in the 'Quantity' column
data = data[data['QuantitySold'] <= 100]

# Sort data by TransactionID column
data_sorted = data.sort_values(by='TransactionID')

# Lưu DataFrame vào tệp CSV
data.to_csv('sales_data.csv', index=False)
# Lưu DataFrame vào tệp CSV
data_sorted.to_csv('sales_data.csv', index=False)


print('Save to CSV file successfully.')