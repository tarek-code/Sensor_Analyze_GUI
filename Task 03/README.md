# Task 03: Electrical Circuit Analysis with Object-Oriented Programming

## 📋 Overview

Task 03 is an educational electrical circuit analysis application that demonstrates Object-Oriented Programming (OOP) principles in Python. The application allows users to build and analyze both series and parallel DC circuits, calculating voltage, current, and resistance values using fundamental electrical engineering principles.

## 🎯 Features

### Core Functionality
- **Circuit Construction**: Build custom electrical circuits with resistors and voltage sources
- **Circuit Types**: Support for both series and parallel circuit configurations
- **Automatic Calculations**: Real-time computation of electrical parameters
- **Interactive Interface**: User-friendly console-based circuit builder
- **Component Management**: Add and remove electrical components dynamically

### Electrical Analysis Capabilities
- **Voltage Analysis**: Calculate voltage drops across resistors
- **Current Analysis**: Determine total and branch currents
- **Resistance Calculations**: Compute equivalent resistance for series/parallel circuits
- **Power Calculations**: Basic electrical power analysis
- **Circuit Validation**: Automatic circuit integrity checks

### OOP Concepts Demonstrated
- **Inheritance**: Hierarchical class structure for circuit types
- **Encapsulation**: Private attributes with getter/setter methods
- **Polymorphism**: Different behavior for different circuit types
- **Composition**: Circuits composed of multiple components

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- No external packages required (uses only built-in Python libraries)

### Running the Application
```bash
python Tarek_Adel_Task_03.py
```

## 🔌 Sample Circuit Examples

### Series Circuit Example
```
Voltage Source: 12V
Resistor 1: 10Ω
Resistor 2: 20Ω
Resistor 3: 30Ω

Results:
- Total Resistance: 60Ω
- Total Current: 0.2A
- Voltage Drop R1: 2V
- Voltage Drop R2: 4V
- Voltage Drop R3: 6V
```

### Parallel Circuit Example
```
Voltage Source: 24V
Resistor 1: 12Ω
Resistor 2: 6Ω
Resistor 3: 4Ω

Results:
- Total Resistance: 2Ω
- Total Current: 12A
- Branch Current R1: 2A
- Branch Current R2: 4A
- Branch Current R3: 6A
```

## 🏗️ Code Architecture

### Class Hierarchy

```
Component (Base Class)
├── Resistor
└── VoltageSource

Circuit (Base Class)
└── DCCircuit
    ├── SeriesCircuit
    └── ParallelCircuit

DisplayInfo (Utility Class)
```

### Main Classes

#### 1. `Component` (Base Class)
- **Purpose**: Abstract base class for all electrical components
- **Attributes**: 
  - `__name`: Private component identifier
  - `__value`: Private component value (resistance/voltage)
- **Methods**: Getter and setter methods for encapsulation
- **Use Case**: Foundation for all electrical components

#### 2. `Resistor` (Inherits from Component)
- **Purpose**: Represents electrical resistors in circuits
- **Methods**: `show_info()` - displays resistor information
- **Use Case**: Current-limiting components in circuits

#### 3. `VoltageSource` (Inherits from Component)
- **Purpose**: Represents power sources in circuits
- **Methods**: `show_info()` - displays voltage source information
- **Use Case**: Power supply for circuit operation

#### 4. `Circuit` (Base Class)
- **Purpose**: Abstract base class for circuit containers
- **Attributes**: `components` - list of circuit components
- **Methods**: 
  - `add_component()` - adds components to circuit
  - `remove_component()` - removes components from circuit
- **Use Case**: Component management and organization

#### 5. `DCCircuit` (Inherits from Circuit)
- **Purpose**: Base class for DC circuit analysis
- **Methods**:
  - `get_voltage()` - retrieves circuit voltage
  - `calculate_total_current()` - computes total current
  - `calculate_voltage_drops()` - calculates voltage across resistors
- **Use Case**: Common DC circuit functionality

#### 6. `SeriesCircuit` (Inherits from DCCircuit)
- **Purpose**: Analyzes series circuit configurations
- **Methods**: `calculate_total_resistance()` - sums all resistances
- **Formula**: R_total = R₁ + R₂ + R₃ + ...
- **Use Case**: Components connected end-to-end

