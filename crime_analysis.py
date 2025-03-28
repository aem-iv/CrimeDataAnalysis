#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crime Data Analysis and Visualization

This script loads crime data, performs exploratory data analysis (EDA),
visualizes crime patterns over time, and applies clustering techniques
for geospatial analysis.

Author: A. Martinez
Created on: March 18, 2025
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import folium
from folium.plugins import HeatMap, MarkerCluster


# Load crime data
file_path = "crimedata.csv"
df = pd.read_csv(file_path)

# Display basic dataset information
print(df.head(10))
print(df.tail(10))

# Convert datetime column
df['REPDATETIME'] = pd.to_datetime(df['REPDATETIME'], errors='coerce')

# --- Frequency Analysis --- #
# Identify the top 10 most common charges
charge_counts = df['CHARGE_LITERAL'].value_counts().head(10)
print("Most Common Charges:\n", charge_counts)

# Plot most common charges
charge_counts.plot(kind='bar', title='Top 10 Most Common Charges')
plt.xlabel("Charge")
plt.ylabel("Frequency")
plt.show()

# --- Temporal Analysis --- #
# Crimes per month
df.set_index('REPDATETIME').resample('M').size().plot(title='Crimes per Month')
plt.xlabel("Month")
plt.ylabel("Number of Crimes")
plt.show()

# Extract time-based features
df['Hour'] = df['REPDATETIME'].dt.hour
df['DayOfWeek'] = df['REPDATETIME'].dt.dayofweek
df['Month'] = df['REPDATETIME'].dt.month

# --- Crime Patterns by Time --- #
# Crime frequency by hour
crime_by_hour = df.groupby('Hour').size().reset_index(name='crime_count')
crime_by_hour.plot(x='Hour', y='crime_count', kind='bar',
                   title='Crime Frequency by Hour')
plt.show()

# Crime frequency by day of the week
day_mapping = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
               4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
crime_by_day = df.groupby('DayOfWeek').size().reset_index(name='crime_count')
crime_by_day['DayOfWeek'] = crime_by_day['DayOfWeek'].map(day_mapping)
crime_by_day.plot(x='DayOfWeek', y='crime_count',
                  kind='bar', title='Crime Frequency by Day')
plt.show()

# --- Crime Heatmap --- #
crime_by_day_hour = df.groupby(
    ['DayOfWeek', 'Hour']).size().unstack().fillna(0)
crime_by_day_hour.index = [day_mapping[i]
                           for i in range(7)]  # Map numeric days to names

plt.figure(figsize=(12, 6))
sns.heatmap(crime_by_day_hour, cmap="cividis", annot=True, fmt="d", cbar=False)
plt.title('Crime Heatmap by Day and Hour')
plt.xlabel('Hour')
plt.ylabel('Day')
plt.show()

# --- Time Period Analysis --- #


def categorize_time(hour):
    if 4 <= hour < 10:
        return 'Morning (4-10am)'
    elif 10 <= hour < 16:
        return 'Midday (10-4pm)'
    elif 16 <= hour < 21:
        return 'Evening (4-9pm)'
    else:
        return 'Late Night (9pm-4am)'


df['TimePeriod'] = df['Hour'].apply(categorize_time)
crime_by_month_time = df.groupby(
    ['Month', 'TimePeriod']).size().unstack().fillna(0)

line_styles = {
    'Morning (4-10am)': ('--', 'D'),   # Dashed line with diamond markers
    'Midday (10-4pm)': ('-', 'o'),     # Solid line with circle markers
    'Evening (4-9pm)': ('-.', 's'),    # Dash-dot line with square markers
    'Late Night (9pm-4am)': (':', '^')  # Dotted line with triangle markers
}

fig, ax = plt.subplots(figsize=(10, 6))

# Iterate over each time period and apply line styles for b/w printing
for time_period, (line_style, marker) in line_styles.items():
    if time_period in crime_by_month_time.columns:
        crime_by_month_time[time_period].plot(
            ax=ax, linestyle=line_style, marker=marker, markersize=6, label=time_period
        )

# Plotting
ax.set_title('Monthly Crime Trends by Time Period')
ax.set_xlabel('Month')
ax.set_ylabel('Crime Count')
ax.legend(title='Time Period')

plt.show()

# --- Geospatial Analysis --- #
# set zoom for map generation
zoom = 15
# Heatmap
h = folium.Map(location=[df['LATITUDE'].mode(),
               df['LONGITUDE'].mode()], zoom_start=zoom)
HeatMap(df[['LATITUDE', 'LONGITUDE']].dropna().values.tolist()).add_to(h)
h.save('crime_heatmap.html')


# Crime cluster map
m = folium.Map(location=[df['LATITUDE'].mode(),
               df['LONGITUDE'].mode()], zoom_start=zoom)
marker_cluster = MarkerCluster().add_to(m)
for _, row in df.iterrows():
    folium.Marker(
        location=[row['LATITUDE'], row['LONGITUDE']],
        popup=f"Charge: {row['CHARGE_LITERAL']}"
    ).add_to(marker_cluster)
m.save('crime_cluster_map.html')
