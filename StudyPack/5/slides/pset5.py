import pandas as pd

# Load and filter the data first
df_cpu = pd.read_csv("cpu.csv", usecols=['Image', 'PID', 'Description', 'Status', 'Threads', 'Average CPU'])
df_disk = pd.read_csv("disk.csv", usecols=['Image', 'PID', 'Total Byte Per Second'])
df_memory = pd.read_csv("memory.csv", usecols=['Image', 'PID', 'Working Set KB'])

# Display shape and info for each DataFrame
print("CPU DataFrame:")
print(df_cpu.shape)
df_cpu.info()
print("\n")

print("Disk DataFrame:")
print(df_disk.shape)
df_disk.info()
print("\n")

print("Memory DataFrame:")
print(df_memory.shape)
df_memory.info()

# Define the function for cleaning column names
def clean_column_headings(dfx):
    """Standardizes column names to lowercase and replaces spaces with underscores."""
    dfx.columns = dfx.columns.str.lower().str.replace(' ', '_')
    return dfx

# Apply the function directly to the loaded datasets
df_cpu = clean_column_headings(df_cpu)
df_disk = clean_column_headings(df_disk)
df_memory = clean_column_headings(df_memory)

# Examples of changes
print("CPU DataFrame columns:", df_cpu.columns)
print("Disk DataFrame columns:", df_disk.columns)
print("Memory DataFrame columns:", df_memory.columns)

