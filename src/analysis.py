import tracking
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

data = pd.read_csv("/Users/robotdrdave/git/continuous-intelligence-workshop/data/raw/store47-2016.csv")

print("Data has ", len(data), " entries")
print("Column names: ", data.columns)
print(os.getenv('MLFLOW_TRACKING_URL'))
with tracking.track() as track:
        track.log_metrics(data.describe().to_dict())
