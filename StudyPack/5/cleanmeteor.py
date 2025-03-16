import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('meteorite_landings.csv')

# Drop rows with missing latitude or longitude
df.dropna(subset=['reclat', 'reclong'], inplace=True)

# Convert longitudes greater than 180 (fix longitude range)
df.loc[df['reclong'] > 180, 'reclong'] -= 360

# Load world map manually
world = gpd.read_file("https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip")

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the world map
world.plot(ax=ax, color='lightgray', edgecolor='black')

# Plot meteorite landings
ax.scatter(df['reclong'], df['reclat'], 
           s=10, color='red', alpha=0.5)  # Adjust size & transparency

# Labels and title
ax.set_title("Meteorite Landings Around the World", fontsize=14)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

# Save as PDF
plt.savefig("meteorite_map.pdf", format="pdf", bbox_inches="tight", dpi=300)

# Show the plot
plt.show()
