import os
import pandas as pd
import numpy as np

csv_file = os.path.join(os.path.dirname(__file__), "Housing.csv")
df = pd.read_csv(csv_file)
df = df.select_dtypes(include=[np.number])
print(df.head())
