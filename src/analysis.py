import tracking
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import mlflow

data = pd.read_csv("/Users/robotdrdave/git/continuous-intelligence-workshop/data/raw/store47-2016.csv", index_col=0)

print("Data has ", len(data), " entries")
print("Column names: ", data.columns)
plt.hist(data['unit_sales'], bins=range(0,1000,20))
plt.xlabel('Unit Sales')
plt.ylabel('Count')
plt.title('Distribution of Unit Sales')
plt.savefig('/Users/robotdrdave/Documents/Experiment_Artifacts/test.png')
plt.close()

#with tracking.track() as track:
#        track.log_params({'metrics': str(data.describe().to_dict())})
#        track.log_graph('/Users/robotdrdave/Documents/test.png')
MLFLOW_TRACKING_URL = os.getenv('MLFLOW_TRACKING_URL')
TENANT = os.getenv('TENANT','local')
RUN_LABEL = os.getenv('GO_PIPELINE_LABEL', '0')

mlflow.set_tracking_uri(uri=MLFLOW_TRACKING_URL)
#mlflow.create_experiment('histogram', '/Users/robotdrdave/Documents/go-agent-19.5.0/pipelines/analysis/mlruns')
mlflow.set_experiment('histogram')
mlflow.set_experiment(TENANT)
mlflow.start_run(run_name=RUN_LABEL)

mlflow.log_param('metrics', str(data.describe().to_dict()))
mlflow.log_artifact('/Users/robotdrdave/Documents/Experiment_Artifacts/test.png')
mlflow.end_run()
