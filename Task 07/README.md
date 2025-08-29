# Task 07: Sensor Data Analysis with Pandas & PyQt6

## 📋 Overview

Task 07 is a comprehensive sensor data analysis application that demonstrates advanced data manipulation using Pandas DataFrames and provides both console and graphical user interfaces. The application processes sensor readings including temperature, stress, and displacement data, offering statistical analysis, data visualization, and export capabilities.

## 🎯 Features

### Core Functionality
- **Data Conversion**: Convert sensor data to Pandas DataFrames with proper timestamp handling
- **Statistical Analysis**: Calculate averages per sensor for all metrics (temperature, stress, displacement)
- **Data Visualization**: Create line charts and scatter plots using Matplotlib
- **Data Organization**: Group and organize sensor readings by sensor ID
- **Extreme Value Detection**: Identify sensors with maximum and minimum temperature values
- **Time Series Analysis**: Compare readings across different time intervals
- **Data Export**: Save results to Excel files and JSON format

### User Interface Options
- **Console Interface**: Command-line interface for quick data analysis
- **GUI Interface**: Professional PyQt6-based graphical interface with user authentication
- **Interactive Dashboard**: User-friendly buttons for all analysis functions

### Data Processing Capabilities
- Temperature trend analysis and comparison
- Stress pattern identification and threshold detection
- Displacement tracking and statistical analysis
- Multi-sensor data aggregation and grouping
- Time-series data handling and comparison

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Required Packages
```bash
pip install pandas
pip install matplotlib
pip install PyQt6
pip install openpyxl
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
    ("S3", "2025-04-28 10:00", 34.0, 11.8, 0.0025),
    ("S2", "2025-04-28 11:00", 37.2, 14.3, 0.0031),
    ("S1", "2025-04-28 12:00", 37.0, 13.0, 0.0022),
]
```

## 🔧 Usage

### Running the Application

#### Option 1: Console Interface (Default)
```bash
python Task_07.py
```

#### Option 2: GUI Interface
```python
# Uncomment the following line in the main section:
# main_gui()
```

#### Option 3: Extended Console Interface
```python
# Uncomment the following line in the main section:
# main_console()
```

### Console Menu Options

When running the console interface, you'll see the following options:

1. **Convert sensor data to dataframe** - Transforms data into Pandas DataFrame format
2. **Compute and display averages per sensor** - Shows mean values for each sensor
3. **Identify highest temperature sensor** - Finds sensor with maximum average temperature
4. **Plot temperature vs time chart** - Creates line chart with markers
5. **Create stress vs displacement scatter plot** - Shows relationship between metrics
6. **Exit** - Close the application

### Extended Console Features (11 options)
- Organize readings per sensor
- Identify extreme sensors
- Compare time interval readings
- Summarize data with statistics
- Group data by sensor
- Find high stress sensors (>13.0)
- Calculate comprehensive statistics
- Max/min temperature and displacement analysis
- Extract and sort timestamps
- Most recent readings per sensor

## 🏗️ Code Architecture

### Main Functions

#### 1. `convert_sensor_data_to_dataframe(sensor_data)`
- **Purpose**: Converts raw sensor data to Pandas DataFrame
- **Input**: List of sensor data tuples
- **Output**: Pandas DataFrame with proper column names and timestamp conversion
- **Features**: Automatic timestamp parsing and data type optimization

#### 2. `plot_temperature_vs_time(sensor_data)`
- **Purpose**: Creates line charts showing temperature trends over time
- **Input**: Sensor data
- **Output**: Interactive Matplotlib plot
- **Features**: Different colors per sensor, markers for data points, grid lines

#### 3. `plot_stress_vs_displacement(sensor_data)`
- **Purpose**: Creates scatter plots showing relationship between stress and displacement
- **Input**: Sensor data
- **Output**: Interactive Matplotlib scatter plot
- **Features**: Color-coded by sensor, legend, grid lines

