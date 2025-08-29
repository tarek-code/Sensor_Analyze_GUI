# Sensor Data Analysis Tool

## Overview

This Sensor Data Analysis Tool is a comprehensive Python application designed for processing, analyzing, and visualizing sensor data from multiple sensors. The tool provides various functions to organize, compare, and summarize sensor readings, with capabilities to identify extreme values, track temperature changes over time, and export results to Excel for further analysis.

Developed by Tarek Adel Ali at Kaitech, this tool demonstrates advanced data manipulation techniques using Python's data structures and pandas for Excel integration. The application is particularly useful for monitoring environmental conditions or industrial processes where temperature, stress, and displacement measurements are critical.

## Features

The Sensor Data Analysis Tool offers a rich set of features for comprehensive sensor data management:

- **Data Organization**: Efficiently organizes raw sensor readings by sensor ID for easier analysis
- **Extreme Value Detection**: Identifies sensors recording maximum and minimum temperature values
- **Temporal Analysis**: Compares readings across different time intervals to track changes
- **Statistical Analysis**: Calculates key statistics (max, min, average) for temperature, stress, and displacement
- **Data Grouping**: Groups readings by sensor ID using various Python data structures
- **Unique Sensor Identification**: Uses set operations to find sensors with specific characteristics
- **Timestamp Management**: Extracts, sorts, and filters timestamps with or without duplicates
- **Recent Reading Extraction**: Creates tuples of the most recent readings for each sensor
- **Excel Export**: Saves all analysis results to a multi-sheet Excel workbook for reporting and sharing

## Installation

### Prerequisites

To run this application, you need:

- Python 3.6 or higher
- pandas library
- openpyxl library

### Setup

1. Clone this repository to your local machine
2. Install the required dependencies:

```bash
pip install pandas openpyxl
```

3. Run the script using Python:

```bash
python sensor_analysis.py
```

## Usage

The application comes with sample sensor data pre-loaded, but you can modify the `sensor_data` list to include your own measurements. Each sensor reading should follow this format:

```python
(sensor_id, timestamp, temperature, stress, displacement)
```

For example:
```python
("S1", "2025-04-28 10:00", 35.2, 12.1, 0.002)
```

### Basic Workflow

1. **Organize Data**: First, organize the raw sensor data by sensor ID
   ```python
   organized_data = organize_readings(sensor_data)
   ```

2. **Analyze Data**: Use various functions to analyze the organized data
   ```python
   extreme_values = Extreme_sensors(organized_data)
   reading_comparisons = Compare_readings(organized_data)
   ```

3. **Export Results**: Save analysis results to Excel for reporting
   ```python
   Extreme_sensors_save_to_excel(extreme_values)
   Compare_readings_save_to_excel(reading_comparisons)
   ```

## Detailed Function Documentation

### Data Organization Functions

#### `organize_readings(sensor_data)`
Transforms raw sensor data into a dictionary organized by sensor ID. Each sensor's readings are stored as a list of dictionaries containing timestamp, temperature, stress, and displacement values.

#### `show_data_before_and_after(original_data, organized_data)`
Displays the data structure before and after organization for comparison and verification.

### Analysis Functions

#### `Extreme_sensors(data)`
Identifies sensors recording the maximum and minimum temperature values across all readings. Returns a list of strings describing these extreme values.

#### `Compare_readings(data)`
Analyzes temperature changes between consecutive readings for each sensor. Detects increases, decreases, or constant temperatures and returns detailed descriptions of these changes.

#### `Summarize_data(data)`
Calculates comprehensive statistics (maximum, minimum, average) for temperature, stress, and displacement readings per sensor. Allows user to select which measurements to display.

#### `Group_data_by_sensor(original_data)`
Groups raw sensor data by sensor ID using a dictionary with sensor IDs as keys and lists of reading tuples as values. Provides a different organization approach than `organize_readings`.

#### `unique_sensor_set(original_data)`
Uses Python sets to identify sensors that recorded stress values greater than 13.0, demonstrating efficient use of set operations for filtering.

#### `max_and_min_values(data)`
Calculates global maximum, minimum, and average temperature values across all sensors, as well as the maximum displacement value.

#### `timestapms_extracted(data)`
Extracts all timestamps from the readings, with options to include or exclude duplicates, and returns them in sorted order.

#### `most_recent_reading(data)`
Creates a tuple containing the most recent reading for each sensor, useful for getting the current state of all sensors.

### Excel Export Functions

#### `Organize_readings_per_sensor_save_to_excel(data)`
Exports the organized sensor readings to an Excel file, creating or appending to a sheet named "reading_sensorsensors".

#### `Extreme_sensors_save_to_excel(data)`
Saves information about sensors with extreme temperature values to the Excel file.

#### `Compare_readings_save_to_excel(data)`
Exports temperature change analysis between consecutive readings to the Excel file.

#### `Summarize_data_save_to_excel(data)`
Saves statistical summaries of sensor readings to the Excel file.

#### `Group_data_by_sensor_save_to_excel(data)`
Exports grouped sensor data to the Excel file.

## Data Structure

The application uses several Python data structures to efficiently manage sensor data:

- **Lists**: Store raw sensor readings and intermediate results
- **Tuples**: Represent individual sensor readings with fixed structure
- **Dictionaries**: Organize readings by sensor ID for efficient lookup and analysis
- **Sets**: Find unique sensors matching specific criteria
- **Pandas DataFrames**: Format data for Excel export

## Example Output

When running the analysis functions, you'll see output similar to:

```
Sensor with max temperature: S2 with extreme value in temperature: 37.2℃
Sensor with min temperature: S3 with extreme value in temperature: 34.0℃

Sensor S1 has a temperature increased of 0.90 between 2025-04-28 10:00 and 2025-04-28 11:00
Sensor S1 has a temperature increased of 0.90 between 2025-04-28 11:00 and 2025-04-28 12:00
Sensor S2 has a temperature increased of 0.70 between 2025-04-28 10:00 and 2025-04-28 11:00

The maximum temperature is 37.2℃ and the minimum temperature is 34.0℃ and the average temperature is 36.00℃
The maximum value in displacement: 0.0031m
```

## Excel Output

The application generates an Excel file named `sensor_readings.xlsx` with multiple sheets:

- **reading_sensorsensors**: Contains all organized sensor readings
- **Extreme_sensors**: Lists sensors with maximum and minimum temperature values
- **Compare_readings**: Shows temperature changes between consecutive readings
- **Summarize_data**: Contains statistical summaries for each sensor
- **Group_data_by_sensor**: Shows data grouped by sensor ID

## Author

**Tarek Adel Ali**  
Kaitech

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Thanks to Kaitech for supporting this project
- Special thanks to all contributors and testers
