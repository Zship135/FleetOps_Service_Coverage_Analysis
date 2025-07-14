import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import contextily as ctx
from pyproj import Transformer

warehouse_data = [
    {"warehouse_id": "FO-CHI-001", "warehouse_name": "Chicago Central Hub", "city": "Chicago", "state": "Illinois", "latitude": 41.8781, "longitude": -87.6298, "max_delivery_radius": 75},
    {"warehouse_id": "FO-MIL-002", "warehouse_name": "Milwaukee Distribution", "city": "Milwaukee", "state": "Wisconsin", "latitude": 43.0389, "longitude": -87.9065, "max_delivery_radius": 65},
    {"warehouse_id": "FO-IND-003", "warehouse_name": "Indianapolis Central", "city": "Indianapolis", "state": "Indiana", "latitude": 39.7684, "longitude": -86.1581, "max_delivery_radius": 70},
    {"warehouse_id": "FO-STL-004", "warehouse_name": "St. Louis Gateway", "city": "St. Louis", "state": "Missouri", "latitude": 38.627, "longitude": -90.1994, "max_delivery_radius": 80},
    {"warehouse_id": "FO-DET-005", "warehouse_name": "Detroit Metro", "city": "Detroit", "state": "Michigan", "latitude": 42.3314, "longitude": -83.0458, "max_delivery_radius": 70},
    {"warehouse_id": "FO-MIN-006", "warehouse_name": "Minneapolis North", "city": "Minneapolis", "state": "Minnesota", "latitude": 44.9778, "longitude": -93.265, "max_delivery_radius": 75},
    {"warehouse_id": "FO-COL-007", "warehouse_name": "Columbus East", "city": "Columbus", "state": "Ohio", "latitude": 39.9612, "longitude": -82.9988, "max_delivery_radius": 65},
    {"warehouse_id": "FO-GRB-008", "warehouse_name": "Green Bay Regional", "city": "Green Bay", "state": "Wisconsin", "latitude": 44.5133, "longitude": -88.0133, "max_delivery_radius": 60},
    {"warehouse_id": "FO-KAN-009", "warehouse_name": "Kansas City West", "city": "Kansas City", "state": "Missouri", "latitude": 39.0997, "longitude": -94.5786, "max_delivery_radius": 85},
    {"warehouse_id": "FO-CLE-010", "warehouse_name": "Cleveland North", "city": "Cleveland", "state": "Ohio", "latitude": 41.4993, "longitude": -81.6944, "max_delivery_radius": 70},
    {"warehouse_id": "FO-DES-011", "warehouse_name": "Des Moines Central", "city": "Des Moines", "state": "Iowa", "latitude": 41.5868, "longitude": -93.625, "max_delivery_radius": 80},
    {"warehouse_id": "FO-GRA-012", "warehouse_name": "Grand Rapids West", "city": "Grand Rapids", "state": "Michigan", "latitude": 42.9634, "longitude": -85.6681, "max_delivery_radius": 70}
]

