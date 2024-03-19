# DATA
import pandas as pd
try:
    df = pd.read_csv('stat.csv').set_index(['ADM1_EN', 'ADM2_EN'])
    'label' in df
except:
    df = pd.read_csv('stat.csv', sep=';').set_index(['ADM1_EN', 'ADM2_EN'])
    'label' in df

df['label'] = df['name'].fillna("").apply(lambda x: x.split("—")[0].strip())
print(df)
records = df.to_dict()

labels = records['label']

if 'color' in records:
    colors = records['color']
elif 'value' in records:
    values = records['value']
    colors = dict()
    color_info_ranges = pd.read_csv("colors.csv").to_dict('records')
    print(color_info_ranges)

    for key, value in values.items():
        for color_info in color_info_ranges:
            if color_info['min'] <= value < color_info['max']:
                colors[key] = color_info['color']
else:
    colors = dict()


# MAPS
import cartopy
import cartopy.crs as ccrs
import os
files = [file for file in os.listdir("map") if file.endswith(".shp")]
if len(files) == 0:
    print("NOT FOUND map/*.shp")
    exit(1)
if len(files) > 1:
    print("MANY FILES map/*.shp")
    exit(1)

print("LOAD MAP")
reader = cartopy.io.shapereader.Reader(os.path.join("map", files[0]))

# PLOT
import matplotlib.pyplot as plt
import sys
from  matplotlib.colors import LinearSegmentedColormap

plt.figure(figsize=(100,100))
ax = plt.subplot(111, projection=ccrs.LambertConformal())
ax.set_extent([5, 50, 20, 60])
cmap = plt.get_cmap('rainbow')

records = list(reader.records())
size = len(records)
districts_all = []
districts_not_found = []
for i, record in enumerate(records):
    region1 = record.attributes['ADM1_EN']
    region2 = record.attributes['ADM2_EN']
    if ',' in region2:
        print("MAP", region2)
        region2 = region2.split(',')[0].strip()
        print("REPLACE", region2)
    x = record.geometry.centroid.x        
    y = record.geometry.centroid.y

    name = (region1, region2)
    name_text = region1 + "," + region2
    label = labels.get(name, name_text)
    color = colors.get(name, 'white')

    ax.text(x, y, label, color='black', size=15, ha='center', va='center', transform=ccrs.LambertConformal())
    ax.add_geometries([record.geometry], ccrs.LambertConformal(), facecolor=color, edgecolor='black')

    districts_all.append(name_text)
    if name not in labels:
        districts_not_found.append(name_text)

plt.savefig("fig.png")
# plt.show()

# LOG ALL CODES
text = '\n'.join(sorted(districts_all))
open("districts_all.txt","w").write(text)
# print(text)

text = '\n'.join(sorted(districts_not_found))
open("districts_not_found.txt","w").write(text)
print("NOT FOUND", len(districts_not_found))
print(text)