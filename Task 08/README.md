# Task 08: Sensor Data Analysis with NumPy

## 📋 Overview

Task 8 is a comprehensive sensor data analysis application that demonstrates advanced data manipulation using NumPy arrays. The application processes sensor readings including temperature, stress, and displacement data, providing statistical analysis and data transformation capabilities.

## 🎯 Features

### Core Functionality
- **Data Conversion**: Convert sensor data to structured NumPy arrays
- **Statistical Analysis**: Calculate averages per sensor for all metrics
- **Extreme Value Detection**: Identify sensors with highest stress values
- **Data Filtering**: Extract readings based on temperature thresholds
- **Interactive Console**: User-friendly command-line interface

### Data Processing Capabilities
- Temperature analysis and comparison
- Stress pattern identification
- Displacement tracking
- Time-series data handling
- Multi-sensor data aggregation

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Required Packages
```bash
pip install numpy
pip install pandas
pip install matplotlib
pip install PyQt6
```

### Alternative: Install from requirements.txt
```bash
pip install -r requirements.txt
```

## 📊 Sample Data Structure

The application works with sensor data in the following format:
```python
sensor_data = [
    ("S1", "2025-04-28 10:00", 35.2, 12.1, 0.002),  # (SensorID, Timestamp, Temperature, Stress, Displacement)
    ("S2", "2025-04-28 10:00", 36.5, 14.0, 0.003),
    ("S1", "2025-04-28 11:00", 36.1, 12.5, 0.0021),
    # ... more readings
]
```

## 🔧 Usage

### Running the Application

#### Option 1: Console Interface (Default)
```bash
python Task_08.py
```

#### Option 2: GUI Interface
```python
# Uncomment the following line in the main section:
# main_gui()
```

#### Option 3: Task 7 Console
```python
# Uncomment the following line in the main section:
# task_7_console()
```

### Console Menu Options

When running the console interface, you'll see the following options:

1. **Convert sensor data to NumPy array** - Transforms data into structured NumPy format
2. **Calculate averages per sensor** - Computes mean values for each sensor
3. **Identify highest stress sensor** - Finds sensor with maximum average stress
4. **Extract high temperature readings** - Filters readings above 36.0°C
5. **Exit** - Close the application

## 🏗️ Code Architecture

### Main Functions

#### 1. `convert_sensor_data_to_numpy_array(sensor_data)`
- **Purpose**: Converts raw sensor data to structured NumPy array
- **Input**: List of sensor data tuples
- **Output**: NumPy array with defined data types
- **Data Types**:
  - SensorID: Unicode string (U10)
  - Timestamp: Unicode string (U20)
  - Temperature: 32-bit float (f4)
  - Stress: 32-bit float (f4)
  - Displacement: 32-bit float (f4)

#### 2. `calculate_average_per_sensor(sensor_data)`
- **Purpose**: Calculates average temperature, stress, and displacement for each sensor
- **Input**: Sensor data (raw or NumPy array)
- **Output**: Dictionary with sensor averages
- **Returns**: `{sensor_id: {"avg_temp": float, "avg_stress": float, "avg_disp": float}}`

#### 3. `identify_sensor_with_highest_average_stress(sensor_data)`
- **Purpose**: Finds the sensor with the highest average stress value
- **Input**: Sensor data
- **Output**: Tuple of (sensor_id, highest_stress_value)
- **Use Case**: Critical stress monitoring and maintenance planning

#### 4. `extract_readings_where_temperature_more_than_36(sensor_data)`
- **Purpose**: Filters sensor readings above 36.0°C
- **Input**: Sensor data
- **Output**: NumPy array of filtered readings
- **Use Case**: High-temperature alerting and thermal analysis

### Data Flow

```
Raw Sensor Data → NumPy Array Conversion → Statistical Analysis → Results Display
     ↓                    ↓                      ↓              ↓
List of Tuples → Structured Array → Grouped Calculations → Formatted Output
```

## 📈 Data Analysis Examples

### Example 1: Average Temperature Calculation
```python
# Calculate averages for all sensors
averages = calculate_average_per_sensor(sensor_data)
for sensor, values in averages.items():
    print(f"{sensor}: Temp={values['avg_temp']:.2f}°C, "
          f"Stress={values['avg_stress']:.2f}, "
          f"Disp={values['avg_disp']:.4f}")
```

