#%%
import csv
import pandas as pd
import os



#%%
os.chdir('./')
df = pd.read_csv("C:/ws/schema-annotation-workspace/schema_annotation/Storage/soccer_dataset.csv")

#%%
df.to_json("soccer_dataset.json")

#%%
