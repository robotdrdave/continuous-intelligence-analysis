import tracking
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

data = pd.read_csv("/Users/robotdrdave/git/continuous-intelligence-workshop/data/raw/store47-2016.csv", index_col=0)

print("Data has ", len(data), " entries")
print("Column names: ", data.columns)
plt.hist(data['unit_sales'], bins=range(0,1000,20))
plt.xlabel('Unit Sales')
plt.ylabel('Count')
plt.title('Distribution of Unit Sales')
plt.savefig('/Users/robotdrdave/Documents/test.png')
plt.close()

with tracking.track() as track:
        track.log_params({'metrics': str(data.describe().to_dict())})
        track.log_artifact('/Users/robotdrdave/Documents/test.png')
