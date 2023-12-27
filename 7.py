# 7. Explore the difference between iterrows(), itertuples(), apply(), map()
# Analyze the time taken for above operations using one wider dataset(large no of columns) and
# one taller dataset(Large no. of rows)
# Read dataset as pandas dataframe
import pandas as pd
import numpy as np
import time
def create_wider_dataset(num_rows, num_columns):
    data = np.random.rand(num_rows, num_columns)
    columns = [f"col_{i}" for i in range(num_columns)]
    df = pd.DataFrame(data, columns=columns)
    return df

def create_taller_dataset(num_rows, num_columns):
    data = np.random.rand(num_rows, num_columns)
    columns = [f"col_{i}" for i in range(num_columns)]
    df = pd.DataFrame(data, columns=columns)
    return df
wider_df = create_wider_dataset(1000, 100)
# print(wider_df)  
taller_df = create_taller_dataset(10000, 10)

# Time taken for iterrows() on wider dataset
start_time = time.time()
for index, row in wider_df.iterrows():
    pass
iterrows_time_wider = time.time() - start_time

# Time taken for iterrows() on taller dataset
start_time = time.time()
for index, row in taller_df.iterrows():
    pass
iterrows_time_taller = time.time() - start_time

# Time taken for itertuples() on wider dataset
start_time = time.time()
for row in wider_df.itertuples():
    pass
itertuples_time_wider = time.time() - start_time

# Time taken for itertuples() on taller dataset
start_time = time.time()
for row in taller_df.itertuples():
    pass
itertuples_time_taller = time.time() - start_time

# Time taken for apply() on wider dataset
start_time = time.time()
wider_df.apply(lambda row: row.sum(), axis=1)
apply_time_wider = time.time() - start_time

# Time taken for apply() on taller dataset
start_time = time.time()
taller_df.apply(lambda row: row.sum(), axis=1)
apply_time_taller = time.time() - start_time

# Time taken for map() on wider dataset
start_time = time.time()
wider_df["new_column"] = wider_df["col_0"].map(lambda x: x * 2)
map_time_wider = time.time() - start_time

# Time taken for map() on taller dataset
start_time = time.time()
taller_df["new_column"] = taller_df["col_0"].map(lambda x: x * 2)
map_time_taller = time.time() - start_time

print(f"iterrows() time on wider dataset: {iterrows_time_wider} seconds")
print(f"iterrows() time on taller dataset: {iterrows_time_taller} seconds")
print(f"itertuples() time on wider dataset: {itertuples_time_wider} seconds")
print(f"itertuples() time on taller dataset: {itertuples_time_taller} seconds")
print(f"apply() time on wider dataset: {apply_time_wider} seconds")
print(f"apply() time on taller dataset: {apply_time_taller} seconds")
print(f"map() time on wider dataset: {map_time_wider} seconds")
print(f"map() time on taller dataset: {map_time_taller} seconds")
