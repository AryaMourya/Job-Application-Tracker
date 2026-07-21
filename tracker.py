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
    
