import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('meteorite_landings.csv')

# Drop rows with missing latitude or longitude
df.dropna(subset=['reclat', 'reclong'], inplace=True)

# Convert longitudes greater than 180 (fix longitude range)
df.loc[df['reclong'] > 180, 'reclong'] -= 360

# California boundaries
lat_min, lat_max = 32.5, 42.0
lon_min, lon_max = -124.5, -114.1

# Filter for meteorites in California
df_ca = df[(df['reclat'] >= lat_min) & (df['reclat'] <= lat_max) &
           (df['reclong'] >= lon_min) & (df['reclong'] <= lon_max)]

# Load USA states map
usa = gpd.read_file("https://www2.census.gov/geo/tiger/GENZ2020/shp/cb_2020_us_state_5m.zip")

# Filter for California only
california = usa[usa['STUSPS'] == 'CA']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Plot California map
california.plot(ax=ax, color='lightgray', edgecolor='black')

# Plot meteorite landings in California
ax.scatter(df_ca['reclong'], df_ca['reclat'], 
           s=20, color='red', alpha=0.6)  # Adjust size & transparency

# Labels and title
ax.set_title("Meteorite Landings in California", fontsize=14)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

# Save as PDF
plt.savefig("meteorite_map_california.pdf", format="pdf", bbox_inches="tight", dpi=300)

# Show the plot
plt.show()
