#Job Application Tracker
import pandas as pd
import numpy as np
from datetime import datetime
import os

# define the CSV file path
DATA_FILE = "job_tracker.csv"

def load_tracker():
    if os.path.exist(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        # Creating new dataframe if file doesn't exist
        columns = ["Date Applied","Company","Job Title","Status","Platform","Location"]
        return pd.DataFrame(columns=columns)
    
### Add a New Application
def add_application(df, company, title, status, platform, location):
   new_app = pd.DataFrame({
       "Date Applied":[datetime.now().strftime("%Y-%m-%d")],
       "Company":[company],
       "Job Title":[title],
       "Status":[status],
       "Platform":[platform],
       "Location":[location]
   })
   updated_df = pd.concat([df,new_app],ignore_index=True)
   updated_df.to_csv(DATA_FILE,index=False)
   print(f"Added {title} at {company}.")
   return updated_df

### Analyzing with Pandas & Numpy 
def analyze_data(df):
    if df.empty:
        print("No job applications tracked yet.")
        return


df = load_tracker()
unique_statuses = df["Status"].unique()