#### 7. `ParallelCircuit` (Inherits from DCCircuit)
- **Purpose**: Analyzes parallel circuit configurations
- **Methods**: 
  - `calculate_total_resistance()` - computes equivalent resistance
  - `calculate_branch_currents()` - calculates current in each branch
- **Formula**: 1/R_total = 1/R₁ + 1/R₂ + 1/R₃ + ...
- **Use Case**: Components connected across same voltage

#### 8. `DisplayInfo` (Utility Class)
- **Purpose**: Provides formatted output for circuit analysis
- **Methods**: `display_info()` - comprehensive circuit information display
- **Features**: Automatic detection of circuit type and appropriate calculations

## 🔧 Usage

### Running the Application

#### Step 1: Choose Circuit Type
```
Choose the circuit type:
1. Series Circuit
2. Parallel Circuit
Enter your choice (1 or 2):
```

#### Step 2: Add Components
```
What would you like to add?
1. Resistor
2. Voltage Source
3. Done, calculate results
Enter your choice:
```

#### Step 3: Component Configuration
```
For Resistors:
- Enter resistor name: R1
- Enter resistance value (Ohms): 10

For Voltage Sources:
- Enter voltage source name: V1
- Enter voltage value (Volts): 12
```

#### Step 4: View Results
The application automatically calculates and displays:
- Component information
- Total voltage and resistance
- Total current
- Voltage drops (series) or branch currents (parallel)

### Example Session
```python
# User builds a series circuit
Choose the circuit type: 1 (Series)
Add Resistor: R1 = 10Ω
Add Resistor: R2 = 20Ω
Add Voltage Source: V1 = 12V
Done, calculate results

# Output:
--- Circuit Info ---
The name of the resistor is = R1
The value of the resistor is = 10.0
The name of the resistor is = R2
The value of the resistor is = 20.0
The name of the voltage source is = V1
The value of the voltage source is = 12.0

Total Voltage: 12.0 V
Total Resistance: 30.0 Ohms
Total Current: 0.4 A

--- Voltage on Each Resistor ---
R1: 4.0 V
R2: 8.0 V
```

## ⚡ Electrical Engineering Concepts

### Ohm's Law
- **Formula**: V = I × R
- **Where**: V = Voltage, I = Current, R = Resistance
- **Application**: Used throughout the application for calculations

### Series Circuit Rules
- **Current**: Same current flows through all components
- **Voltage**: Total voltage equals sum of voltage drops
- **Resistance**: Total resistance equals sum of individual resistances

### Parallel Circuit Rules
- **Voltage**: Same voltage across all components
- **Current**: Total current equals sum of branch currents
- **Resistance**: Reciprocal of total resistance equals sum of reciprocals

### Power Calculations
- **Formula**: P = V × I = I² × R = V² / R
- **Units**: Watts (W)
- **Application**: Can be extended for power analysis

## 🔍 Code Quality Features

### Object-Oriented Design
- **Encapsulation**: Private attributes with controlled access
- **Inheritance**: Logical class hierarchy for circuit types
- **Polymorphism**: Different behavior for different circuit configurations
- **Composition**: Circuits composed of multiple components

### Error Handling
- **Input Validation**: Checks for valid numeric inputs
- **Circuit Validation**: Ensures proper circuit configuration
- **Division by Zero**: Handles short circuit conditions

### Code Documentation
- **Clear Class Names**: Descriptive naming conventions
- **Logical Structure**: Organized class hierarchy
- **Consistent Methods**: Standardized interface across classes

## 🧪 Testing and Validation

### Built-in Validation
- **Component Validation**: Ensures valid component values
- **Circuit Integrity**: Checks for proper circuit configuration
- **Mathematical Accuracy**: Validates electrical calculations

### Test Cases
```python
# Test series circuit
series = SeriesCircuit()
series.add_component(VoltageSource("V1", 12))
series.add_component(Resistor("R1", 10))
series.add_component(Resistor("R2", 20))

# Expected results:
# Total Resistance: 30Ω
# Total Current: 0.4A
# Voltage Drop R1: 4V
# Voltage Drop R2: 8V
```

## 🚨 Troubleshooting

### Common Issues

#### 1. Input Errors
```
# Ensure numeric inputs for component values
Enter resistance value (Ohms): 10.5  # Valid
Enter resistance value (Ohms): abc    # Invalid
```

