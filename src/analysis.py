import pandas as pd

# Load sales data
df = pd.read_csv("../data/sales_data.csv", parse_dates=["order_date"])

# Feature engineering: revenue per order
df["revenue"] = df["quantity"] * df["unit_price"]

print("Dataset with Revenue Column:")
print(df.head())

# KPI 1: Total Revenue
total_revenue = df["revenue"].sum()
print("\nTotal Revenue:", total_revenue)

# KPI 2: Revenue by Region
revenue_by_region = df.groupby("region")["revenue"].sum().reset_index()
print("\nRevenue by Region:")
print(revenue_by_region)

# KPI 3: Revenue by Product
revenue_by_product = df.groupby("product")["revenue"].sum().reset_index()
print("\nRevenue by Product:")
print(revenue_by_product)

import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# -----------------------------
# Chart 1: Revenue by Region
# -----------------------------
plt.figure()
sns.barplot(data=revenue_by_region, x="region", y="revenue")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("../outputs/charts/revenue_by_region.png")
plt.close()

# -----------------------------
# Chart 2: Revenue by Product
# -----------------------------
plt.figure()
sns.barplot(data=revenue_by_product, x="product", y="revenue")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("../outputs/charts/revenue_by_product.png")
plt.close()

print("\nCharts saved in outputs/charts/")
