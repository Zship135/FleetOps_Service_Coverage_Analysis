# Geospatial Network Optimization: Identifying Strategic Warehouse Locations to Reduce Delivery Costs

## Background

FleetOps is a prominent Midwest delivery company, operating a network of 12 strategically located warehouses across Ohio, Indiana, Illinois, Wisconsin, Missouri, Minnesota, Iowa, and Michigan.

Recently, the Operations and Logistics department has identified an increasing strain on existing warehouse resources, resulting in suboptimal efficiency and inflated delivery costs in specific regions. This strain is particularly evident in areas requiring long-distance deliveries from current hubs, resulting in higher fuel consumption, increased driver hours, and extended delivery times.

To address these challenges and enhance overall network efficiency and utilization, this project leverages geospatial data analysis. The objective is to identify optimal potential new warehouse locations that can alleviate pressure on struggling areas, effectively reducing operational costs, improving service levels, and strengthening FleetOps' competitive advantage in key underserved markets.

---

## Data Model

### Data Dictionary

Table: Warehouses
This table contains information about existing distribution centers.

| Column Name          | Data Type | Description                                                                     | Constraints       |
|----------------------|-----------|---------------------------------------------------------------------------------|-------------------|
| warehouse_id         | VARCHAR   | Unique identifier for each warehouse                                            | Primary Key       |
| warehouse_name       | VARCHAR   | Full name of warehouse                                                          |                   |
| city                 | VARCHAR   | The city in which the warehouse is located                                      |                   |
| state                | VARCHAR   | The state in which the warehouse is located                                     |                   |
| latitude             | FLOAT     | Geographic latitude of the warehouse in decimal degrees                         | WGS84 (ESPG:4326) |
| longitude            | FLOAT     | Geographic longitude of the warehouse in decimal degrees                        | WGS84 (ESPG:4326) |
| zip_code             | VARCHAR   | The postal code of the warehouse's location                                     |                   |
| opened_date          | DATE      | The date when the warehouse began operations                                    |                   |
| capacity_sqft        | INT       | The total physical storage capacity of the warehouse in square feet             |                   |
| daily_capacity       | INT       | The amount of inventory the warehouse can take per day                          |                   |
| market_density       | FLOAT     | Density of potential customers within the primary service area of the warehouse |                   |
| avg_fuel_price       | FLOAT     | Average fuel price (price per gallon) for vehicles in this warehouse            |                   |
| traffic_factor       | FLOAT     | Multiplier for typical traffic congestion impact on delivery time and fuel      |                   |
| max_delivery_radius  | INT       | Maximum radius in miles within which deliveries from this warehouse are considered efficient | |
| avg_delivery_density | FLOAT     | The average number of deliveries per square mile within the effective service area | |
| avg_stop_time        | FLOAT     | The average time in minutes a delivery vehicle spends at a stop                 |                   |
| current_utilization  | FLOAT     | Current operational capacity utilization percentage                             |                   |
| opened_year          | INT       | The year the warehouse became operational                                       |                   |
| actual_daily_load    | FLOAT     | The actual volume or number of deliveries processed by the warehouse            |                   | 







