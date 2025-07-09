# Geospatial Network Optimization: Identifying Strategic Warehouse Locations to Reduce Delivery Costs

## Background

FleetOps is a prominent Midwest delivery company, operating a network of 12 strategically located warehouses across Ohio, Indiana, Illinois, Wisconsin, Missouri, Minnesota, Iowa, and Michigan.

Recently, the Operations and Logistics department has identified an increasing strain on existing warehouse resources, resulting in suboptimal efficiency and inflated delivery costs in specific regions. This strain is particularly evident in areas requiring long-distance deliveries from current hubs, resulting in higher fuel consumption, increased driver hours, and extended delivery times.

To address these challenges and enhance overall network efficiency and utilization, this project leverages geospatial data analysis. The objective is to identify optimal potential new warehouse locations that can alleviate pressure on struggling areas, effectively reducing operational costs, improving service levels, and strengthening FleetOps' competitive advantage in key underserved markets.

---

## Data Model

### Data Dictionary

**Table:** Warehouses

This table contains information about existing distribution centers.

**Calculated column(s):** actual_daily_load = current_utilization * daily_capacity

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

**Table:** Drivers

This table stores detailed information about FleetOps' delivery drivers, including their assignment to specific warehouses and key performance metrics. This data is vital for understanding workforce capacity and individual contributions to delivery efficiency.

| Column Name  | Data Type | Description                       | Constraints |
|--------------|-----------|-----------------------------------|-------------|
| driver_id    | VARCHAR   | Unique identifier for each driver | Primary Key |
| first_name   | VARCHAR   | Driver's first name               |             |
| last_name    | VARCHAR   | Driver's last name                |             |
| hire_date    | DATE      | The date the driver was hired     |             |
| tenure_years | FLOAT     | The number of years the driver has been employed | |
| assigned_warehouse_id | VARCHAR | The ID of the warehouse to which the driver is currently assigned | Foreign Key referencing Warehouses.warehouse_id |
| vehicle_type | VARCHAR | The type and size of the vehicle used by the driver | |
| license_class | VARCHAR | Class of driver's license, regular or CDL | |
| route_efficiency_score | FLOAT | Performance score indicating driver efficiency on assigned routes | |
| on_time_delivery_rate | FLOAT | Percentage of deliveries completed on or before the scheduled time | |
| avg_mpg | FLOAT | The average miles per gallon for the driver's vehicle | |
| avg_daily_packages | INT | The average number of packages delivered per day | |
| employment_status | VARCHAR | A driver is either active or on leave | |

**Table:** Packages

This table represents the individual items or shipments handled by FleetOps, capturing key details about each package from creation to estimated delivery. This data is crucial for understanding demand patterns, logistics workload, and adherence to service levels.

| Column Name   | Data Type | Description                                    | Constraints |
|---------------|-----------|------------------------------------------------|-------------|
| package_id    | VARCHAR   | Unique identifier for each package or shipment | Primary Key |
| package_type  | VARCHAR   | Categorization of the package                  |             |
| weight_lbs    | FLOAT     | The weight of the package in lbs               |             |
| size_category | VARCHAR   | Classification of package based on its dimensions | |
| priority_level | VARCHAR  | The urgency or importance assigned to the package | | 
| origin_warehouse_id | VARCHAR | The ID of the warehouse from which the package originated | |
| created_date | DATE | The date the package entry was created in the system | |
| estimated_delivery_date | DATE| The date by which the package is expected to be delivered to the customer | |










