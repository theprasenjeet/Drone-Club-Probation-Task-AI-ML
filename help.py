###****Import Library****

import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.colors import n_colors
from plotly.subplots import make_subplots
init_notebook_mode(connected=True)
import cufflinks as cf
cf.go_offline()



###****Demo Import Dataset***

victims = pd.read_csv('/content/drive/MyDrive/ML Global/Victims_of_rape.csv')
police_hr = pd.read_csv('/content/drive/MyDrive/ML Global/Human_rights_violation_by_police.csv')
auto_theft = pd.read_csv('/content/drive/MyDrive/ML Global/Auto_theft.csv')
prop_theft = pd.read_csv('/content/drive/MyDrive/ML Global/Property_stolen_and_recovered.csv')


###******* Importing Map Shape File & Visualizing on Map ***********
### State/UT wise incest rape cases reported from 2001 to 2010


dataset_Variable = pd.DataFrame(inc_victims.groupby(['Area_Name'])['Rape_Cases_Reported'].sum().reset_index())
dataset_Variable.columns = ['State/UT','Cases Reported']
dataset_Variable.replace(to_replace='Arunachal Pradesh',value='Arunanchal Pradesh',inplace=True)

###Importing Map Shape File
shp_gdf = gpd.read_file('/content/drive/MyDrive/ML Global/Indian_States.shp')
merged = shp_gdf.set_index('st_nm').join(dataset_Variable.set_index('State/UT'))

### Visualizing
fig, ax = plt.subplots(1, figsize=(20, 20))
ax.axis('off')
ax.set_title('State-wise Rape-Cases Reported (2001-2010)',
             fontdict={'fontsize': '15', 'fontweight' : '3'})
fig = merged.plot(column='Cases Reported', cmap='Reds', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)




