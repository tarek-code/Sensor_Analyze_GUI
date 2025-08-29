# Breaife about the author:
# Name: Tarek Adel Ali
# Task: 08
# Compant: Kaitech
# Date: 2025-07-21
# Email: tarekadel314@gmail.com

######################################################imports########################################################
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QStackedWidget, QMessageBox, QTextEdit, QScrollArea,
                             QFrame, QGridLayout, QInputDialog,QDialog)
from PyQt6.QtGui import QPixmap,QFont
from PyQt6.QtCore import Qt
import sys
import json
import pandas as pd
import os 
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import IsolationForest
from sklearn.ensemble import RandomForestClassifier
#######################################################core##################################################
######################################################original data########################################################
sensor_data = [
    ("S1", "2025-04-28 10:00", 35.2, 12.1, 0.002),
    ("S2", "2025-04-28 10:00", 36.5, 14.0, 0.003),
    ("S1", "2025-04-28 11:00", 36.1, 12.5, 0.0021),
    ("S3", "2025-04-28 10:00", 34.0, 11.8, 0.0025),
    ("S2", "2025-04-28 11:00", 37.2, 14.3, 0.0031),
    ("S1", "2025-04-28 12:00", 37.0, 13.0, 0.0022),
]


################################################### Graduation Project ##########################################################################

#################################################Data Preparation########################################################
# Convert the list of tuples into a structured NumPy array or pandas DataFrame with labeled columns , Parse timestamps properly and ensure appropriate data types for each column
def convert_sensor_data_to_numpy_array_G(sensor_data):
    parsed_data = []
    for row in sensor_data:
        sensor_id = row[0]
        timestamp = datetime.strptime(row[1], "%Y-%m-%d %H:%M")  # here we convert to real time
        temperature = float(row[2])
        stress = float(row[3])
        displacement = float(row[4])
        parsed_data.append((sensor_id, timestamp, temperature, stress, displacement))
    return np.array(parsed_data, dtype=[
        ("SensorID", "U10"),
        ("Timestamp", "O"),  #  'O' for object type to store datetime
        ("Temperature", "f4"),
        ("Stress", "f4"),
        ("Displacement", "f4")
    ])

#####################################################Feature Extraction and Analysis########################################################

# Calculate the average temperature, stress, and displacement for each sensor
def calculate_average_per_sensor_G(sensor_data):
    data = convert_sensor_data_to_numpy_array_G(sensor_data)
    result = {}
    for row in data:
        sensor = row["SensorID"]
        if sensor not in result:
            result[sensor] = {"temp": [], "stress": [], "disp": []}
        result[sensor]["temp"].append(row["Temperature"])
        result[sensor]["stress"].append(row["Stress"])
        result[sensor]["disp"].append(row["Displacement"])
    
    avg_result = {}
    for sensor_id, values in result.items():
        avg_result[sensor_id] = {
            "avg_temp": float(np.mean(values["temp"])),
            "avg_stress": float(np.mean(values["stress"])),
            "avg_disp": float(np.mean(values["disp"])),
        }
    return avg_result


#  Identify the sensor with the highest average stress
def identify_sensor_with_highest_average_stress_G(sensor_data):
    averages = calculate_average_per_sensor(sensor_data)
    highest_sensor = max(averages.items(), key=lambda x: x[1]["avg_stress"])
    return highest_sensor[0], highest_sensor[1]["avg_stress"]

# Filter and extract all sensor readings where the temperature exceeds 36.0°C
def extract_readings_where_temperature_more_than_36_G(sensor_data):
    data = convert_sensor_data_to_numpy_array_G(sensor_data)
    return data[data["Temperature"] > 36.0]

# Create visualizations (e.g., line plots of stress over time) for better insight
def plot_stress_over_time(sensor_data):
    parsed_data = convert_sensor_data_to_numpy_array_G(sensor_data)

    df = pd.DataFrame(parsed_data)

    # إعداد الشكل
    plt.figure(figsize=(10, 6))

    # جروب حسب SensorID ورسم لكل واحد
    for sensor_id, group in df.groupby("SensorID"):
        plt.plot(group["Timestamp"], group["Stress"], marker='o', label=f"Sensor {sensor_id}")

    # عنوان، محاور، جريد
    plt.title("Stress over Time per Sensor")
    plt.xlabel("Time")
    plt.ylabel("Stress")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

##################################################Machine Learning Insight#####################################################