worst_cities_data = [
    {"City": "South Bend", "State": "Indiana", "Latitude": 41.6764, "Longitude": -86.252},
    {"City": "Niles", "State": "Michigan", "Latitude": 41.8297, "Longitude": -86.242},
    {"City": "Jackson", "State": "Michigan", "Latitude": 42.2459, "Longitude": -84.4013},
    {"City": "Logansport", "State": "Indiana", "Latitude": 40.7544, "Longitude": -86.3567},
    {"City": "Peru", "State": "Indiana", "Latitude": 40.7536, "Longitude": -86.0689},
    {"City": "Richmond", "State": "Indiana", "Latitude": 39.8289, "Longitude": -84.8902},
    {"City": "Mankato", "State": "Minnesota", "Latitude": 44.1636, "Longitude": -93.9993},
    {"City": "Kettering", "State": "Ohio", "Latitude": 39.7589, "Longitude": -84.1916},
    {"City": "Mount Pleasant", "State": "Michigan", "Latitude": 43.5978, "Longitude": -84.7675},
    {"City": "East Lansing", "State": "Michigan", "Latitude": 42.7369, "Longitude": -84.4838},
    {"City": "Willard", "State": "Ohio", "Latitude": 41.0531, "Longitude": -82.7263},
    {"City": "Janesville", "State": "Wisconsin", "Latitude": 42.6828, "Longitude": -89.0187},
    {"City": "Youngstown", "State": "Ohio", "Latitude": 41.0998, "Longitude": -80.6495},
    {"City": "Mansfield", "State": "Ohio", "Latitude": 40.7584, "Longitude": -82.5154},
    {"City": "West Lafayette", "State": "Indiana", "Latitude": 40.4259, "Longitude": -86.9081},
    {"City": "Huber Heights", "State": "Ohio", "Latitude": 39.8439, "Longitude": -84.1246},
    {"City": "St. Cloud", "State": "Minnesota", "Latitude": 45.5608, "Longitude": -94.1633},
    {"City": "Beavercreek", "State": "Ohio", "Latitude": 39.7092, "Longitude": -84.1624},
    {"City": "Adrian", "State": "Michigan", "Latitude": 41.8975, "Longitude": -84.0372},
    {"City": "Lafayette", "State": "Indiana", "Latitude": 40.4167, "Longitude": -86.8753},
    {"City": "Bucyrus", "State": "Ohio", "Latitude": 40.8084, "Longitude": -82.9757},
    {"City": "DeKalb", "State": "Illinois", "Latitude": 41.9295, "Longitude": -88.7503},
    {"City": "Seymour", "State": "Indiana", "Latitude": 38.9592, "Longitude": -85.8903},
    {"City": "Flint", "State": "Michigan", "Latitude": 43.0125, "Longitude": -83.6875},
    {"City": "Fond du Lac", "State": "Wisconsin", "Latitude": 43.7773, "Longitude": -88.4471},
    {"City": "Lansing", "State": "Michigan", "Latitude": 42.732536, "Longitude": -84.555534},
    {"City": "Beaver Dam", "State": "Wisconsin", "Latitude": 43.4578, "Longitude": -88.837},
    {"City": "Connersville", "State": "Indiana", "Latitude": 39.6412, "Longitude": -85.1411},
    {"City": "Galion", "State": "Ohio", "Latitude": 40.7339, "Longitude": -82.7899},
    {"City": "Ashland", "State": "Ohio", "Latitude": 40.8687, "Longitude": -82.3182},
    {"City": "Burton", "State": "Michigan", "Latitude": 42.9947, "Longitude": -83.6163},
    {"City": "Toledo", "State": "Ohio", "Latitude": 41.6528, "Longitude": -83.5379},
    {"City": "Sandusky", "State": "Ohio", "Latitude": 41.4487, "Longitude": -82.7085},
    {"City": "Zanesville", "State": "Ohio", "Latitude": 39.9403, "Longitude": -82.0132},
    {"City": "Marion", "State": "Ohio", "Latitude": 40.5581, "Longitude": -85.6592},
    {"City": "Canton", "State": "Ohio", "Latitude": 40.7989, "Longitude": -81.3797},
    {"City": "Norwalk", "State": "Ohio", "Latitude": 40.0581, "Longitude": -82.4013},
    {"City": "Battle Creek", "State": "Michigan", "Latitude": 42.3211, "Longitude": -85.1797},
    {"City": "Muncie", "State": "Indiana", "Latitude": 40.1934, "Longitude": -85.3863},
    {"City": "LaPorte", "State": "Indiana", "Latitude": 41.6106, "Longitude": -86.7225},
    {"City": "Sheboygan", "State": "Wisconsin", "Latitude": 43.7508, "Longitude": -87.7145},
    {"City": "Kokomo", "State": "Indiana", "Latitude": 40.4864, "Longitude": -86.1336},
    {"City": "Massillon", "State": "Ohio", "Latitude": 40.7967, "Longitude": -81.5215},
    {"City": "Bedford", "State": "Indiana", "Latitude": 38.8611, "Longitude": -86.4872}
]

new_warehouse_data = [
    {"warehouse_id": "FO-ROC-NEW", "warehouse_name": "Rochester", "city": "Rochester", "state": "Indiana", "latitude": 41.0667, "longitude": -86.1969, "max_delivery_radius": 90},
    {"warehouse_id": "FO-BALLV-NEW", "warehouse_name": "Ballville", "city": "Ballville", "state": "Ohio", "latitude": 41.3117, "longitude": -83.1364, "max_delivery_radius": 90} # Replaced Green Springs with Ballville
]
df_new_warehouses = pd.DataFrame(new_warehouse_data)

df_warehouses_all = pd.concat([pd.DataFrame(warehouse_data), df_new_warehouses], ignore_index=True)


df_worst_cities = pd.DataFrame(worst_cities_data)

gdf_warehouses_all = gpd.GeoDataFrame(
    df_warehouses_all,
    geometry=gpd.points_from_xy(df_warehouses_all.longitude, df_warehouses_all.latitude),
    crs="EPSG:4326"
)

gdf_worst_cities = gpd.GeoDataFrame(
    df_worst_cities,
    geometry=gpd.points_from_xy(df_worst_cities.Longitude, df_worst_cities.Latitude),
    crs="EPSG:4326"
)

