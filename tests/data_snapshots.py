import pickle

test_dir = 'tbd/static/files/'

with open(test_dir + 'default_df.pkl', 'rb') as df_obj_file:
    default_df = pickle.load(df_obj_file)
with open(test_dir + 'default_df_attr.pkl', 'rb') as df_obj_file:
    default_df_attr = pickle.load(df_obj_file)
