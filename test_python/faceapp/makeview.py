import numpy as np
import pandas as pd

import os

import codecs

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import plotly.graph_objects as go

df_images = pd.read_csv(
    r'C:\Users\nakamura.yo\Documents\test_python\faceapp\outputfiles\storeimages.csv')

df_detectapi = pd.read_csv(
    r'C:\Users\nakamura.yo\Documents\test_python\faceapp\outputfiles\detectapi.csv')

df_images['key'] = df_images['image_url'].str.rsplit('/', 1).str[1]
df_detectapi['key'] = df_detectapi['file_path'].str.rsplit('\\', 1).str[1]


# print(df_images)
# df_images.to_csv(r'C:\Users\nakamura.yo\Documents\test_python\faceapp\outputfiles\view.csv')

df_view = df_images.merge(df_detectapi, how='left', on='key')

df_view = df_view.sort_values(
    'beauty_female', ascending=False, na_position='last')

df_view = df_view.loc[:, ['name', 'beauty_female', 'age']]

# print(df_view)

# print(df_view.info())

df_view.to_csv(
    r'C:\Users\nakamura.yo\Documents\test_python\faceapp\outputfiles\view.csv')


'''
fig, ax = plt.subplots(figsize=((len(df_view.columns) + 1) * 1.2, (len(df_view) + 1) * 0.4))
ax.axis('off')

tbl = ax.table(cellText=df_view.values, bbox=[0, 0, 1, 1], colLabels=df_view.columns)
plt.show()
'''
