import pandas as pd
import glob

def load_all_hospitals(path="uploads/*.csv"):
    files = glob.glob(path)
    return pd.concat([pd.read_csv(f) for f in files])
