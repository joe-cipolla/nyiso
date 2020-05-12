import pandas as pd
import os

proj_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = proj_dir.replace('/tests', '') + '/data/'

default_df = pd.read_csv(data_dir + 'default_df.csv')