### Example 2: High Temperature Alerting
```python
# Find readings above 36°C
high_temp_readings = extract_readings_where_temperature_more_than_36(sensor_data)
print(f"Found {len(high_temp_readings)} readings above 36°C")
```

### Example 3: Stress Analysis
```python
# Identify critical stress sensor
critical_sensor, max_stress = identify_sensor_with_highest_average_stress(sensor_data)
print(f"Critical sensor: {critical_sensor} with stress: {max_stress}")
```

## 🔍 Code Quality Features

### Error Handling
- Input validation for user choices
- Graceful handling of empty datasets
- Type checking for data consistency

### Performance Optimization
- Efficient NumPy array operations
- Minimal memory allocation
- Vectorized calculations where possible

### Code Documentation
- Comprehensive function docstrings
- Clear variable naming conventions
- Logical code organization

## 🧪 Testing and Validation

### Test Cases
The code includes built-in validation:
- Data type consistency checks
- Range validation for temperature/stress values
- Sensor ID uniqueness verification

### Sample Output Validation
```python
# Expected output format for averages
{
    'S1': {'avg_temp': 36.1, 'avg_stress': 12.53, 'avg_disp': 0.0021},
    'S2': {'avg_temp': 36.85, 'avg_stress': 14.15, 'avg_disp': 0.00305},
    'S3': {'avg_temp': 34.0, 'avg_stress': 11.8, 'avg_disp': 0.0025}
}
```

## 🚨 Troubleshooting

### Common Issues

#### 1. Import Errors
```bash
# If you get PyQt6 import errors, install it separately:
pip install PyQt6
```

#### 2. NumPy Version Compatibility
```bash
# Ensure you have a compatible NumPy version:
pip install "numpy>=1.19.0"
```

#### 3. Data Format Issues
- Ensure sensor data follows the exact tuple format
- Check that numeric values are valid floats
- Verify timestamp format consistency

### Debug Mode
Add debug prints to understand data flow:
```python
# Add this to any function for debugging
print(f"Debug: Processing sensor {sensor_id} with data {reading}")
```

## 🔄 Extending the Code

### Adding New Analysis Functions
```python
def new_analysis_function(sensor_data):
    """
    Template for new analysis functions
    
    Args:
        sensor_data: Input sensor data
        
    Returns:
        Analysis results
    """
    # Convert to NumPy array
    data = convert_sensor_data_to_numpy_array(sensor_data)
    
    # Your analysis logic here
    
    return results
```

### Custom Data Sources
```python
# Load data from different sources
def load_from_csv(filename):
    import pandas as pd
    df = pd.read_csv(filename)
    return df.values.tolist()

def load_from_json(filename):
    import json
    with open(filename, 'r') as f:
        return json.load(f)
```

## 📚 Learning Resources

### NumPy Concepts Used
- **Structured Arrays**: Custom data types for sensor data
- **Array Indexing**: Boolean indexing for data filtering
- **Statistical Functions**: Mean calculations and aggregations
- **Data Type Management**: Efficient memory usage with specific types

### Related Topics
- Time series analysis
- Statistical data processing
- Sensor data management
- Industrial monitoring systems

## 🤝 Contributing

### Code Style Guidelines
- Follow PEP 8 Python style guide
- Use descriptive variable names
- Add docstrings for all functions
- Include error handling

### Testing New Features
1. Test with sample data
2. Validate output formats
3. Check error conditions
4. Update documentation

## 📄 License

This project is part of the Kaitech company training program. Please respect the company's intellectual property rights.

## 👨‍💻 Author Information

- **Name**: Tarek Adel Ali
- **Company**: Kaitech
- **Date**: 2025-07-21
- **Email**: tarekadel314@gmail.com
- **Task**: 08 - Sensor Data Analysis with NumPy

## 🔗 Related Projects

- **Task 7**: Pandas-based sensor data analysis
- **Task 6**: Basic sensor data organization
- **Task 5**: Excel data export functionality

## 📞 Support

For questions or issues:
1. Check the troubleshooting section above
2. Review the code comments and docstrings
3. Contact the author at tarekadel314@gmail.com

---

**Happy Coding! 🚀**

*This README provides comprehensive documentation for understanding, using, and extending the Task 8 sensor data analysis application.*
