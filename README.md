# Crime Data Analysis and Visualization

## Project Description

This project analyzes and visualizes crime data, exploring patterns over time and using clustering techniques for geospatial analysis. The dataset includes information on crime incidents such as the charges, locations, and times of occurrence.

### Key Features:
- Frequency analysis of common crime charges
- Temporal analysis of crime trends by hour, day of the week, and month
- Geospatial analysis using heatmaps and clustering
- Custom classification of crime data into different time periods

## Data

This project uses a dataset containing crime data, with the following fields utilized for analysis:
- `REPDATETIME`: Date and time of the reported crime
- `CHARGE_LITERAL`: Qualitative description of the charge associated with the crime
- `LATITUDE`: Latitude coordinate of the crime location
- `LONGITUDE`: Longitude coordinate of the crime location

(Note: The dataset includes additional fields that were not used in this analysis.)

The dataset is in CSV format and should be placed in the same directory as the script (or the file path in the script can be updated).

## Requirements

To run this project, you will need to install the following Python libraries:

- pandas
- matplotlib
- seaborn
- folium

You can install them using `pip`:

```bash
pip install pandas matplotlib seaborn folium
```
## Usage

To clone this repository and get started, run the following commands:

1. Clone the repository:
   ```bash
   git clone https://github.com/aem-iv/CrimeDataAnalysis.git
   ```
2. Navigate into the project directory:
   ```bash
   cd CrimeDataAnalysis
   ```
## Visualizations

- Crime Frequency by Hour: A bar plot showing how crime frequency varies by hour.

- Crime Frequency by Day: A bar plot showing how crime frequency varies by day of the week.

- Crime Frequency Heatmap: A frequency table by day of the week and hour, providing a heatmap to identify patterns in crime occurrence across different times.

- Crime Heatmap: A geospacial heatmap that shows the density of crimes across different areas.

- Crime Cluster Map: An interactive map showing clustered crime data with popups for crime charges.

## Conclusion
This project analyzes crime trends over time and geographical patterns, providing valuable information for law enforcement, urban planning, community engagement, and public safety efforts.