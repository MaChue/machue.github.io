# Pricing strategies: How does pricing vary across different neighbourhoods, and how is it related to the number of reviews and the room type?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.metrics import silhouette_score

# 1. Data Loading and Exploration
# Load the data
df = pd.read_csv('AB_NYC_2019.csv')

# Explore the data
print("\n\n# Detail Info of AB_NYC_2019 dataset")
print(df.info())
print("\n-----------------------------------------------------------------\n\n")

# 2. Data Preprocessing
# Subset of required data
ds = df[['price', 'neighbourhood', 'neighbourhood_group', 'number_of_reviews', 'room_type']]
print("# Detail Info of Required Data")
print(ds.info())
print("\n-----------------------------------------------------------------\n\n")

print("# Check Missing Values")
print(ds.isnull().sum())
print("\n-----------------------------------------------------------------\n\n")

# Drop rows with missing values (if any)
ds = ds.dropna()

print("# Check for duplicates")
print(ds.duplicated().sum())
print("\n-----------------------------------------------------------------\n\n")

# Drop duplicates (if any)
ds = ds.drop_duplicates()

# Check for outliers in 'price' and 'number_of_reviews' 
Q1 = ds[['price', 'number_of_reviews']].quantile(0.25)
Q3 = ds[['price', 'number_of_reviews']].quantile(0.75)
IQR = Q3 - Q1
ds = ds[~((ds[['price', 'number_of_reviews']] < (Q1 - 1.5 * IQR)) | (ds[['price', 'number_of_reviews']] > (Q3 + 1.5 * IQR))).any(axis=1)]
print("# Descriptive Statistics of Price and Number of Reviews")
print(ds.describe())
print("\n-----------------------------------------------------------------\n\n")

""" 
# 3. Data Visualisation
# Boxplot for price variation across different neighborhoods group
plt.figure(figsize=(12, 6))
sns.boxplot(x='neighbourhood_group', y='price', data=ds)
plt.title('Price Variation Across Neighborhood Group')
plt.show()

# Barplot for average price across different neighborhoods
avg_price_neighbourhood = ds.groupby('neighbourhood_group')['price'].mean().sort_values(ascending=False)
avg_price_neighbourhood.plot(kind='bar', figsize=(12, 6))
plt.title('Average Price Across Neighborhood Groups')
plt.ylabel('Average Price')
plt.show()

# Scatterplot showing the relationship between the number of reviews and the price
sns.scatterplot(data=ds, x="price", y="number_of_reviews")
plt.show()
"""

# -----------------------------------------------------------------

# 4. Statistical Analysis
print("# Transform 'neighbourhood', 'neighbourhood_group' and 'room_type' columns into numeric")
labelencoder = LabelEncoder()
ds['neighbourhood'] = labelencoder.fit_transform(ds['neighbourhood'])
ds['neighbourhood_group'] = labelencoder.fit_transform(ds['neighbourhood_group'])
ds['room_type'] = labelencoder.fit_transform(ds['room_type'])
print(ds.info())
print("\n-----------------------------------------------------------------\n\n")

print("# Descriptive Statistics")
print(ds.describe(include='all'))
print("\n-----------------------------------------------------------------\n\n")

print("# Correlation Matrix")
print(ds.corr())
print("\n-----------------------------------------------------------------\n\n")

"""
# Perform Silhouette Method to know how many cluster is the best
sil = []
K = range(2,10)
# dissimilarity would not be defined for a single cluster, thus, minimum number of clusters should be 2
for k in K:
  kmeans = KMeans(n_clusters = k).fit(ds)
  labels = kmeans.labels_
  sil.append(silhouette_score(ds, labels, metric = 'euclidean'))

# Plotting silhouette scores 
plt.plot(K, sil, 'bx-')
plt.xlabel('k')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Method showing the optimal k')
plt.show()
"""

# Normalize the data
scaler = StandardScaler()
ds_scaled = scaler.fit_transform(ds)

# Perform K-means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(ds_scaled)

print("# Add the cluster labels for each data point to the dataframe")
ds['cluster_label'] = kmeans.labels_
print(ds.head())
print("\n-----------------------------------------------------------------\n\n")

# Get the cluster centers
centers = scaler.inverse_transform(kmeans.cluster_centers_)

# Create a DataFrame for easy visualization
cluster_centers = pd.DataFrame(centers, columns=ds.columns[:-1])

print("# See the cluster centers")
print(cluster_centers)
print("\n-----------------------------------------------------------------\n\n")