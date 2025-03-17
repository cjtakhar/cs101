import pandas as pd
import matplotlib.pyplot as plt

def load_and_clean_csv(file_path, columns):
    """
    Loads a CSV file, extracts specified columns, and cleans column names.
    """
    df = pd.read_csv(file_path, usecols=columns)
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

def clean_numeric_column(dfx, column_name):
    """
    Cleans and converts a numeric column by removing commas and converting to float.
    """
    dfx[column_name] = dfx[column_name].astype(str).str.replace(',', '')
    dfx[column_name] = pd.to_numeric(dfx[column_name], errors='coerce')
    return dfx.dropna(subset=[column_name])

def aggregate_data(dfx, group_by, sum_column):
    """
    Aggregates data by summing a numeric column and counting occurrences.
    """
    return dfx.groupby(group_by).agg(
        process_qty=(group_by, 'size'),
        sum_value=(sum_column, 'sum')
    ).reset_index().rename(columns={group_by: 'image_name', 'sum_value': sum_column + '_sum'})

# Load and clean datasets
df_cpu = load_and_clean_csv("cpu.csv", ['Image', 'PID', 'Threads'])
df_disk = load_and_clean_csv("disk.csv", ['Image', 'PID', 'Total Byte Per Second'])
df_memory = load_and_clean_csv("memory.csv", ['Image', 'PID', 'Working Set KB'])

# Convert numeric columns
df_cpu = clean_numeric_column(df_cpu, 'threads')
df_disk = clean_numeric_column(df_disk, 'total_byte_per_second')
df_memory = clean_numeric_column(df_memory, 'working_set_kb')

# Aggregate data
df_cpu_sum = aggregate_data(df_cpu, 'image', 'threads')
df_disk_sum = aggregate_data(df_disk, 'image', 'total_byte_per_second')
df_memory_sum = aggregate_data(df_memory, 'image', 'working_set_kb')

# Merge datasets
df_merged = df_cpu_sum.merge(df_disk_sum, on='image_name', how='inner')
df_merged = df_merged.merge(df_memory_sum, on='image_name', how='inner')

# Apply filters
high_memory = df_merged[df_merged['working_set_kb_sum'] > 200000]
high_threads = df_merged[df_merged['threads_sum'] > 200]
hi_mem_low_thread_low_io = df_merged[(df_merged['working_set_kb_sum'] > 200000) &
                                     (df_merged['threads_sum'] < 50) &
                                     (df_merged['total_byte_per_second_sum'] < 7000)]

# Display results
print("High Memory Processes:")
print(high_memory)
print("\nHigh Thread Processes:")
print(high_threads)
print("\nHigh Memory, Low Thread, Low IO Processes:")
print(hi_mem_low_thread_low_io)

# Visualization
plt.figure(figsize=(10, 6))
plt.bar(df_merged['image_name'][:10], df_merged['working_set_kb_sum'][:10])
plt.xticks(rotation=90)
plt.xlabel('Process')
plt.ylabel('Memory Usage (KB)')
plt.title('Top 10 Memory-Intensive Processes')
plt.show()