gdf_warehouses_all_proj = gdf_warehouses_all.to_crs(epsg=3857)
gdf_worst_cities_proj = gdf_worst_cities.to_crs(epsg=3857)

gdf_warehouses_all_proj['delivery_area'] = gdf_warehouses_all_proj.geometry.buffer(gdf_warehouses_all_proj['max_delivery_radius'] * 1609.34)


existing_warehouse_ids = [wh['warehouse_id'] for wh in warehouse_data]
gdf_existing_warehouses_proj = gdf_warehouses_all_proj[gdf_warehouses_all_proj['warehouse_id'].isin(existing_warehouse_ids)]


gdf_rochester_proj = gdf_warehouses_all_proj[gdf_warehouses_all_proj['warehouse_id'] == 'FO-ROC-NEW']
gdf_ballville_proj = gdf_warehouses_all_proj[gdf_warehouses_all_proj['warehouse_id'] == 'FO-BALLV-NEW']


fig, ax = plt.subplots(figsize=(14, 14))

gdf_existing_warehouses_proj.set_geometry('delivery_area').plot(ax=ax, color='lightblue', edgecolor='blue', alpha=0.4, label='Existing Warehouse Service Area')

gdf_rochester_proj.set_geometry('delivery_area').plot(ax=ax, color='palegreen', edgecolor='darkgreen', alpha=0.5, label='Proposed Rochester Service Area (Radius: 90 miles)')

gdf_ballville_proj.set_geometry('delivery_area').plot(ax=ax, color='palegreen', edgecolor='darkgreen', alpha=0.5, label='Proposed Ballville Service Area (Radius: 90 miles)')

gdf_existing_warehouses_proj.plot(ax=ax, color='black', markersize=40, zorder=5, label='Existing Warehouse')

gdf_rochester_proj.plot(ax=ax, color='darkgreen', marker='H', markersize=80, zorder=6, label='Proposed Rochester Warehouse', edgecolor='forestgreen', linewidth=1)

gdf_ballville_proj.plot(ax=ax, color='darkgreen', marker='D', markersize=80, zorder=6, label='Proposed Ballville Warehouse', edgecolor='midnightblue', linewidth=1) # 'D' for diamond marker


gdf_worst_cities_proj.plot(ax=ax, color='red', marker='X', markersize=70, zorder=7, label='High-Cost Delivery Cities', edgecolor='darkred', linewidth=0.8)

for _, row in gdf_existing_warehouses_proj.iterrows():
    ax.annotate(
        row['warehouse_name'],
        xy=(row.geometry.x, row.geometry.y),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=8,
        color='black',
        fontweight='bold'
    )

for _, row in gdf_rochester_proj.iterrows():
    ax.annotate(
        row['warehouse_name'],
        xy=(row.geometry.x, row.geometry.y),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=9,
        color='darkgreen',
        fontweight='bold'
    )

for _, row in gdf_ballville_proj.iterrows():
    ax.annotate(
        row['warehouse_name'],
        xy=(row.geometry.x, row.geometry.y),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=9,
        color='darkblue',
        fontweight='bold'
    )

top_worst_cities_to_label = [
    "South Bend", "Niles", "Jackson", "Logansport", "Peru", "Richmond",
    "Youngstown", "Mansfield", "West Lafayette", "DeKalb", "Seymour", "Lafayette",
    "Toledo", "Flint", "Muncie", "Kokomo", "Kettering", "Lansing", "Ballville"
]

for _, row in gdf_worst_cities_proj.iterrows():
    if row['City'] in top_worst_cities_to_label:
        ax.annotate(
            f"{row['City']}, {row['State']}",
            xy=(row.geometry.x, row.geometry.y),
            xytext=(7, -10),
            textcoords="offset points",
            fontsize=7,
            color='red',
            fontweight='bold',
            ha='left'
        )

ctx.add_basemap(ax, crs=gdf_warehouses_all_proj.crs.to_string(), source=ctx.providers.CartoDB.Positron)

ax.legend(loc='lower left', fontsize=10)

transformer = Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)
min_x, min_y = transformer.transform(-98, 37)
max_x, max_y = transformer.transform(-78, 48)

ax.set_xlim(min_x, max_x)
ax.set_ylim(min_y, max_y)

ax.set_title("FleetOps Delivery Coverage with Proposed Rochester (IN) & Ballville (OH) Warehouses", fontsize=16)
ax.set_axis_off()

plt.savefig("fleetops_coverage_with_rochester_ballville_increased_radius.png", dpi=300, bbox_inches='tight')
plt.show()
