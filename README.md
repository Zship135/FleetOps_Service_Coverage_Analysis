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

**Table:** Service_Areas

This table defines the specific geographic regions or zones that each warehouse is responsible for serving. It includes demographic and locational data crucial for evaluating market potential, delivery complexity, and current coverage efficiency. This table is pivotal for understanding how effectively current warehouses serve their territories and where potential gaps may exist.

| Column Name | Data Type | Description | Constraints |
|-------------|-----------|-------------|-------------|
| service_area_id | VARCHAR | Unique identifier for each distinct service area segment | Primary Key |
| warehouse_id | VARCHAR | The ID of the warehouse primarily responsible for this service area | Foreign Key referencing Warehouses.warehouse_id |
| city | VARCHAR | The city name within the service area | |
| state | VARCHAR | The state abbreviation where the service areas are located | |
| zip_code | VARCHAR | The primary zip code that defines this service area segment | |
| latitude | FLOAT | Geographic latitude of the centroid or representative point of the service area | WSG84 (ESPG:4326) |
| longitude | FLOAT | Geographic longitude of the centroid or representative point of the service area | WSG84 (ESPG:4326) |
| population_density | FLOAT | The number of people per square mile within this service area | |
| distance_from_warehouse | FLOAT | The calculated distance in miles from the warehouse_id to the centroid of this service_area_id |

**Table:** Deliveries

This is the central transactional table, recording details for each completed package delivery. The metrics within this table are crucial for identifying inefficient delivery patterns, calculating costs, and pinpointing "high-cost delivery cities."

| Column Name | Data Type | Description | Constraints |
|-------------|-----------|-------------|-------------|
| delivery_id | VARCHAR   | Unique identifier for each individual delivery event | Primary Key |
| package_id  | VARCHAR   | The ID of the package being delivered | Foreign Key referencing Packages.package_id
| driver_id | VARCHAR | The ID of the driver who performed this delivery | Foreign Key referencing Drivers.driver_id |
| warehouse_id | VARCHAR | The ID of the warehouse from which this particular delivery was dispatched | Foreign Key referencing Warehouses.warehouse_id |
| delivery_city | VARCHAR | The city where the package was delivered | |
| delivery_state | VARCHAR | The state where the package was delivered | |
| delivery_zip | VARCHAR | The zip code of the delivery destination | |
| delivery_latitude | FLOAT | Geographic latitude of the delivery destination in decimal degrees | WGS84 (EPSG:4326) |
| delivery_longitude | FLOAT | Geographic longitude of the delivery destination in decimal degrees | WGS84 (EPSG:4326) |
| delivery_date | DATE | The actual date the delivery was completed | |
| delivery_time_hours | FLOAT | The total time in hours taken for this delivery, from dispatch to completion |
| distance_miles | FLOAT | The total distance in miles traveled for this delivery | |
| fuel_cost | FLOAT | The estimated fuel cost incurred for this delivery | |
| driver_cost | FLOAT | The estimated labor cost attributed to this delivery | |
| total_cost | FLOAT | The aggregate cost incurred for this delivery | |
| distance_from_warehouse | FLOAT | The direct-line or route distance in miles from the dispatching warehouse_id to the delivery_destination | |
| efficiency_penalty_factor | FLOAT | A calculated factor representing increased inefficiency due to long distances, traffic, or low delivery density | |

---

### ER Diagram

![image](https://github.com/user-attachments/assets/03bfd7f1-9e85-4aea-84a9-873280407b6a)

---

### Relational Schema

![image](https://github.com/user-attachments/assets/bd270acd-557b-4edb-8d34-202c3258b212)

---

## Executive Summary



---

## Insights Deep Dive

***Warehouse Utilization and Efficiency:***
- It takes ~3 years for a warehouse to reach 50% utilization, and ~6 years for 80%-90%
- As the traffic factor increases, the average stop time for delivery decreases
- As market density increases, the average stop time for delivery decreases

The trends found in the average stop time are not what is expected. As the driver encounters more traffic and has more to deliver, the average stop time decreases. While somewhat counterintuitive, there is a potential explanation. Given tighter delivery constraints, a driver might put more effort into making the deliveries faster. Another factor could be urban vs rural deliveries. Urban deliveries may involve office buildings or apartments, which are less personal and take less time than a delivery to a single home. 

<img width="752" height="564" alt="image" src="https://github.com/user-attachments/assets/276e2868-cb7f-4dac-8402-c3f4d9cfb6aa" />

<img width="802" height="452" alt="image" src="https://github.com/user-attachments/assets/257454ff-f8f7-48f7-9e88-19b49be70b5e" />





---

## Recommendations


