#### 4. `organize_readings(sensor_data)`
- **Purpose**: Groups sensor readings by sensor ID
- **Input**: Raw sensor data
- **Output**: Dictionary with sensor ID as key and readings as values
- **Use Case**: Data organization for further analysis

#### 5. `Extreme_sensors(data)`
- **Purpose**: Identifies sensors with maximum and minimum temperature values
- **Input**: Organized sensor data
- **Output**: List of extreme sensor findings
- **Use Case**: Critical temperature monitoring

#### 6. `Compare_readings(data)`
- **Purpose**: Compares temperature readings across time intervals
- **Input**: Organized sensor data
- **Output**: List of temperature change observations
- **Features**: Detects increases, decreases, and constant temperatures

#### 7. `Summarize_data(data, choice)`
- **Purpose**: Calculates comprehensive statistics per sensor
- **Input**: Organized sensor data and user choice
- **Output**: Statistical summary (max, min, average)
- **Choices**: Temperature, Stress, Displacement, or All

### Data Flow

```
Raw Sensor Data → Pandas DataFrame → Statistical Analysis → Visualization → Export
      ↓                    ↓                    ↓              ↓           ↓
List of Tuples → Structured DataFrame → Grouped Calculations → Charts → Excel/JSON
```

## 📈 Data Analysis Examples

### Example 1: Basic DataFrame Conversion
```python
# Convert sensor data to DataFrame
df = convert_sensor_data_to_dataframe(sensor_data)
print(f"DataFrame shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Data types: {df.dtypes}")
```

### Example 2: Statistical Analysis
```python
# Calculate averages per sensor
temp_avg = df.groupby("SensorID")["Temperature"].mean()
stress_avg = df.groupby("SensorID")["Stress"].mean()
displacement_avg = df.groupby("SensorID")["Displacement"].mean()

print("Temperature averages per sensor:")
print(temp_avg)
```

### Example 3: Data Visualization
```python
# Create temperature trend plot
plot_temperature_vs_time(sensor_data)

# Create stress-displacement relationship plot
plot_stress_vs_displacement(sensor_data)
```

### Example 4: Advanced Data Processing
```python
# Organize and analyze data
organized_data = organize_readings(sensor_data)
extreme_findings = Extreme_sensors(organized_data)
comparison_results = Compare_readings(organized_data)

# Print results
for finding in extreme_findings:
    print(finding)
```

## 🖥️ GUI Interface Features

### User Authentication System
- **Login/Signup**: Secure user account management
- **Profile Management**: Update user information and passwords
- **Session Management**: Secure login/logout functionality

### Dashboard Interface
- **Function Buttons**: Easy access to all analysis functions
- **Results Display**: Text area showing analysis results
- **Save Options**: Export results to Excel or JSON format
- **User Settings**: Profile management and customization

### Professional Design
- **Modern UI**: Clean, professional appearance
- **Responsive Layout**: Adapts to different screen sizes
- **Color Scheme**: Professional green theme with good contrast
- **Interactive Elements**: Hover effects and visual feedback

## 💾 Data Export Capabilities

### Excel Export Functions
- **Multiple Sheets**: Each analysis gets its own worksheet
- **Append Mode**: Can add to existing Excel files
- **Sheet Management**: Automatic sheet naming and organization
- **Data Formatting**: Proper data structure preservation

### JSON Export Functions
- **Structured Data**: Maintains data hierarchy
- **File Naming**: Descriptive filenames for each analysis
- **Data Integrity**: Preserves all analysis results

### Export Options
```python
# Save to Excel
Organize_readings_per_sensor_save_to_excel(data)

# Save to JSON
write_to_json(data, "analysis_results.json")

# Save to both formats
# (Available through GUI save dialog)
```

## 🔍 Code Quality Features

### Error Handling
- Input validation for user choices
- Graceful handling of empty datasets
- File operation error handling
- User input validation

### Performance Optimization
- Efficient Pandas operations
- Minimal memory allocation
- Vectorized calculations
- Optimized data structures