# Predictive maintenance
def train_predictive_maintenance_model(sensor_data):
    
    parsed_data = convert_sensor_data_to_numpy_array_G(sensor_data)
    df = pd.DataFrame(parsed_data)

    # Assuming we have a binary label for failure (1 for failure, 0 for normal operation)
    failure_labels = [0, 1, 1, 0, 1, 1]  
    df["Failure"] = failure_labels

    X = df[["Temperature", "Stress", "Displacement"]]
    y = df["Failure"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    # تقييم الموديل
    print("Predictive Maintenance Report:")
    print(classification_report(y_test, predictions))
    print("predections:", predictions)

    return model



# Anomaly detection
def detect_anomalies(sensor_data):
     
    parsed_data = convert_sensor_data_to_numpy_array_G(sensor_data)
    
    df = pd.DataFrame(parsed_data)
    
    features = df[["Temperature", "Stress", "Displacement"]]

    model = IsolationForest(contamination=0.2, random_state=42)
    df["Anomaly"] = model.fit_predict(features)

    anomalies = df[df["Anomaly"] == -1]
    print("Anomalies detected:")
    print(anomalies[["SensorID", "Timestamp", "Temperature", "Stress", "Displacement"]])

    return df

# Structural health prediction
def train_structural_health_prediction_model(sensor_data):
    parsed_data = convert_sensor_data_to_numpy_array_G(sensor_data)
    df = pd.DataFrame(parsed_data)

    conditions = []
    for _, row in df.iterrows():
        if row["Stress"] > 14.0 or row["Displacement"] > 0.003:
            conditions.append(2)  # حالة خطيرة
        elif row["Stress"] > 12.5 or row["Displacement"] > 0.0022:
            conditions.append(1)  # حالة متوسطة
        else:
            conditions.append(0)  # حالة سليمة
    df["HealthStatus"] = conditions

    # نحضّر البيانات
    X = df[["Temperature", "Stress", "Displacement"]]
    y = df["HealthStatus"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    model = RandomForestClassifier(random_state=0)
    model.fit(X_train, y_train)

    # تقييم الموديل
    y_pred = model.predict(X_test)
    print("Structural Health Prediction Report:")
    print(classification_report(y_test, y_pred))
    print("Predictions:", y_pred)

    return model


# final structured data console
def Grduation_Project_console():
    while True:
        print("\nGraduation Project Console Menu:")
        print("1. Convert the sensor data into a structured NumPy array")
        print("2. Compute average temperature, stress, and displacement per sensor")
        print("3. Identify the sensor with the highest average stress")
        print("4. Extract all readings where temperature > 36.0°C")
        print("5. Plot stress over time per sensor")
        print("6. Run Predictive Maintenance Model")
        print("7. Detect anomalies")
        print("8. Run Structural Health Prediction Model")
        print("9. Exit")

        x = input("Enter the number of the task you want to run: ")

        if x == "1":
            print(convert_sensor_data_to_numpy_array_G(sensor_data))
            print("--------------------------------")
        
        elif x == "2":
            results = calculate_average_per_sensor_G(sensor_data)
            for sensor, values in results.items():
                print(f"{sensor} => Temp: {values['avg_temp']}°C, Stress: {values['avg_stress']}, Disp: {values['avg_disp']}")
            print("--------------------------------")
        
        elif x == "3":
            sensor, avg_stress = identify_sensor_with_highest_average_stress_G(sensor_data)
            print(f"Sensor with highest average stress: {sensor} ({avg_stress})")
            print("--------------------------------")
        
        elif x == "4":
            high_temp_data = extract_readings_where_temperature_more_than_36_G(sensor_data)
            for row in high_temp_data:
                print(row)
            print("--------------------------------")
        
        elif x == "5":
            plot_stress_over_time(sensor_data)
            print("--------------------------------")

        elif x == "6":
            train_predictive_maintenance_model(sensor_data)
            print("--------------------------------")

        elif x == "7":
            detect_anomalies(sensor_data)
            print("--------------------------------")

        elif x == "8":
            train_structural_health_prediction_model(sensor_data)
            print("--------------------------------")

        elif x == "9":
            print("Goodbye!")
            break

        else:
            print("Plz enter a number between 1 and 9.")



#################################################### END #######################################################################
################################################### Task 8 Start #########################################################

# Convert the sensor data into a structured NumPy array
def convert_sensor_data_to_numpy_array(sensor_data):
    return np.array(sensor_data, dtype=[
        ("SensorID", "U10"),
        ("Timestamp", "U20"),
        ("Temperature", "f4"),
        ("Stress", "f4"),
        ("Displacement", "f4")
    ])

# Calculate the average temperature, stress, and displacement for each sensor
def calculate_average_per_sensor(sensor_data):
    data = convert_sensor_data_to_numpy_array(sensor_data)
    result = {}
    for row in data:
        sensor = row["SensorID"]
        if sensor not in result:
            result[sensor] = {"temp": [], "stress": [], "disp": []}
        result[sensor]["temp"].append(row["Temperature"])
        result[sensor]["stress"].append(row["Stress"])
        result[sensor]["disp"].append(row["Displacement"])
    
    avg_result = {}
    for sensor_id, values in result.items():
        avg_result[sensor_id] = {
            "avg_temp": float(np.mean(values["temp"])),
            "avg_stress": float(np.mean(values["stress"])),
            "avg_disp": float(np.mean(values["disp"])),
        }
    return avg_result

# Identify the sensor with the highest average stress
def identify_sensor_with_highest_average_stress(sensor_data):
    averages = calculate_average_per_sensor(sensor_data)
    highest_sensor = max(averages.items(), key=lambda x: x[1]["avg_stress"])
    return highest_sensor[0], highest_sensor[1]["avg_stress"]

# Extract all readings where temperature > 36.0°C
def extract_readings_where_temperature_more_than_36(sensor_data):
    data = convert_sensor_data_to_numpy_array(sensor_data)
    return data[data["Temperature"] > 36.0]

# Main console of task 8 
def task_8_console():
    while True:
        print("\n1. Convert the sensor data into a structured NumPy array")
        print("2. Calculate the average temperature, stress, and displacement for each sensor")
        print("3. Identify the sensor with the highest average stress")
        print("4. Extract all readings where temperature > 36.0°C")
        print("5. Exit")
        
        x = input("Enter the number of the task you want to run: ")

        if x == "1":
            print(convert_sensor_data_to_numpy_array(sensor_data))
            print("--------------------------------")
        
        elif x == "2":
            results = calculate_average_per_sensor(sensor_data)
            for sensor, values in results.items():
                print(f"{sensor} => Temp: {values['avg_temp']}°C, Stress: {values['avg_stress']}, Disp: {values['avg_disp']}")
            print("--------------------------------")
        
        elif x == "3":
            sensor, avg_stress = identify_sensor_with_highest_average_stress(sensor_data)
            print(f"Sensor with highest average stress: {sensor} ({avg_stress})")
            print("--------------------------------")
        
        elif x == "4":
            high_temp_data = extract_readings_where_temperature_more_than_36(sensor_data)
            for row in high_temp_data:
                print(row)
            print("--------------------------------")
        
        elif x == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")













################################################### Task 8 End #########################################################

###############################################task 7 Start########################################################
def convert_sensor_data_to_dataframe(sensor_data):
    df = pd.DataFrame(sensor_data, columns=["SensorID", "Timestamp", "Temperature", "Stress", "Displacement"])
    df["Timestamp"] = pd.to_datetime(df["Timestamp"]) 
    return df


# Compute and display the average temperature, stress, and displacement per sensor
temp_per_sensor=convert_sensor_data_to_dataframe(sensor_data).groupby("SensorID")["Temperature"].mean()
stress_per_sensor=convert_sensor_data_to_dataframe(sensor_data).groupby("SensorID")["Stress"].mean()
displacement_per_sensor=convert_sensor_data_to_dataframe(sensor_data).groupby("SensorID")["Displacement"].mean()


# Identify the sensor with the highest average temperature
def highest_temp_sensor(temp_per_sensor):
    highest_temp_sensor=temp_per_sensor.idxmax()
    print(f"The sensor with the highest average temperature is {highest_temp_sensor}")
    return highest_temp_sensor
highest_temp_sensor(temp_per_sensor)

# Plot a line chart of temperature vs. time for each sensor (use different colors)  , Add markers for the data points
def plot_temperature_vs_time(sensor_data):
    df = convert_sensor_data_to_dataframe(sensor_data)

    plt.figure(figsize=(10, 6))

    sensors = df["SensorID"].unique()

    for sensor_id in sensors:
        sensor_df = df[df["SensorID"] == sensor_id]
        plt.plot(sensor_df["Timestamp"], sensor_df["Temperature"], 
                 marker='o', label=f"Sensor {sensor_id}") 

    plt.xlabel("Time")
    plt.ylabel("Temperature (℃)")
    plt.title("Temperature vs Time per Sensor")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()


# Create a scatter plot showing the relationship between stress and displacement.
def plot_stress_vs_displacement(sensor_data):
    df = convert_sensor_data_to_dataframe(sensor_data)
    sensors = df["SensorID"].unique()

    plt.figure(figsize=(8, 6))
    for sensor_id in sensors:
        sensor_df = df[df["SensorID"] == sensor_id]
        plt.scatter(sensor_df["Stress"], sensor_df["Displacement"], label=f"Sensor {sensor_id}")

    plt.xlabel("Stress")
    plt.ylabel("Displacement")
    plt.title("Stress vs Displacement per Sensor")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()



def task_7_console():
    while True:
        print("1. Convert sensor data to dataframe")
        print("2. Compute and display the average temperature, stress, and displacement per sensor")
        print("3. Identify the sensor with the highest average temperature")
        print("4. Plot a line chart of temperature vs. time for each sensor")
        print("5. Create a scatter plot showing the relationship between stress and displacement")
        print("6. Exit")
        x=input("Enter the number of the task you want to run:")
        if x == "1":
            print(convert_sensor_data_to_dataframe(sensor_data))
            print("--------------------------------")
        elif x == "2":
            print(temp_per_sensor)
            print(stress_per_sensor)
            print(displacement_per_sensor)
            print("--------------------------------")
        elif x == "3":
            print(highest_temp_sensor(temp_per_sensor))
            print("--------------------------------")
        elif x == "4":
            plot_temperature_vs_time(sensor_data)
            print("--------------------------------")
        elif x == "5":
            plot_stress_vs_displacement(sensor_data)
            print("--------------------------------")
        elif x == "6":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")




###############################################task 7 End########################################################
###################################################################################################################
# Organize readings per sensor
def organize_readings(sensor_data):
    reading_sensor={}
    for sensor in sensor_data:
        sensor_id, timestamp, temperature, stress, displacement = sensor
        if sensor_id not in reading_sensor:
            reading_sensor[sensor_id]=[]
        reading_sensor[sensor_id].append({"timestamp":timestamp, "temperature":temperature,"stress": stress, "displacement":displacement})
    return reading_sensor

def show_data_before_and_after(original_data, organized_data):
    
    print("Data before organizing:")
    print(original_data)
    print("\nData after organizing:")
    print(organized_data)



#####################################################################################################################


# Identify unique sensors with extreme values
def Extreme_sensors(data):
    extreme_sensors=[]
    max_temp = float('-inf')  #save maximum temperature
    min_temp = float('inf')   #save minimum temperature
    max_temp_sensor = 0   #save sensor id with maximum temperature
    min_temp_sensor = 0 #save sensor id with minimum temperature

# for loop to find the sensor with maximum and minimum temperature
    for  sensor_id,readings in data.items():
        for reading in readings:
            if reading["temperature"] > max_temp:
                max_temp = reading["temperature"]
                max_temp_sensor = sensor_id
            if reading["temperature"] < min_temp:
                min_temp = reading["temperature"]
                min_temp_sensor = sensor_id
    print(f"Sensor with max temperature: {max_temp_sensor} with extreme value in temperature: {max_temp}℃")
    print(f"Sensor with min temperature: {min_temp_sensor} with extreme value in temperature: {min_temp}℃")
    extreme_sensors.append(f"Sensor with max temperature: {max_temp_sensor} with extreme value in temperature: {max_temp}℃")
    extreme_sensors.append(f"Sensor with min temperature: {min_temp_sensor} with extreme value in temperature: {min_temp}℃")
    return extreme_sensors



###########################################################################################################################
#Compare readings from different time intervals
def Compare_readings(data):
    readings_data=[]
    for sensor_id, readings in data.items():
        if len(readings) < 2:
            print(f"Sensor {sensor_id} has one time reading which is {readings[0]['temperature']}℃ at {readings[0]['timestamp']}")
            readings_data.append(f"Sensor {sensor_id} has one time reading which is {readings[0]['temperature']}℃ at {readings[0]['timestamp']}")
            continue
        for i in range(len(readings)-1):
            current_reading = readings[i]
            next_reading=readings[i+1]
            temp_diff = next_reading["temperature"] - current_reading["temperature"]
            if temp_diff > 0:
                print(f"Sensor {sensor_id} has a temperature increased of {abs(temp_diff):.2f} between {current_reading['timestamp']} and {next_reading['timestamp']}")
                readings_data.append(f"Sensor {sensor_id} has a temperature increased of {abs(temp_diff):.2f} between {current_reading['timestamp']} and {next_reading['timestamp']}")
            elif temp_diff < 0:
                print(f"Sensor {sensor_id} has a temperature decreased of {abs(temp_diff):.2f} between {current_reading['timestamp']} and {next_reading['timestamp']}")
                readings_data.append(f"Sensor {sensor_id} has a temperature decreased of {abs(temp_diff):.2f} between {current_reading['timestamp']} and {next_reading['timestamp']}")
            else:
                print(f"Sensor {sensor_id} has a constant temperature between {current_reading['timestamp']} and {next_reading['timestamp']}")
                readings_data.append(f"Sensor {sensor_id} has a constant temperature between {current_reading['timestamp']} and {next_reading['timestamp']}")
    return readings_data


########################################################################################################################################


#Summarize the data by calculating max, min, and average readings per sensor
#Calculate statistics per sensor
def Summarize_data(data, choice=None):
    summarize_data=[]
    print("Which data do you want to show?")
    print("1. Temperature")
    print("2. Stress")
    print("3. Displacement")
    print("4. All")
    if choice is None:
        choice = input("Enter your choice (1-4): ")
    else:
        print(f"Choice: {choice}")
    for sensor_id, readings in data.items():
        temperatures=[]
        for r in readings:  # traditional way to extract temperature values and store them in a list
             temperatures.append(r["temperature"])
        stress=[r["stress"] for r in readings] # modern way to extract stress values and store them in a list
        displacements=[r["displacement"] for r in readings] # store displacements in a list
        temp_max=max(temperatures) # find maximum temperature
        temp_min=min(temperatures) # find minimum temperature
        tem_avg=sum(temperatures)/len(temperatures) # find average temperature
        stress_max=max(stress) # find maximum stress
        stress_min=min(stress) # find minimum stress
        stress_avg=sum(stress)/len(stress) # find average stress
        displacement_max=max(displacements) # find maximum displacement
        displacement_min=min(displacements) # find minimum displacement
        displacement_avg=sum(displacements)/len(displacements) # find average displacement
        # Print the statistics for each sensor
        print(f"\nSensor {sensor_id} has the following statistics:")
        summarize_data.append(f"\nSensor {sensor_id} has the following statistics:")
        if choice == "1":
            print(f"Max temperature: {temp_max:.2f}℃ and min temperature: {temp_min:.2f} and average temperature: {tem_avg:.2f}")
            summarize_data.append(f"Max temperature: {temp_max:.2f}℃ and min temperature: {temp_min:.2f} and average temperature: {tem_avg:.2f}")
        elif choice == "2":
            print(f"Max stress: {stress_max:.2f} and min stress: {stress_min:.2f} and average stress: {stress_avg:.2f}")
            summarize_data.append(f"Max stress: {stress_max:.2f} and min stress: {stress_min:.2f} and average stress: {stress_avg:.2f}")
        elif choice == "3":
            print(f"Max displacement: {displacement_max} and min displacement: {displacement_min} and average displacement: {displacement_avg}")
            summarize_data.append(f"Max displacement: {displacement_max} and min displacement: {displacement_min} and average displacement: {displacement_avg}")
        elif choice == "4":
            print(f"Max temperature: {temp_max:.2f}℃ and min temperature: {temp_min:.2f} and average temperature: {tem_avg:.2f}")
            summarize_data.append(f"Max temperature: {temp_max:.2f}℃ and min temperature: {temp_min:.2f} and average temperature: {tem_avg:.2f}")
            print(f"Max stress: {stress_max:.2f} and min stress: {stress_min:.2f} and average stress: {stress_avg:.2f}")
            summarize_data.append(f"Max stress: {stress_max:.2f} and min stress: {stress_min:.2f} and average stress: {stress_avg:.2f}")
            print(f"Max displacement: {displacement_max} and min displacement: {displacement_min} and average displacement: {displacement_avg}")
            summarize_data.append(f"Max displacement: {displacement_max} and min displacement: {displacement_min} and average displacement: {displacement_avg}")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            return 0
    return summarize_data


################################################################################################################################

#Group data by sensor using a dictionary (sensor_id as key, list of tuples as value)
def Group_data_by_sensor(original_data):
    print("Before grouping:")
    print(original_data)
    grouped_data = {}
    for sensor_id, timestamp, temperature, stress, displacement in original_data:
        if sensor_id not in grouped_data:
            grouped_data[sensor_id] = []
        grouped_data[sensor_id].append((timestamp, temperature, stress, displacement))
    #show the new data structure
    for sensor_id, readings in grouped_data.items():
        print(f"\nSensor {sensor_id} has the following readings:")
        for reading in readings:
            print(f"Timestamp: {reading[0]}, Temperature: {reading[1]}℃, Stress: {reading[2]}, Displacement: {reading[3]}")
    print("\nAfter grouping:")
    print(grouped_data)
    return grouped_data
###############################################################################################################################

#Use sets to find unique sensor IDs that recorded stress > 13.0
def unique_sensor_set(original_data):
    unique_sensor=set() 
    unique_sensor_list=[]
    unique_sensor_value=0
    for sensor_id, _, _, stress, _ in original_data:
        if stress > 13.0:
            unique_sensor.add(sensor_id)
    unique_sensor_value=unique_sensor.pop()
    print(f"{unique_sensor_value} has a stress value greater than 13.0")
    unique_sensor_list.append(f"{unique_sensor_value} has a stress value greater than 13.0")
    return unique_sensor_list


################################################################################################################################

#Max, min, and average temperature
#Max displacement
def max_and_min_values(data):
    max_and_min_values_list=[]
    max_temp = float('-inf')  #save maximum temperature
    min_temp = float('inf')   #save minimum temperature
    avg_temp = 0 #save average temperature
    max_displacement = float('-inf') #save maximum displacement
    # for loop to find the sensor with maximum and minimum temperature
    for  sensor_id,readings in data.items():
        for reading in readings:
            if reading["temperature"] > max_temp:
                max_temp = reading["temperature"]
            if reading["temperature"] < min_temp:
                min_temp = reading["temperature"]
            if reading["displacement"] > max_displacement:
                max_displacement = reading["displacement"]
            if reading["temperature"] > 0:
                avg_temp += reading["temperature"]
    avg_temp /= len(sensor_data) # calculate average temperature
    print(f"The maximum temperature is {max_temp}℃ and the minimum temperature is {min_temp}℃ and the average temperature is {avg_temp:.2f}℃")
    max_and_min_values_list.append(f"The maximum temperature is {max_temp}℃ and the minimum temperature is {min_temp}℃ and the average temperature is {avg_temp:.2f}℃")
    print(f"The maximum value in displacement: {max_displacement}m")
    max_and_min_values_list.append(f"The maximum value in displacement: {max_displacement}m")
    return max_and_min_values_list



################################################################################################################################################


#Extract all timestamps into a list and sort them
def timestapms_extracted(data, choice=None):
    print("You want all timestamps? or you want witout duplicates?")
    print("1. All timestamps")
    print("2. Timestamps without duplicates")
    if choice is None:
        choice = input("Enter your choice (1-2): ")
    else:
        print(f"Choice: {choice}")
    timestamps = []
    for readings in data.values():
        for reading in readings:
            timestamps.append(reading["timestamp"])
    if choice == "1": ## Sort the timestamps
        timestamps = sorted(timestamps)  
    elif choice == "2": ## Remove duplicates and sort the timestamps
        timestamps = sorted(set(timestamps))
    else:
        print("Invalid choice. Please enter a number between 1 and 2.")
    
    print(f"Sorted timestamps: {timestamps}")## Print the sorted timestamps
    return timestamps




########################################################################################################################################


#Create a tuple of the most recent reading for each sensor
def most_recent_reading(data):
    recent_readings = tuple() # Create an empty tuple to store the most recent readings
    most_recent_reading_list=[]
    for sensor_id, readings in data.items():
        if readings:
            most_recent = readings[-1] # Get last reading for each sensor
            recent_readings += (sensor_id, most_recent["timestamp"], most_recent["temperature"], most_recent["stress"], most_recent["displacement"])
    print(recent_readings) # Print the tuple of most recent readings for each sensor
    most_recent_reading_list.append(recent_readings)
    return most_recent_reading_list


########################################################################################################################################


def Organize_readings_per_sensor_save_to_excel(data):
    max_len=max(len(v)for v in data.values())
    formated_data={}
    for sensor_id, readings in data.items():
        reading_str = [str(r) for r in readings]
        reading_str+=[None]*(max_len-len(readings))
        formated_data[sensor_id]=reading_str    
    df_sensor_reading=pd.DataFrame(formated_data)
    file_name="sensor_readings.xlsx"
    mode=""
    if_sheet_exists=""
    if os.path.exists(file_name):
        mode="a"
        if_sheet_exists="replace"
    else:
        mode="w"
        if_sheet_exists=None
    with pd.ExcelWriter(file_name, engine="openpyxl",mode=mode,if_sheet_exists=if_sheet_exists) as writer:
        df_sensor_reading.to_excel(writer, sheet_name="reading_sensorsensors", index=False)



def Extreme_sensors_save_to_excel(data):
    df_extream=pd.DataFrame({"max and min":data})
    file_name="sensor_readings.xlsx"
    mode=""
    if_sheet_exists=""
    if os.path.exists(file_name):
        mode="a"
        if_sheet_exists="replace"
    else:
        mode="w"
        if_sheet_exists=None
    with pd.ExcelWriter(file_name, engine="openpyxl",mode=mode,if_sheet_exists=if_sheet_exists) as writer:
        df_extream.to_excel(writer, sheet_name="Extreme_sensors", index=False)



def Compare_readings_save_to_excel(data):
    df_compare_readings=pd.DataFrame({"Compare_readings":data})
    file_name="sensor_readings.xlsx"
    mode=""
    if_sheet_exists=""
    if os.path.exists(file_name):
        mode="a"
        if_sheet_exists="replace"
    else:
        mode="w"
        if_sheet_exists=None
    with pd.ExcelWriter(file_name, engine="openpyxl",mode=mode,if_sheet_exists=if_sheet_exists) as writer:
        df_compare_readings.to_excel(writer, sheet_name="Compare_readings", index=False)


def Summarize_data_save_to_excel(data):
    df_summarize=pd.DataFrame({"Summarize_data":data})
    file_name="sensor_readings.xlsx"
    mode=""
    if_sheet_exists=""
    if os.path.exists(file_name):
        mode="a"
        if_sheet_exists="replace"
    else:
        mode="w"
        if_sheet_exists=None
    with pd.ExcelWriter(file_name, engine="openpyxl",mode=mode,if_sheet_exists=if_sheet_exists) as writer:
        df_summarize.to_excel(writer, sheet_name="Summarize_data", index=False)



def Group_data_by_sensor_save_to_excel(data):
    df_grouped=pd.DataFrame({"Group_data_by_sensor":list(data.items())})
    file_name="sensor_readings.xlsx"
    mode=""
    if_sheet_exists=""
    if os.path.exists(file_name):
        mode="a"
        if_sheet_exists="replace"
    else:
        mode="w"
        if_sheet_exists=None
    with pd.ExcelWriter(file_name, engine="openpyxl",mode=mode,if_sheet_exists=if_sheet_exists) as writer:
        df_grouped.to_excel(writer, sheet_name="Group_data_by_sensor", index=False)




def unique_sensor_set_save_to_excel(data):
    df_unique=pd.DataFrame({"Unique_sensor_set":data})
    file_name="sensor_readings.xlsx"
    mode=""
    if_sheet_exists=""
    if os.path.exists(file_name):
        mode="a"
        if_sheet_exists="replace"
    else:
        mode="w"
        if_sheet_exists=None
    with pd.ExcelWriter(file_name, engine="openpyxl",mode=mode,if_sheet_exists=if_sheet_exists) as writer:
        df_unique.to_excel(writer, sheet_name="Unique_sensor_set", index=False)





def max_and_min_values_save_to_excel(data):
    df_max_and_min_values=pd.DataFrame({"max and min":data})
    file_name="sensor_readings.xlsx"
    mode=""
    if_sheet_exists=""
    if os.path.exists(file_name):
        mode="a"
        if_sheet_exists="replace"
    else:
        mode="w"
        if_sheet_exists=None
    with pd.ExcelWriter(file_name, engine="openpyxl",mode=mode,if_sheet_exists=if_sheet_exists) as writer:
        df_max_and_min_values.to_excel(writer, sheet_name="max_and_min_values", index=False)





def timestamps_save_to_excel(data):
    df_timestamps=pd.DataFrame({"timestamps":data})
    file_name="sensor_readings.xlsx"
    mode=""
    if_sheet_exists=""
    if os.path.exists(file_name):
        mode="a"
        if_sheet_exists="replace"
    else:
        mode="w"
        if_sheet_exists=None
    with pd.ExcelWriter(file_name, engine="openpyxl",mode=mode,if_sheet_exists=if_sheet_exists) as writer:
        df_timestamps.to_excel(writer, sheet_name="timestamps", index=False)




def most_recent_reading_save_to_excel(data):
    df_most_recent_reading=pd.DataFrame({"most_recent_reading":data})
    file_name="sensor_readings.xlsx"
    mode=""
    if_sheet_exists=""
    if os.path.exists(file_name):
        mode="a"
        if_sheet_exists="replace"
    else:
        mode="w"
        if_sheet_exists=None
    with pd.ExcelWriter(file_name, engine="openpyxl",mode=mode,if_sheet_exists=if_sheet_exists) as writer:
        df_most_recent_reading.to_excel(writer, sheet_name="most_recent_reading", index=False)


########################################################################################################################

def write_to_json(data,json_file_name):
    with open(json_file_name, "w") as json_file:
        json.dump(data, json_file)




##################################################core end########################################################
##############################################################################################################################
######################################################### GUI ##############################################################

class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.users = {}  # Dictionary to store user credentials
        self.current_user = None
        self.load_users_from_file()  # Load existing users
        self.init_ui()
        
    def load_users_from_file(self):
        """Load user data from file"""
        try:
            if os.path.exists("users.txt"):
                with open("users.txt", "r") as file:
                    for line in file:
                        line = line.strip()
                        if line and "|" in line:
                            parts = line.split("|")
                            if len(parts) == 3:
                                name, email, password = parts
                                self.users[email] = {
                                    'name': name,
                                    'password': password
                                }
        except Exception as e:
            print(f"Could not load user data from file: {e}")
            
    def save_users_to_file(self):
        """Save updated user data to file"""
        try:
            with open("users.txt", "w") as file:
                for email, user_data in self.users.items():
                    file.write(f"{user_data['name']}|{email}|{user_data['password']}\n")
        except Exception as e:
            QMessageBox.warning(self, "Warning", f"Could not save user data to file: {e}")
        
    def init_ui(self):
        self.setWindowTitle("Company Login System - Sensor Data Analysis")
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet("background-color: #90EE90;")  # Light green background
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add company logo
        logo_label = QLabel()
        logo_pixmap = QPixmap("logo_5e37c4cd90a4c.png")
        if not logo_pixmap.isNull():
            logo_pixmap = logo_pixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            logo_label.setPixmap(logo_pixmap)
            logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            main_layout.addWidget(logo_label)
        
        # Create stacked widget for all pages
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)
        
        # Create login page
        self.login_page = self.create_login_page()
        self.stacked_widget.addWidget(self.login_page)
        
        # Create signup page
        self.signup_page = self.create_signup_page()
        self.stacked_widget.addWidget(self.signup_page)
        
        # Create dashboard page
        self.dashboard_page = self.create_dashboard_page()
        self.stacked_widget.addWidget(self.dashboard_page)
        
        # Show login page by default
        self.stacked_widget.setCurrentIndex(0)
        
    def create_login_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(20)
        layout.setContentsMargins(50, 30, 50, 30)
        
        # Title
        title = QLabel("Welcome Back!")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #2E8B57; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Email input
        email_label = QLabel("Email:")
        email_label.setFont(QFont("Arial", 12))
        email_label.setStyleSheet("color: #2E8B57; font-weight: bold;")
        layout.addWidget(email_label)
        
        self.login_email = QLineEdit()
        self.login_email.setPlaceholderText("Enter your email")
        self.login_email.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 2px solid #2E8B57;
                border-radius: 8px;
                font-size: 14px;
                background-color: black;
                color: white;
            }
            QLineEdit:focus {
                border: 2px solid #228B22;
            }
        """)
        layout.addWidget(self.login_email)
        
        # Password input
        password_label = QLabel("Password:")
        password_label.setFont(QFont("Arial", 12))
        password_label.setStyleSheet("color: #2E8B57; font-weight: bold;")
        layout.addWidget(password_label)
        
        self.login_password = QLineEdit()
        self.login_password.setPlaceholderText("Enter your password")
        self.login_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_password.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 2px solid #2E8B57;
                border-radius: 8px;
                font-size: 14px;
                background-color: black;
                color: white;
            }
            QLineEdit:focus {
                border: 2px solid #228B22;
            }
        """)
        layout.addWidget(self.login_password)
        
        # Login button
        login_btn = QPushButton("Login")
        login_btn.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        login_btn.setStyleSheet("""
            QPushButton {
                background-color: #2E8B57;
                color: white;
                padding: 12px;
                border: none;
                border-radius: 8px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #228B22;
            }
            QPushButton:pressed {
                background-color: #006400;
            }
        """)
        login_btn.clicked.connect(self.login)
        layout.addWidget(login_btn)
        
        # Signup link
        signup_layout = QHBoxLayout()
        signup_layout.addStretch()
        
        signup_text = QLabel("Don't have an account?")
        signup_text.setStyleSheet("color: #2E8B57;")
        signup_layout.addWidget(signup_text)
        
        signup_link = QPushButton("Sign Up")
        signup_link.setStyleSheet("""
            QPushButton {
                background: none;
                border: none;
                color: #0066CC;
                text-decoration: underline;
                font-weight: bold;
            }
            QPushButton:hover {
                color: #003366;
            }
        """)
        signup_link.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        signup_layout.addWidget(signup_link)
        signup_layout.addStretch()
        
        layout.addLayout(signup_layout)
        layout.addStretch()
        
        return page
        
    def create_signup_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(20)
        layout.setContentsMargins(50, 30, 50, 30)
        
        # Title
        title = QLabel("Create Account")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #2E8B57; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Name input
        name_label = QLabel("Full Name:")
        name_label.setFont(QFont("Arial", 12))
        name_label.setStyleSheet("color: #2E8B57; font-weight: bold;")
        layout.addWidget(name_label)
        
        self.signup_name = QLineEdit()
        self.signup_name.setPlaceholderText("Enter your full name")
        self.signup_name.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 2px solid #2E8B57;
                border-radius: 8px;
                font-size: 14px;
                background-color: black;
                color: white;
            }
            QLineEdit:focus {
                border: 2px solid #228B22;
            }
        """)
        layout.addWidget(self.signup_name)
        
        # Email input
        email_label = QLabel("Email:")
        email_label.setFont(QFont("Arial", 12))
        email_label.setStyleSheet("color: #2E8B57; font-weight: bold;")
        layout.addWidget(email_label)
        
        self.signup_email = QLineEdit()
        self.signup_email.setPlaceholderText("Enter your email")
        self.signup_email.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 2px solid #2E8B57;
                border-radius: 8px;
                font-size: 14px;
                background-color: black;
                color: white;
            }
            QLineEdit:focus {
                border: 2px solid #228B22;
            }
        """)
        layout.addWidget(self.signup_email)
        
        # Password input
        password_label = QLabel("Password:")
        password_label.setFont(QFont("Arial", 12))
        password_label.setStyleSheet("color: #2E8B57; font-weight: bold;")
        layout.addWidget(password_label)
        
        self.signup_password = QLineEdit()
        self.signup_password.setPlaceholderText("Enter your password")
        self.signup_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.signup_password.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 2px solid #2E8B57;
                border-radius: 8px;
                font-size: 14px;
                background-color: black;
                color: white;
            }
            QLineEdit:focus {
                border: 2px solid #228B22;
            }
        """)
        layout.addWidget(self.signup_password)
        
        # Confirm Password input
        confirm_label = QLabel("Confirm Password:")
        confirm_label.setFont(QFont("Arial", 12))
        confirm_label.setStyleSheet("color: #2E8B57; font-weight: bold;")
        layout.addWidget(confirm_label)
        
        self.signup_confirm = QLineEdit()
        self.signup_confirm.setPlaceholderText("Confirm your password")
        self.signup_confirm.setEchoMode(QLineEdit.EchoMode.Password)
        self.signup_confirm.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 2px solid #2E8B57;
                border-radius: 8px;
                font-size: 14px;
                background-color: black;
                color: white;
            }
            QLineEdit:focus {
                border: 2px solid #228B22;
            }
        """)
        layout.addWidget(self.signup_confirm)
        
        # Signup button
        signup_btn = QPushButton("Sign Up")
        signup_btn.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        signup_btn.setStyleSheet("""
            QPushButton {
                background-color: #2E8B57;
                color: white;
                padding: 12px;
                border: none;
                border-radius: 8px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #228B22;
            }
            QPushButton:pressed {
                background-color: #006400;
            }
        """)
        signup_btn.clicked.connect(self.signup)
        layout.addWidget(signup_btn)
        
        # Login link
        login_layout = QHBoxLayout()
        login_layout.addStretch()
        
        login_text = QLabel("Already have an account?")
        login_text.setStyleSheet("color: #2E8B57;")
        login_layout.addWidget(login_text)
        
        login_link = QPushButton("Login")
        login_link.setStyleSheet("""
            QPushButton {
                background: none;
                border: none;
                color: #0066CC;
                text-decoration: underline;
                font-weight: bold;
            }
            QPushButton:hover {
                color: #003366;
            }
        """)
        login_link.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        login_layout.addWidget(login_link)
        login_layout.addStretch()
        
        layout.addLayout(login_layout)
        layout.addStretch()
        
        return page
        
    def create_dashboard_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 20, 30, 20)
        
        # Header with user info and logout
        header_layout = QHBoxLayout()
        
        self.welcome_label = QLabel("Welcome!")
        self.welcome_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.welcome_label.setStyleSheet("color: #2E8B57;")
        header_layout.addWidget(self.welcome_label)
        
        header_layout.addStretch()
        
        # Settings button
        settings_btn = QPushButton("Settings")
        settings_btn.setStyleSheet("""
            QPushButton {
                background-color: #4682B4;
                color: white;
                padding: 8px 16px;
                border: none;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #357ABD;
            }
        """)
        settings_btn.clicked.connect(self.show_settings)
        header_layout.addWidget(settings_btn)
        
        logout_btn = QPushButton("Logout")
        logout_btn.setStyleSheet("""
            QPushButton {
                background-color: #DC143C;
                color: white;
                padding: 8px 16px;
                border: none;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #B22222;
            }
        """)
        logout_btn.clicked.connect(self.logout)
        header_layout.addWidget(logout_btn)
        
        layout.addLayout(header_layout)
        
        # Title
        title = QLabel("Sensor Data Analysis Dashboard")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #2E8B57; margin: 20px 0;")
        layout.addWidget(title)
        
        # Create scrollable area for buttons
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
        """)
        
        scroll_widget = QWidget()
        scroll_layout = QGridLayout(scroll_widget)
        scroll_layout.setSpacing(15)
        
        # Create buttons for all functions
        buttons = [
            ("Organize Readings per Sensor", self.organize_readings_ui),
            ("Identify Extreme Sensors", self.extreme_sensors_ui),
            ("Compare Readings", self.compare_readings_ui),
            ("Summarize Data", self.summarize_data_ui),
            ("Group Data by Sensor", self.group_data_ui),
            ("Find High Stress Sensors", self.unique_sensor_ui),
            ("Calculate Statistics", self.calculate_statistics_ui),
            ("Max/Min Values", self.max_min_values_ui),
            ("Extract Timestamps", self.timestamps_ui),
            ("Most Recent Readings", self.most_recent_ui)
        ]
        
        for i, (text, func) in enumerate(buttons):
            btn = QPushButton(text)
            btn.setFont(QFont("Arial", 12, QFont.Weight.Bold))
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #2E8B57;
                    color: white;
                    padding: 15px;
                    border: none;
                    border-radius: 10px;
                    font-size: 14px;
                    min-height: 60px;
                }
                QPushButton:hover {
                    background-color: #228B22;
                    transform: scale(1.05);
                }
                QPushButton:pressed {
                    background-color: #006400;
                }
            """)
            btn.clicked.connect(func)
            scroll_layout.addWidget(btn, i // 2, i % 2)
        
        scroll_area.setWidget(scroll_widget)
        layout.addWidget(scroll_area)
        
        # Results area
        self.results_text = QTextEdit()
        self.results_text.setFont(QFont("Consolas", 10))
        self.results_text.setStyleSheet("""
            QTextEdit {
                background-color: white;
                border: 2px solid #2E8B57;
                border-radius: 8px;
                padding: 10px;
                color: #333;
            }
        """)
        self.results_text.setMaximumHeight(200)
        layout.addWidget(self.results_text)
        
        return page
        
    def show_settings(self):
        # Find current user's email
        current_email = None
        for email, user_data in self.users.items():
            if user_data['name'] == self.current_user:
                current_email = email
                break
        
        if not current_email:
            QMessageBox.critical(self, "Error", "User data not found!")
            return
        
        # Create settings dialog
        dialog = QDialog(self)
        dialog.setWindowTitle("Settings - Profile Management")
        dialog.setGeometry(100, 100, 500, 600)
        dialog.setStyleSheet("background-color: #90EE90;")
        
        layout = QVBoxLayout(dialog)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title = QLabel("Profile Settings")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #2E8B57; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Current Password (required to make changes)
        old_pass_label = QLabel("Current Password:")
        old_pass_label.setFont(QFont("Arial", 12))
        old_pass_label.setStyleSheet("color: #2E8B57; font-weight: bold;")
        layout.addWidget(old_pass_label)
        
        old_password = QLineEdit()
        old_password.setPlaceholderText("Enter your current password")
        old_password.setEchoMode(QLineEdit.EchoMode.Password)
        old_password.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 2px solid #2E8B57;
                border-radius: 8px;
                font-size: 14px;
                background-color: black;
                color: white;
            }
            QLineEdit:focus {
                border: 2px solid #228B22;
            }
        """)
        layout.addWidget(old_password)
        
        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setStyleSheet("background-color: #2E8B57; margin: 20px 0;")
        layout.addWidget(separator)
        
        # New Full Name
        name_label = QLabel("New Full Name:")
        name_label.setFont(QFont("Arial", 12))
        name_label.setStyleSheet("color: #2E8B57; font-weight: bold;")
        layout.addWidget(name_label)
        
        new_name = QLineEdit()
        new_name.setPlaceholderText("Enter new full name")
        new_name.setText(self.current_user)
        new_name.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 2px solid #2E8B57;
                border-radius: 8px;
                font-size: 14px;
                background-color: black;
                color: white;
            }
            QLineEdit:focus {
                border: 2px solid #228B22;
            }
        """)
        layout.addWidget(new_name)
        
        # New Email
        email_label = QLabel("New Email:")
        email_label.setFont(QFont("Arial", 12))
        email_label.setStyleSheet("color: #2E8B57; font-weight: bold;")
        layout.addWidget(email_label)
        
        new_email = QLineEdit()
        new_email.setPlaceholderText("Enter new email")
        new_email.setText(current_email)
        new_email.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 2px solid #2E8B57;
                border-radius: 8px;
                font-size: 14px;
                background-color: black;
                color: white;
            }
            QLineEdit:focus {
                border: 2px solid #228B22;
            }
        """)
        layout.addWidget(new_email)
        
        # New Password
        password_label = QLabel("New Password:")
        password_label.setFont(QFont("Arial", 12))
        password_label.setStyleSheet("color: #2E8B57; font-weight: bold;")
        layout.addWidget(password_label)
        
        new_password = QLineEdit()
        new_password.setPlaceholderText("Enter new password (leave blank to keep current)")
        new_password.setEchoMode(QLineEdit.EchoMode.Password)
        new_password.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 2px solid #2E8B57;
                border-radius: 8px;
                font-size: 14px;
                background-color: black;
                color: white;
            }
            QLineEdit:focus {
                border: 2px solid #228B22;
            }
        """)
        layout.addWidget(new_password)
        
        # Confirm New Password
        confirm_label = QLabel("Confirm New Password:")
        confirm_label.setFont(QFont("Arial", 12))
        confirm_label.setStyleSheet("color: #2E8B57; font-weight: bold;")
        layout.addWidget(confirm_label)
        
        confirm_password = QLineEdit()
        confirm_password.setPlaceholderText("Confirm new password")
        confirm_password.setEchoMode(QLineEdit.EchoMode.Password)
        confirm_password.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 2px solid #2E8B57;
                border-radius: 8px;
                font-size: 14px;
                background-color: black;
                color: white;
            }
            QLineEdit:focus {
                border: 2px solid #228B22;
            }
        """)
        layout.addWidget(confirm_password)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        save_btn = QPushButton("Save Changes")
        save_btn.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #2E8B57;
                color: white;
                padding: 12px;
                border: none;
                border-radius: 8px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #228B22;
            }
            QPushButton:pressed {
                background-color: #006400;
            }
        """)
        
        def save_changes():
            # Validate current password
            if old_password.text() != self.users[current_email]['password']:
                QMessageBox.critical(dialog, "Error", "Current password is incorrect!")
                return
            
            # Get new values
            new_name_val = new_name.text().strip()
            new_email_val = new_email.text().strip()
            new_pass_val = new_password.text()
            confirm_pass_val = confirm_password.text()
            
            # Validate inputs
            if not new_name_val or not new_email_val:
                QMessageBox.warning(dialog, "Error", "Name and email cannot be empty!")
                return
            
            # Check if new email already exists (if changed)
            if new_email_val != current_email and new_email_val in self.users:
                QMessageBox.critical(dialog, "Error", "Email already registered!")
                return
            
            # Validate password if provided
            if new_pass_val:
                if new_pass_val != confirm_pass_val:
                    QMessageBox.critical(dialog, "Error", "New passwords do not match!")
                    return
                if len(new_pass_val) < 3:
                    QMessageBox.warning(dialog, "Error", "Password must be at least 3 characters!")
                    return
            
            # Update user data
            old_user_data = self.users[current_email].copy()
            
            # Remove old email entry if email changed
            if new_email_val != current_email:
                del self.users[current_email]
            
            # Create new entry
            self.users[new_email_val] = {
                'name': new_name_val,
                'password': new_pass_val if new_pass_val else old_user_data['password']
            }
            
            # Update current user
            self.current_user = new_name_val
            self.welcome_label.setText(f"Welcome, {self.current_user}!")
            
            # Save to file
            self.save_users_to_file()
            
            QMessageBox.information(dialog, "Success", "Profile updated successfully!")
            dialog.accept()
        
        save_btn.clicked.connect(save_changes)
        button_layout.addWidget(save_btn)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setFont(QFont("Arial", 14))
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #6C757D;
                color: white;
                padding: 12px;
                border: none;
                border-radius: 8px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #5A6268;
            }
        """)
        cancel_btn.clicked.connect(dialog.reject)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        layout.addStretch()
        
        dialog.exec()
        
    def login(self):
        email = self.login_email.text().strip()
        password = self.login_password.text()
        
        if not email or not password:
            QMessageBox.warning(self, "Error", "Please fill in all fields!")
            return
            
        if email in self.users and self.users[email]['password'] == password:
            self.current_user = self.users[email]['name']
            self.welcome_label.setText(f"Welcome, {self.current_user}!")
            QMessageBox.information(self, "Success", f"Welcome back, {self.current_user}!")
            self.login_email.clear()
            self.login_password.clear()
            self.stacked_widget.setCurrentIndex(2)  # Go to dashboard
        else:
            QMessageBox.critical(self, "Error", "Invalid email or password!")
            
    def signup(self):
        name = self.signup_name.text().strip()
        email = self.signup_email.text().strip()
        password = self.signup_password.text()
        confirm = self.signup_confirm.text()
        
        if not name or not email or not password or not confirm:
            QMessageBox.warning(self, "Error", "Please fill in all fields!")
            return
            
        if password != confirm:
            QMessageBox.critical(self, "Error", "Passwords do not match!")
            return
            
        if email in self.users:
            QMessageBox.critical(self, "Error", "Email already registered!")
            return
            
        # Store user data in dictionary
        self.users[email] = {
            'name': name,
            'password': password
        }
        
        # Save to file
        self.save_users_to_file()
        
        QMessageBox.information(self, "Success", "Account created successfully! You can now login.")
        
        # Clear fields and switch to login page
        self.signup_name.clear()
        self.signup_email.clear()
        self.signup_password.clear()
        self.signup_confirm.clear()
        self.stacked_widget.setCurrentIndex(0)
        
    def logout(self):
        self.current_user = None
        self.results_text.clear()
        self.stacked_widget.setCurrentIndex(0)
        
    def show_save_dialog(self, data, function_name):
        """Show save dialog and handle saving to Excel/JSON"""
        choice, ok = QInputDialog.getItem(self, "Save Data", "Save to Excel, JSON, or both?", 
                                        ["Excel", "JSON", "Both"], 0, False)
        if not ok:
            return
            
        success_messages = []
        error_messages = []
        
        if choice in ["Excel", "Both"]:
            try:
                # Call the appropriate Excel function based on function_name
                if function_name == "organize_readings":
                    Organize_readings_per_sensor_save_to_excel(data)
                elif function_name == "extreme_sensors":
                    Extreme_sensors_save_to_excel(data)
                elif function_name == "compare_readings":
                    Compare_readings_save_to_excel(data)
                elif function_name == "summarize_data":
                    Summarize_data_save_to_excel(data)
                elif function_name == "group_data":
                    Group_data_by_sensor_save_to_excel(data)
                elif function_name == "unique_sensor":
                    unique_sensor_set_save_to_excel(data)
                elif function_name == "max_min_values":
                    max_and_min_values_save_to_excel(data)
                elif function_name == "timestamps":
                    timestamps_save_to_excel(data)
                elif function_name == "most_recent":
                    most_recent_reading_save_to_excel(data)
                success_messages.append("Excel file saved successfully!")
            except Exception as e:
                error_messages.append(f"Failed to save to Excel file: {e}")
                
        if choice in ["JSON", "Both"]:
            try:
                json_filename = f"{function_name}.json"
                write_to_json(data, json_filename)
                success_messages.append("JSON file saved successfully!")
            except Exception as e:
                error_messages.append(f"Failed to save to JSON file: {e}")
        
        # Show results
        if success_messages:
            QMessageBox.information(self, "Success", "\n".join(success_messages))
        if error_messages:
            QMessageBox.critical(self, "Error", "\n".join(error_messages))
        
    # UI functions that call your existing functions
    def organize_readings_ui(self):
        result = "=== Organize Readings per Sensor ===\n\n"
        result += "Data before organizing:\n"
        for sensor in sensor_data:
            result += f"{sensor}\n"
        result += "\nData after organizing:\n"
        organized_data = organize_readings(sensor_data)
        for sensor_id, readings in organized_data.items():
            result += f"\nSensor {sensor_id}:\n"
            for reading in readings:
                result += f"  {reading}\n"
        self.results_text.setText(result)
        
        # Show save dialog
        self.show_save_dialog(organized_data, "organize_readings")
        
    def extreme_sensors_ui(self):
        result = "=== Identify Extreme Sensors ===\n\n"
        organized_data = organize_readings(sensor_data)
        data_extreme = Extreme_sensors(organized_data)
        for line in data_extreme:
            result += line + "\n"
        self.results_text.setText(result)
        
        self.show_save_dialog(data_extreme, "extreme_sensors")
        
    def compare_readings_ui(self):
        result = "=== Compare Readings ===\n\n"
        organized_data = organize_readings(sensor_data)
        data_compare = Compare_readings(organized_data)
        for line in data_compare:
            result += line + "\n"
        self.results_text.setText(result)
        
        self.show_save_dialog(data_compare, "compare_readings")
        
    def summarize_data_ui(self):
        result = "=== Summarize Data ===\n\n"
        choice, ok = QInputDialog.getItem(self, "Data Type", "Which data do you want to show?", 
                                        ["Temperature", "Stress", "Displacement", "All"], 0, False)
        if not ok:
            return
            
        organized_data = organize_readings(sensor_data)
        # Simulate user input for your function
        if choice == "Temperature":
            choice_num = "1"
        elif choice == "Stress":
            choice_num = "2"
        elif choice == "Displacement":
            choice_num = "3"
        else:
            choice_num = "4"
            
        # We need to modify the Summarize_data function to accept choice as parameter
        # For now, we'll use a workaround
        data_summarize = Summarize_data(organized_data, choice_num)
        for line in data_summarize:
            result += line + "\n"
        self.results_text.setText(result)
        
        self.show_save_dialog(data_summarize, "summarize_data")
        
    def group_data_ui(self):
        result = "=== Group Data by Sensor ===\n\n"
        result += "Before grouping:\n"
        for sensor in sensor_data:
            result += f"{sensor}\n"
            
        data_grouped = Group_data_by_sensor(sensor_data)
        result += "\nAfter grouping:\n"
        for sensor_id, readings in data_grouped.items():
            result += f"\nSensor {sensor_id}:\n"
            for reading in readings:
                result += f"  Timestamp: {reading[0]}, Temp: {reading[1]}℃, Stress: {reading[2]}, Displacement: {reading[3]}\n"
        self.results_text.setText(result)
        
        self.show_save_dialog(data_grouped, "group_data")
        
    def unique_sensor_ui(self):
        result = "=== Find High Stress Sensors (>13.0) ===\n\n"
        data_unique = unique_sensor_set(sensor_data)
        for line in data_unique:
            result += line + "\n"
        self.results_text.setText(result)
        
        self.show_save_dialog(data_unique, "unique_sensor")
        
    def calculate_statistics_ui(self):
        # Same as summarize_data_ui
        self.summarize_data_ui()
        
    def max_min_values_ui(self):
        result = "=== Max/Min Values ===\n\n"
        organized_data = organize_readings(sensor_data)
        data_max_and_min_values = max_and_min_values(organized_data)
        for line in data_max_and_min_values:
            result += line + "\n"
        self.results_text.setText(result)
        
        self.show_save_dialog(data_max_and_min_values, "max_min_values")
        
    def timestamps_ui(self):
        result = "=== Extract Timestamps ===\n\n"
        choice, ok = QInputDialog.getItem(self, "Timestamp Type", "You want all timestamps or without duplicates?", 
                                        ["All timestamps", "Timestamps without duplicates"], 0, False)
        if not ok:
            return
            
        organized_data = organize_readings(sensor_data)
        # Simulate user input for your function
        if choice == "All timestamps":
            choice_num = "1"
        else:
            choice_num = "2"
            
        data_timestamps = timestapms_extracted(organized_data, choice_num)
        if choice_num == "1":
            result += "All timestamps (sorted):\n"
        else:
            result += "Timestamps without duplicates (sorted):\n"
            
        for timestamp in data_timestamps:
            result += f"  {timestamp}\n"
        self.results_text.setText(result)
        
        self.show_save_dialog(data_timestamps, "timestamps")
        
    def most_recent_ui(self):
        result = "=== Most Recent Readings ===\n\n"
        organized_data = organize_readings(sensor_data)
        data_most_recent_reading = most_recent_reading(organized_data)
        result += "Most recent readings for each sensor:\n"
        for reading in data_most_recent_reading:
            result += f"{reading}\n"
        self.results_text.setText(result)
        
        self.show_save_dialog(data_most_recent_reading, "most_recent")

def main_gui():
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())

##############################################################################################################################
######################################################App as Console#############################################################
reading_sensor = organize_readings(sensor_data)  # Organize the data
#Main function to call all the functions
def console():
    reading_sensor = organize_readings(sensor_data)  # Organize the data
    print("Welcome to the sensor data analysis program!")
    print("Please choose an option:")
    print("1. Organize readings per sensor")
    print("2. Identify unique sensors with extreme values")
    print("3. Compare readings from different time intervals")
    print("4. Summarize the data by calculating max, min, and average readings per sensor")
    print("5. Group data by sensor using a dictionary (sensor_id as key, list of tuples as value)")
    print("6. Use sets to find unique sensor IDs that recorded stress > 13.0")
    print("7. Calculate statistics per sensor")
    print("8. Max, min, and average temperature and max displacement")
    print("9. Extract all timestamps into a list and sort them")
    print("10. Create a tuple of the most recent reading for each sensor")
    print("11. Exit")
    choice = input("Enter your choice (1-11): ")
    if choice == "1":
        show_data_before_and_after(sensor_data, reading_sensor)
        print("want to save the data to excel file or json file or both? write first letter of the option")
        save_data=input("Enter your choice (e/j/b): ")
        if save_data == "e":
            Organize_readings_per_sensor_save_to_excel(reading_sensor)
            print("Data saved to excel file.")
        elif save_data == "j":
            write_to_json(reading_sensor,"Organize-readings-per-sensor.json")
            print("Data saved to json file.")
        elif save_data == "b":
            Organize_readings_per_sensor_save_to_excel(reading_sensor)
            print("Data saved to excel file.")
            write_to_json(reading_sensor,"Organize-readings-per-sensor.json")
            print("Data saved to json file.")
        else:
            print("Data not saved to excel file or json file.")
    elif choice == "2":
        data_extreme=Extreme_sensors(reading_sensor)
        print("want to save the data to excel file or json file or both? write first letter of the option")
        save_data=input("Enter your choice (e/j/b): ")
        if save_data == "e":
            Extreme_sensors_save_to_excel(data_extreme)
            print("Data saved to excel file.")
        elif save_data == "j":
            write_to_json(data_extreme,"Identify-unique-sensors-with-extreme-values.json")
            print("Data saved to json file.")
        elif save_data == "b":
            Extreme_sensors_save_to_excel(data_extreme)
            print("Data saved to excel file.")
            write_to_json(data_extreme,"Identify-unique-sensors-with-extreme-values.json")
            print("Data saved to json file.")
        else:
            print("Data not saved to excel file or json file.")
    elif choice == "3":
        data_compare=Compare_readings(reading_sensor)
        print("want to save the data to excel file or json file or both? write first letter of the option")
        save_data=input("Enter your choice (e/j/b): ")
        if save_data == "e":
            Compare_readings_save_to_excel(data_compare)
            print("Data saved to excel file.")
        elif save_data == "j":
            write_to_json(data_compare,"Compare-readings-from-different-time-intervals.json")
            print("Data saved to json file.")
        elif save_data == "b":
            Compare_readings_save_to_excel(data_compare)
            print("Data saved to excel file.")
            write_to_json(data_compare,"Compare-readings-from-different-time-intervals.json")
            print("Data saved to json file.")
        else:
            print("Data not saved to excel file or json file.")
    elif choice == "4":
        data_summarize=Summarize_data(reading_sensor)
        print("want to save the data to excel file or json file or both? write first letter of the option")
        save_data=input("Enter your choice (e/j/b): ")
        if save_data == "e":
            Summarize_data_save_to_excel(data_summarize)
            print("Data saved to excel file.")
        elif save_data == "j":
            write_to_json(data_summarize,"Summarize-the-data-by-calculating-max-min-and-average-readings-per-sensor.json")
            print("Data saved to json file.")
        elif save_data == "b":
            Summarize_data_save_to_excel(data_summarize)
            print("Data saved to excel file.")
            write_to_json(data_summarize,"Summarize-the-data-by-calculating-max-min-and-average-readings-per-sensor.json")
            print("Data saved to json file.")
        else:
            print("Data not saved to excel file or json file.")
    elif choice == "5":
        data_grouped=Group_data_by_sensor(sensor_data)
        print("want to save the data to excel file or json file or both? write first letter of the option")
        save_data=input("Enter your choice (e/j/b): ")
        if save_data == "e":
            Group_data_by_sensor_save_to_excel(data_grouped)
            print("Data saved to excel file.")
        elif save_data == "j":
            write_to_json(data_grouped,"Group-data-by-sensor-using-a-dictionary-sensor_id-as-key-list-of-tuples-as-value.json")
            print("Data saved to json file.")
        elif save_data == "b":
            Group_data_by_sensor_save_to_excel(data_grouped)
            print("Data saved to excel file.")
            write_to_json(data_grouped,"Group-data-by-sensor-using-a-dictionary-sensor_id-as-key-list-of-tuples-as-value.json")
            print("Data saved to json file.")
        else:
            print("Data not saved to excel file or json file.")
    elif choice == "6":
        data_unique=unique_sensor_set(sensor_data)
        print("want to save the data to excel file or json file or both? write first letter of the option")
        save_data=input("Enter your choice (e/j/b): ")
        if save_data == "e":
            unique_sensor_set_save_to_excel(data_unique)
            print("Data saved to excel file.")
        elif save_data == "j":
            write_to_json(data_unique,"Use-sets-to-find-unique-sensor-IDs-that-recorded-stress-13.0.json")
            print("Data saved to json file.")
        elif save_data == "b":
            unique_sensor_set_save_to_excel(data_unique)
            print("Data saved to excel file.")
            write_to_json(data_unique,"Use-sets-to-find-unique-sensor-IDs-that-recorded-stress-13.0.json")
            print("Data saved to json file.")
        else:
            print("Data not saved to excel file or json file.")
    elif choice == "7":
        data_summarize=Summarize_data(reading_sensor)
        print("want to save the data to excel file or json file or both? write first letter of the option")
        save_data=input("Enter your choice (e/j/b): ")
        if save_data == "e":
            Summarize_data_save_to_excel(data_summarize)
            print("Data saved to excel file.")
        elif save_data == "j":
            write_to_json(data_summarize,"Calculate-statistics-per-sensor.json")
            print("Data saved to json file.")
        elif save_data == "b":
            Summarize_data_save_to_excel(data_summarize)
            print("Data saved to excel file.")
            write_to_json(data_summarize,"Calculate-statistics-per-sensor.json")
            print("Data saved to json file.")
        else:
            print("Data not saved to excel file or json file.")
    elif choice == "8":
        data_max_and_min_values=max_and_min_values(reading_sensor)
        print("want to save the data to excel file or json file or both? write first letter of the option")
        save_data=input("Enter your choice (e/j/b): ")
        if save_data == "e":
            max_and_min_values_save_to_excel(data_max_and_min_values)
            print("Data saved to excel file.")
        elif save_data == "j":
            write_to_json(data_max_and_min_values,"Max-min-and-average-temperature-and-max-displacement.json")
            print("Data saved to json file.")
        elif save_data == "b":
            max_and_min_values_save_to_excel(data_max_and_min_values)
            print("Data saved to excel file.")
            write_to_json(data_max_and_min_values,"Max-min-and-average-temperature-and-max-displacement.json")
            print("Data saved to json file.")
        else:
            print("Data not saved to excel file or json file.")
    elif choice == "9":
        data_timestamps=timestapms_extracted(reading_sensor)
        print("want to save the data to excel file or json file or both? write first letter of the option")
        save_data=input("Enter your choice (e/j/b): ")
        if save_data == "e":
            timestamps_save_to_excel(data_timestamps)
            print("Data saved to excel file.")
        elif save_data == "j":
            write_to_json(data_timestamps,"Extract-all-timestamps-into-a-list-and-sort-them.json")
            print("Data saved to json file.")
        elif save_data == "b":
            timestamps_save_to_excel(data_timestamps)
            print("Data saved to excel file.")
            write_to_json(data_timestamps,"Extract-all-timestamps-into-a-list-and-sort-them.json")
            print("Data saved to json file.")
        else:
            print("Data not saved to excel file or json file.")
    elif choice == "10":
        data_most_recent_reading=most_recent_reading(reading_sensor)
        print("want to save the data to excel file or json file or both? write first letter of the option")
        save_data=input("Enter your choice (e/j/b): ")
        if save_data == "e":
            most_recent_reading_save_to_excel(data_most_recent_reading)
            print("Data saved to excel file.")
        elif save_data == "j":
            write_to_json(data_most_recent_reading,"Create-a-tuple-of-the-most-recent-reading-for-each-sensor.json")
            print("Data saved to json file.")
        elif save_data == "b":
            most_recent_reading_save_to_excel(data_most_recent_reading)
            print("Data saved to excel file.")
            write_to_json(data_most_recent_reading,"Create-a-tuple-of-the-most-recent-reading-for-each-sensor.json")
            print("Data saved to json file.")
        else:
            print("Data not saved to excel file or json file.")
    elif choice == "11":
        print("Exiting the program.")       
    else:
        print("Invalid choice. Please enter a number between 1 and 10.")



def main_console():
    while True:
        console()
        cont = input("Do you want to continue? (y/n): ").strip().lower()
        if cont != "y":
            print("Exiting the program.")
            break





########################################################App as Console end########################################################
######################################################### Main function ##############################################################


if __name__ == "__main__":
    Grduation_Project_console()
   #task_8_console()
   
   #task_7_console()
   # main_gui()  # Run the GUI application
   #main_console()  # Run the console application
    


##info that idea of function 4 same as idea for function 7