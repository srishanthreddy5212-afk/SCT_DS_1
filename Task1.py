import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("/content/API_SP.POP.TOTL_DS2_en_csv_v2_430662.csv", skiprows=4)

# Select the latest year available (change if needed)
year = '2022'

# Keep country name and population
pop_df = df[['Country Name', year]]

# Remove missing values
pop_df = pop_df.dropna()

# Get top 10 most populated countries
top10 = pop_df.sort_values(by=year, ascending=False).head(10)

# Create bar chart
plt.figure(figsize=(12,6))
plt.bar(top10['Country Name'], top10[year])
plt.title('Top 10 Most Populated Countries (2022)')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