### Code Documentation
- Comprehensive function documentation
- Clear variable naming conventions
- Logical code organization
- Inline comments for complex operations

## 🧪 Testing and Validation

### Built-in Validation
- Data type consistency checks
- Range validation for numeric values
- Sensor ID uniqueness verification
- Timestamp format validation

### Sample Output Examples
```python
# Expected DataFrame output
   SensorID           Timestamp  Temperature  Stress  Displacement
0       S1 2025-04-28 10:00:00         35.2    12.1        0.002
1       S2 2025-04-28 10:00:00         36.5    14.0        0.003
2       S1 2025-04-28 11:00:00         36.1    12.5        0.0021

# Expected statistical output
S1    36.13
S2    36.85
S3    34.00
Name: Temperature, dtype: float64
```

## 🚨 Troubleshooting

### Common Issues

#### 1. Import Errors
```bash
# If you get PyQt6 import errors:
pip install PyQt6

# If you get openpyxl errors:
pip install openpyxl
```

#### 2. Matplotlib Display Issues
```python
# For headless environments, use:
import matplotlib
matplotlib.use('Agg')
```

#### 3. Data Format Issues
- Ensure sensor data follows the exact tuple format
- Check that numeric values are valid floats
- Verify timestamp format consistency (YYYY-MM-DD HH:MM)

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
    # Convert to DataFrame
    df = convert_sensor_data_to_dataframe(sensor_data)
    
    # Your analysis logic here
    
    return results
```

### Custom Data Sources
```python
# Load data from different sources
def load_from_csv(filename):
    df = pd.read_csv(filename)
    return df.values.tolist()

def load_from_database(connection_string):
    # Database loading logic
    pass
```

### Adding New Visualization Types
```python
def plot_new_chart(sensor_data, chart_type):
    df = convert_sensor_data_to_dataframe(sensor_data)
    
    if chart_type == "histogram":
        # Histogram logic
        pass
    elif chart_type == "boxplot":
        # Boxplot logic
        pass
```

## 📚 Learning Resources

### Pandas Concepts Used
- **DataFrame Operations**: Data manipulation and transformation
- **GroupBy Operations**: Aggregating data by categories
- **Data Type Management**: Efficient data storage and processing
- **Time Series Handling**: Timestamp parsing and manipulation

### Matplotlib Concepts Used
- **Line Charts**: Time series visualization
- **Scatter Plots**: Relationship analysis
- **Figure Management**: Plot sizing and layout
- **Styling**: Colors, markers, and grid lines

### Related Topics
- Time series analysis
- Statistical data processing
- Data visualization techniques
- Industrial monitoring systems
- User interface design

## 🤝 Contributing

### Code Style Guidelines
- Follow PEP 8 Python style guide
- Use descriptive variable names
- Add docstrings for all functions
- Include error handling
- Maintain consistent formatting

### Testing New Features
1. Test with sample data
2. Validate output formats
3. Check error conditions
4. Update documentation
5. Test both console and GUI interfaces

## 📄 License

This project is part of the Kaitech company training program. Please respect the company's intellectual property rights.

## 👨‍💻 Author Information

- **Name**: Tarek Adel Ali
- **Company**: Kaitech
- **Date**: 2025-07-12
- **Email**: tarekadel314@gmail.com
- **Task**: 07 - Sensor Data Analysis with Pandas & PyQt6

## 🔗 Related Projects

- **Task 8**: NumPy-based sensor data analysis
- **Task 6**: Basic sensor data organization
- **Task 5**: Excel data export functionality

## 📞 Support

For questions or issues:
1. Check the troubleshooting section above
2. Review the code comments and docstrings
3. Test with the provided sample data
4. Contact the author at tarekadel314@gmail.com

---

**Happy Coding! 🚀**

*This README provides comprehensive documentation for understanding, using, and extending the Task 07 sensor data analysis application with Pandas and PyQt6.*
