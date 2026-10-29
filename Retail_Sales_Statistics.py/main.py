import pandas as pd

data = pd.read_csv("sales_data.csv")

print("Mean Sales:", data["Sales"].mean())
print("Median Sales:", data["Sales"].median())
print("Mode Sales:", data["Sales"].mode()[0])
print("Standard Deviation:", data["Sales"].std())
print("Variance:", data["Sales"].var())
print("\nCategory-wise Sales:")

category_sales = data.groupby("Category")["Sales"].sum()

print(category_sales)

print("\nCategory-wise Profit:")

category_profit = data.groupby("Category")["Profit"].sum()

print(category_profit)
import matplotlib.pyplot as plt

category_sales = data.groupby("Category")["Sales"].sum()

category_sales.plot(kind="bar")

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()
# Correlation Analysis

correlation = data["Sales"].corr(data["Profit"])

print("Correlation between Sales and Profit:", correlation)

if correlation > 0:
    print("Sales and Profit have a positive relationship.")
elif correlation < 0:
    print("Sales and Profit have a negative relationship.")
else:
    print("There is no linear correlation.")
# Scatter Plot: Sales vs Profit

plt.scatter(data["Sales"], data["Profit"])

plt.title("Sales vs Profit Relationship")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()
# Data Cleaning

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDuplicate Rows:")
print(data.duplicated().sum())

print("\nDataset Information:")
print(data.info())
# Business Insights

print("\n--- Business Insights ---")

print("Total Sales:", data["Sales"].sum())
print("Total Profit:", data["Profit"].sum())
print("Total Orders:", data["Order_ID"].nunique())

best_category = data.groupby("Category")["Sales"].sum().idxmax()
print("Best Selling Category:", best_category)

profit_margin = data["Profit"].sum() / data["Sales"].sum() * 100
print("Overall Profit Margin:", round(profit_margin, 2), "%")
# Statistical Summary

print("\n--- Statistical Summary ---")
print(data[["Sales", "Profit", "Quantity"]].describe())

# Average Profit by Category

print("\n--- Average Profit by Category ---")
print(data.groupby("Category")["Profit"].mean())

# Highest Profit Order

highest_profit = data.loc[data["Profit"].idxmax()]

print("\n--- Highest Profit Order ---")
print(highest_profit)
# Final Project Summary

print("\n===== RETAIL SALES ANALYSIS REPORT =====")

print("Total Orders:", data["Order_ID"].nunique())
print("Total Sales:", data["Sales"].sum())
print("Total Profit:", data["Profit"].sum())

print("\nSales by Category:")
print(data.groupby("Category")["Sales"].sum())

print("\nProfit by Category:")
print(data.groupby("Category")["Profit"].sum())

print("\nAverage Order Value:", round(data["Sales"].mean(), 2))
print("Average Profit per Order:", round(data["Profit"].mean(), 2))