#### 2. Circuit Configuration
- **Series Circuit**: Components must be connected end-to-end
- **Parallel Circuit**: Components must be connected across same voltage
- **Mixed Circuits**: Not supported in current version

#### 3. Mathematical Errors
- **Zero Resistance**: Handled automatically (short circuit)
- **Negative Values**: Not validated (assumes positive values)
- **Extreme Values**: No range checking implemented

### Debug Mode
Add debug prints to understand circuit behavior:
```python
# Add this to any method for debugging
print(f"Debug: Processing component {component.get_name()} with value {component.get_value()}")
```

## 🔄 Extending the Code

### Adding New Component Types
```python
class Capacitor(Component):
    def __init__(self, name, value):
        super().__init__(name, value)
        self.__capacitance = value
    
    def show_info(self):
        print(f"The capacitance is = {self.__capacitance} F")
    
    def calculate_reactance(self, frequency):
        return 1 / (2 * 3.14159 * frequency * self.__capacitance)
```

### Adding New Circuit Types
```python
class MixedCircuit(DCCircuit):
    def calculate_total_resistance(self):
        # Complex circuit analysis logic
        # Combine series and parallel calculations
        pass
```

### Adding AC Circuit Support
```python
class ACCircuit(Circuit):
    def __init__(self, frequency):
        super().__init__()
        self.frequency = frequency
    
    def calculate_impedance(self):
        # AC impedance calculations
        pass
```

### Adding Power Analysis
```python
def calculate_power_dissipation(self):
    current = self.calculate_total_current()
    for component in self.components:
        if isinstance(component, Resistor):
            power = current ** 2 * component.get_value()
            print(f"{component.get_name()}: {power:.3f} W")
```

## 📚 Learning Resources

### OOP Concepts Used
- **Classes and Objects**: Component and Circuit classes
- **Inheritance**: Circuit type hierarchy
- **Encapsulation**: Private attributes with methods
- **Polymorphism**: Different circuit behaviors
- **Composition**: Circuits containing components

### Electrical Engineering Concepts
- **Circuit Analysis**: Kirchhoff's laws and Ohm's law
- **Series Circuits**: Current flow and voltage division
- **Parallel Circuits**: Voltage sharing and current division
- **Power Calculations**: Electrical power relationships

### Python Programming Concepts
- **Class Definition**: `class` keyword and methods
- **Constructor**: `__init__` method
- **Private Attributes**: Double underscore naming
- **Method Overriding**: Custom behavior in subclasses
- **Type Checking**: `isinstance()` function usage

### Related Topics
- Electrical circuit theory
- Object-oriented programming
- Python class design
- Engineering calculations
- User interface design

## 🤝 Contributing

### Code Style Guidelines
- Follow PEP 8 Python style guide
- Use descriptive class and method names
- Add docstrings for all classes and methods
- Include error handling for edge cases
- Maintain consistent formatting

### Testing New Features
1. Test with simple circuits first
2. Validate electrical calculations
3. Check error conditions
4. Update documentation
5. Test edge cases (zero resistance, etc.)

### Suggested Improvements
- **GUI Interface**: Add graphical circuit builder
- **Component Library**: Pre-defined common components
- **Circuit Visualization**: Visual representation of circuits
- **Advanced Analysis**: AC circuits, frequency response
- **File I/O**: Save and load circuit configurations

## 📄 License

This project is part of the Kaitech company training program. Please respect the company's intellectual property rights.

## 👨‍💻 Author Information

- **Name**: Tarek Adel Ali
- **Company**: Kaitech
- **Date**: 2025-07-21
- **Email**: tarekadel314@gmail.com
- **Task**: 03 - Electrical Circuit Analysis with OOP

## 🔗 Related Projects

- **Task 7**: Pandas-based sensor data analysis
- **Task 8**: NumPy-based sensor data analysis
- **Task 6**: Basic sensor data organization

## 📞 Support

For questions or issues:
1. Check the troubleshooting section above
2. Review the code comments and class structure
3. Test with simple circuit examples
4. Contact the author at tarekadel314@gmail.com

---

**Happy Circuit Building! ⚡**

*This README provides comprehensive documentation for understanding, using, and extending the Task 03 electrical circuit analysis application with Object-Oriented Programming principles.*
