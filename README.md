# Sensor Data Analysis System

## 📋 Overview

A comprehensive sensor data analysis application that provides both GUI and console interfaces for analyzing sensor readings including temperature, stress, and displacement data. The system offers advanced data processing capabilities with export functionality to Excel and JSON formats.

## 👨‍💻 Author Information

- **Name:** Tarek Adel Ali
- **Task:** 06
- **Company:** Kaitech
- **Date:** 2025-06-29
- **Email:** tarekadel314@gmail.com

## 🚀 Features

### Core Data Analysis Functions
- **Data Organization:** Organize sensor readings by sensor ID
- **Extreme Value Detection:** Identify sensors with maximum and minimum temperature values
- **Time-based Comparison:** Compare readings across different time intervals
- **Statistical Analysis:** Calculate max, min, and average values for temperature, stress, and displacement
- **Data Grouping:** Group data by sensor using dictionaries
- **High Stress Detection:** Find sensors with stress values > 13.0
- **Timestamp Extraction:** Extract and sort timestamps with duplicate removal options
- **Recent Readings:** Get the most recent reading for each sensor

### User Interface
- **Modern GUI:** Professional PyQt6-based graphical interface
- **User Authentication:** Secure login and signup system with profile management
- **Interactive Dashboard:** User-friendly dashboard with organized function buttons
- **Data Export:** Save results to Excel (.xlsx) and JSON formats
- **Settings Management:** User profile settings and preferences

### Data Export Capabilities
- **Excel Export:** Multi-sheet Excel files with organized data
- **JSON Export:** Structured JSON files for data interchange
- **Flexible Export Options:** Choose Excel, JSON, or both formats

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Required Dependencies
```bash
pip install PyQt6 pandas openpyxl
```

### Installation Steps
1. Clone the repository:
```bash
git clone <repository-url>
cd sensor-data-analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python Tarek_Adel_Task_06.py
```

## 🎯 Usage

### GUI Mode (Default)
The application starts in GUI mode by default, providing a modern interface with the following features:

#### 1. User Authentication
- **Login:** Use existing credentials to access the system
- **Signup:** Create a new account with email and password
- **Profile Management:** Update user information and settings

#### 2. Dashboard Functions
The dashboard provides access to all data analysis functions:

| Function | Description |
|----------|-------------|
| **Organize Readings per Sensor** | Groups sensor data by sensor ID |
| **Identify Extreme Sensors** | Finds sensors with max/min temperature values |
| **Compare Readings** | Analyzes temperature changes over time |
| **Summarize Data** | Calculates statistics (max, min, average) |
| **Group Data by Sensor** | Organizes data using dictionaries |
| **Find High Stress Sensors** | Identifies sensors with stress > 13.0 |
| **Calculate Statistics** | Per-sensor statistical analysis |
| **Max/Min Values** | Overall system statistics |
| **Extract Timestamps** | Extracts and sorts timestamps |
| **Most Recent Readings** | Gets latest readings for each sensor |

#### 3. Data Export
After each analysis, you can export results to:
- **Excel (.xlsx):** Multi-sheet format with organized data
- **JSON:** Structured data format
- **Both:** Export to both formats simultaneously

### Console Mode
To use the console interface, modify the main function:

```python
if __name__ == "__main__":
    # main_gui()  # Comment out GUI mode
    main_console()  # Uncomment for console mode
```

#### Console Menu Options
```
1. Organize readings per sensor
2. Identify unique sensors with extreme values
3. Compare readings from different time intervals
4. Summarize the data by calculating max, min, and average readings per sensor
5. Group data by sensor using a dictionary
6. Use sets to find unique sensor IDs that recorded stress > 13.0
7. Calculate statistics per sensor
8. Max, min, and average temperature and max displacement
9. Extract all timestamps into a list and sort them
10. Create a tuple of the most recent reading for each sensor
11. Exit
```

## 📊 Sample Data Structure

The application works with sensor data in the following format:
```python
sensor_data = [
    ("S1", "2025-04-28 10:00", 35.2, 12.1, 0.002),  # (sensor_id, timestamp, temperature, stress, displacement)
    ("S2", "2025-04-28 10:00", 36.5, 14.0, 0.003),
    # ... more data
]
```

## 🔧 Technical Details

### Core Functions
- **`organize_readings()`:** Groups sensor data by sensor ID
- **`Extreme_sensors()`:** Identifies extreme temperature values
- **`Compare_readings()`:** Analyzes temperature changes over time
- **`Summarize_data()`:** Calculates statistical measures
- **`Group_data_by_sensor()`:** Organizes data using dictionaries
- **`unique_sensor_set()`:** Finds high-stress sensors using sets
- **`max_and_min_values()`:** Calculates overall system statistics
- **`timestapms_extracted()`:** Extracts and processes timestamps
- **`most_recent_reading()`:** Gets latest readings per sensor

### Export Functions
- **Excel Export:** Functions ending with `_save_to_excel()`
- **JSON Export:** `write_to_json()` function
- **File Management:** Automatic file creation and sheet management

### GUI Components
- **LoginApp Class:** Main application window
- **User Management:** Secure authentication system
- **Dashboard:** Interactive function selection
- **Results Display:** Real-time results viewing
- **Settings Dialog:** Profile management interface

## 📁 File Structure

```
sensor-data-analysis/
├── Tarek_Adel_Task_06.py          # Main application file
├── users.txt                      # User credentials storage
├── sensor_readings.xlsx           # Generated Excel file
├── *.json                         # Generated JSON files
├── logo_5e37c4cd90a4c.png        # Application logo
└── README.md                      # This file
```

## 🛠️ Customization

### Adding New Sensor Data
Modify the `sensor_data` list in the main file:
```python
sensor_data = [
    ("S1", "2025-04-28 10:00", 35.2, 12.1, 0.002),
    # Add your sensor data here
]
```

### Modifying Analysis Functions
All core functions are modular and can be easily modified or extended to add new analysis capabilities.

## 🔒 Security Features

- **Password Protection:** Secure user authentication
- **File-based Storage:** User credentials stored locally
- **Session Management:** Secure login/logout functionality
- **Profile Security:** Password verification for profile changes

## 📈 Data Analysis Capabilities

### Statistical Analysis
- Maximum, minimum, and average calculations
- Per-sensor and system-wide statistics
- Temperature, stress, and displacement analysis

### Time-based Analysis
- Temporal data comparison
- Timestamp extraction and sorting
- Recent reading identification

### Data Organization
- Sensor-based grouping
- Dictionary-based data structures
- Set operations for unique value identification

## 🚨 Troubleshooting

### Common Issues

1. **Import Errors:**
   ```bash
   pip install PyQt6 pandas openpyxl
   ```

2. **GUI Not Starting:**
   - Ensure PyQt6 is properly installed
   - Check Python version compatibility

3. **File Permission Errors:**
   - Ensure write permissions in the application directory
   - Close any open Excel files before running

4. **Data Export Issues:**
   - Verify sufficient disk space
   - Check file permissions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is developed for Kaitech company use.

## 📞 Support

For technical support or questions, please contact:
- **Developer:** Tarek Adel Ali
- **Company:** Kaitech

---

**Note:** This application is designed for sensor data analysis and provides both GUI and console interfaces for maximum flexibility. The system supports various data formats and export options to meet different analysis requirements. 