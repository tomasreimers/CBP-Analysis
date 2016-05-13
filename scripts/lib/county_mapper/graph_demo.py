from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.patches import PathPatch
import numpy as np

# Define constants

SHAPEFILE = "../../data/shape_files/us_counties/us_counties"

# Get axis to draw data

fig = plt.figure()
ax = fig.add_subplot(111)

# Set up the basic map

map = Basemap()

map.drawmapboundary(fill_color='aqua')

# map.fillcontinents(color='#ddaa66',lake_color='aqua')
# map.drawcoastlines()

# Read in the counties

map.readshapefile(SHAPEFILE, 'us_counties', drawbounds = False)

for info, shape in zip(map.us_counties_info, map.us_counties):
    ax.add_patch( Polygon(np.array(shape), True, facecolor=("#990000" if int(info['COUNTYFP']) < 100 else "#FF0000"), edgecolor='k', linewidth=1.,) )

plt.show()
