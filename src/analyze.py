import pandas as pd
import matplotlib.pyplot as plt
from clean_data import clean_data

df = clean_data("data/sales.csv")

# Total revenue
total_revenue = df['revenue'].sum()
print("Total Revenue:", total_revenue)

# Revenue by product
revenue_by_product = df.groupby('product')['revenue'].sum()
print("\nRevenue by Product:\n", revenue_by_product)

# Plot
revenue_by_product.plot(kind='bar')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.savefig("outputs/revenue_chart.png")

plt.show()