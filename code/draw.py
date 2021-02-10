# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point
from geopy.distance import distance, lonlat
import math
import os

# %%
file_path = os.path.join(os.getcwd(), 'data', 'output_data', 'v_boundary.shp')
Victoria = gpd.read_file(file_path)
Victoria.plot()

# %%
fire_data = pd.read_csv(
    os.path.join(os.getcwd(), 'data', 'output_data', 'output_fire_data',
                 'clustering_fire_data.csv'))

filename = "first_model_data.npy"
data_path = os.path.join(os.getcwd(), 'code', filename)
location_data = np.load(data_path)

# %%
fig, ax = plt.subplots()
ax.grid()
ax.set_aspect('equal')
fe = ax.scatter(x=fire_data['longitude'],
                y=fire_data['latitude'],
                s=fire_data['frp'] / 2,
                marker='o',
                color='red')

# ax.scatter(x=drone_cors[:,0],y=drone_cors[:,1],marker='o',s=120,c='white',edgecolor='blue')
dp = ax.scatter(x=location_data[:, 0],
                y=location_data[:, 1],
                marker='o',
                s=240,
                c='white',
                edgecolor='blue',
                alpha=0.4)
ax.set(xlabel='longtitude(°)',
       ylabel='latitude(°)',
       title='positions of UAVs and fire event points')
ax.legend((fe, dp), ("fire event points", "UAVs"))
plt.show()
# %%

# %%

# %%
