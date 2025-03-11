import pandas as pd 

# Load the CSV file into a Pandas DataFrame
file_path = "cpu.csv"
df_cpu = pd.read_csv(file_path)

# Extract the specified columns (Image, PID, Total Byte
df_cpu = df_cpu[['Image', 'PID', 'Description', 'Status', 'Threads', 'Average CPU']]

# Load disk.csv into a DataFrame and extract specified columns (Image, PID, Total Byte Per Second)
df_disk = pd.read_csv("disk.csv")
df_disk = df_disk[['Image', 'PID', 'Total Byte Per Second']]

# Load memory.csv into a DataFrame and extract specified columns (Image, PID, Working Set KB)
df_memory = pd.read_csv("memory.csv")
df_memory = df_memory[['Image', 'PID', 'Working Set KB']]

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

# Function to clean column names
def CleanColumnHeading(dfx):
    """
    Cleans the column names:
    - Converts all column names to lowercase.
    - Replaces spaces with underscores.
    """
    dfx.columns = dfx.columns.str.lower().str.replace(' ', '_')
    return dfx

# Load datasets
df_cpu = pd.read_csv("cpu.csv")
df_disk = pd.read_csv("disk.csv")
df_memory = pd.read_csv("memory.csv")

# Apply the function to each data frame
df_cpu = CleanColumnHeading(df_cpu)
df_disk = CleanColumnHeading(df_disk)
df_memory = CleanColumnHeading(df_memory)

# Examples of changes
print("CPU DataFrame columns:", df_cpu.columns)
print("Disk DataFrame columns:", df_disk.columns)
print("Memory DataFrame columns:", df_memory.columns)

# Function to clean numeric columns
def clean_numeric_column(dfx, column_name):
    """
    Converts a column to numeric by:
    - Removing commas (e.g., "71,807" → "71807")
    - Converting to float or int
    - Dropping invalid values
    """
    dfx[column_name] = dfx[column_name].astype(str).str.replace(',', '')  # Remove commas
    dfx[column_name] = pd.to_numeric(dfx[column_name], errors='coerce')  # Convert to number
    before_drop = len(dfx)
    dfx = dfx.dropna(subset=[column_name])  # Drop rows with invalid values
    after_drop = len(dfx)

  # Show examples of modified rows (if any rows were dropped)
    if before_drop != after_drop:
        print(f"Modified rows in {column_name} (before dropping NaN values):")
        print(dfx[[column_name]].head())
    
    return dfx

# Clean 'threads' column in df_cpu
df_cpu = clean_numeric_column(df_cpu, 'threads')

# Clean 'total_byte_per_second' column in df_disk
df_disk = clean_numeric_column(df_disk, 'total_byte_per_second')

# Clean 'working_set_kb' column in df_memory
df_memory = clean_numeric_column(df_memory, 'working_set_kb')

# Display updated DataFrame info
print("\nCPU DataFrame Info:")
df_cpu.info()

print("\nDisk DataFrame Info:")
df_disk.info()

print("\nMemory DataFrame Info:")
df_memory.info()

# Function to aggregate data dynamically based on dataset type
def aggregate_data(dfx):
    """
    Aggregates the given dataframe based on its dataset type:
    - df_cpu: Groups by 'image', sums 'threads', and counts occurrences.
    - df_disk: Groups by 'image', sums 'total_byte_per_second', and counts occurrences.
    - df_memory: Groups by 'image', sums 'working_set_kb', and counts occurrences.
    """
    # Identify dataset type based on columns
    if 'threads' in dfx.columns:
        df_combo = dfx.groupby('image').agg(
            process_qty=('image', 'size'),
            threads_sum=('threads', 'sum')
        ).reset_index()
        df_combo.rename(columns={'image': 'image_name'}, inplace=True)
    
    elif 'total_byte_per_second' in dfx.columns:
        df_combo = dfx.groupby('image').agg(
            process_qty=('image', 'size'),
            total_byte_sum=('total_byte_per_second', 'sum')
        ).reset_index()
        df_combo.rename(columns={'image': 'image_name'}, inplace=True)
    
    elif 'working_set_kb' in dfx.columns:
        df_combo = dfx.groupby('image').agg(
            process_qty=('image', 'size'),
            working_set_sum=('working_set_kb', 'sum')
        ).reset_index()
        df_combo.rename(columns={'image': 'image_name'}, inplace=True)
    
    else:
        raise ValueError("Unknown dataset structure. Unable to aggregate.")

    return df_combo

# Apply the aggregation function to each dataset
df_cpu_sum = aggregate_data(df_cpu)
df_disk_sum = aggregate_data(df_disk)
df_memory_sum = aggregate_data(df_memory)

# Print head(10) and tail(10) for each aggregated dataframe
print("\nCPU Aggregated Data:")
print(df_cpu_sum.head(10))
print(df_cpu_sum.tail(10))

print("\nDisk Aggregated Data:")
print(df_disk_sum.head(10))
print(df_disk_sum.tail(10))

print("\nMemory Aggregated Data:")
print(df_memory_sum.head(10))
print(df_memory_sum.tail(10))

# Merge df_cpu_sum and df_disk_sum on 'image_name' using an inner join
df_new = pd.merge(df_cpu_sum, df_disk_sum, on='image_name', how='inner')

# Display the merged DataFrame after first merge
print("Merged CPU and Disk Data (first 10 rows):")
print(df_new.head(10))
print(df_new.info())  # Show DataFrame structure

# Merge df_new with df_memory_sum on 'image_name' using an inner join
df_new = pd.merge(df_new, df_memory_sum, on='image_name', how='inner')

# Display the final merged DataFrame
print("\nFinal Merged Data (first 10 rows):")
print(df_new.head(10))
print(df_new.info())  # Show DataFrame structure

# Filter for 'working_set_sum' greater than 200,000
high_memory_image = df_new[df_new['working_set_sum'] > 200000]

# Filter for 'threads_sum' greater than 200
high_thread_image = df_new[df_new['threads_sum'] > 200]

# Filter for 'working_set_sum' > 200,000, 'threads_sum' < 50, and 'total_byte_sum' < 7,000
hi_mem_low_thread_low_io = df_new[
    (df_new['working_set_sum'] > 200000) & 
    (df_new['threads_sum'] < 50) & 
    (df_new['total_byte_sum'] < 7000)
]

# Display the results
print("High Memory Image:")
print(high_memory_image)

print("\nHigh Thread Image:")
print(high_thread_image)

print("\nHigh Memory, Low Thread, Low IO:")
print(hi_mem_low_thread_low_io)