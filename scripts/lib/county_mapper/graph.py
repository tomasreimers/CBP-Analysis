from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.patches import PathPatch
import numpy as np
import os

# Define constants
SHAPEFILE = os.path.join(os.path.dirname(__file__), "../../../data/shape_files/us_counties/us_counties")
WATER_COLOR = "#999999"
COLOR_MAP = plt.get_cmap("inferno")
NO_DATA_COLOR = COLOR_MAP(0.)
CURVE_BY = 0.25
ALPHA = 1

# Get axis to draw data
fig = plt.figure()
ax = fig.add_subplot(111)

# normalize dict
def normalize_dict(data_dict):
    max_val = max(data_dict.values())
    return {k: (float(v) / max_val) ** CURVE_BY for k, v in data_dict.iteritems()}

# get colors from the colormap, val should be [0, 1]
def lower_alpha(a):
    l = list(a)
    l[3] = ALPHA
    return tuple(l)

def get_color(n):
    if n == -1:
        return lower_alpha(NO_DATA_COLOR)
    return lower_alpha(COLOR_MAP(float(n)))

# the data_dict should be structured {(fipstate, fipscty): value}
def graph(data_dict):
    # normalize data
    norm_data_dict = normalize_dict(data_dict)

    # Set up the basic map
    map = Basemap()
    map.drawmapboundary(fill_color=WATER_COLOR)
    # map.fillcontinents(color='#ddaa66',lake_color=WATER_COLOR)

    # Read in the counties
    map.readshapefile(SHAPEFILE, 'us_counties', drawbounds = False)

    for info, shape in zip(map.us_counties_info, map.us_counties):
        ax.add_patch(
            Polygon(
                np.array(shape),
                True,
                facecolor=get_color(
                    norm_data_dict.get(
                        (info['STATEFP'], info['COUNTYFP']),
                        -1
                    )
                ),
                edgecolor='k',
                linewidth=1.
            )
        )

    plt.show()
