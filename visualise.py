import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (for the sake of demonstration, we'll create a sample dataset)
# Assuming the dataset would look something like this
data = {
    'Temperature': np.random.normal(30, 5, 100), 
    'Rain': np.random.normal(100, 20, 100), 
    'Humidity': np.random.normal(60, 10, 100), 
    'Wind Speed': np.random.normal(10, 2, 100),
    'Oxygen': np.random.normal(21, 2, 100),
    'Fire_Risk': np.random.choice(['Low', 'High'], 100)
}

df = pd.DataFrame(data)

# Create a figure with multiple subplots
plt.figure(figsize=(14, 12))

# Pie Chart for Target Variable Distribution
plt.subplot(3, 2, 1)
plt.title('Pie Chart: Distribution of Fire Risk')
df['Fire_Risk'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#ff9999','#66b3ff'], startangle=90, wedgeprops=dict(width=0.3))
plt.ylabel('')  # Remove ylabel for better appearance

# Bar Graph for Average Feature Values
plt.subplot(3, 2, 2)
plt.title('Bar Chart: Average Feature Values')
feature_means = df[['Temperature', 'Rain', 'Humidity', 'Wind Speed', 'Oxygen']].mean()
feature_means.plot(kind='bar', color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ffb3e6'])
plt.xlabel('Features')
plt.ylabel('Average Value')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Histogram for Rain Distribution
plt.subplot(3, 2, 3)
plt.title('Histogram: Rain Distribution')
plt.hist(df['Rain'], bins=20, color='#ff9999', edgecolor='black')
plt.xlabel('Rain')
plt.ylabel('Frequency')

# Histogram for Temperature Distribution
plt.subplot(3, 2, 4)
plt.title('Histogram: Temperature Distribution')
plt.hist(df['Temperature'], bins=20, color='#66b3ff', edgecolor='black')
plt.xlabel('Temperature')
plt.ylabel('Frequency')

# Histogram for Wind Speed Distribution
plt.subplot(3, 2, 5)
plt.title('Histogram: Wind Speed Distribution')
plt.hist(df['Wind Speed'], bins=20, color='#99ff99', edgecolor='black')
plt.xlabel('Wind Speed')
plt.ylabel('Frequency')

# Histogram for Oxygen Distribution
plt.subplot(3, 2, 6)
plt.title('Histogram: Oxygen Distribution')
plt.hist(df['Oxygen'], bins=20, color='#ffcc99', edgecolor='black')
plt.xlabel('Oxygen')
plt.ylabel('Frequency')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Save the entire visualization to a file
plt.savefig('combined_visualization.png')

# Display the combined plot
plt.show()


