# Task 02: Linear Equation Solver with Object-Oriented Programming

## 📋 Overview

Task 02 is an educational linear equation solver application that demonstrates Object-Oriented Programming (OOP) principles in Python, combined with NumPy for mathematical computations. The application solves systems of three linear equations with three variables (x, y, z) using matrix operations and provides an interactive interface for user input.

## 🎯 Features

### Core Functionality
- **Linear Equation Solving**: Solve systems of three linear equations with three variables
- **Matrix Operations**: Use NumPy's linear algebra functions for efficient computation
- **Interactive Input**: User-friendly console interface for coefficient and constant input
- **Equation Display**: Clear representation of the system of equations
- **Solution Display**: Accurate solutions for all variables

### Mathematical Capabilities
- **3x3 System**: Handles systems of three linear equations
- **Matrix Inversion**: Automatic matrix inversion and solution computation
- **Error Handling**: Built-in validation for solvable systems
- **Precision**: High-precision floating-point calculations

### OOP Concepts Demonstrated
- **Inheritance**: Child class extends parent class functionality
- **Encapsulation**: Private attributes with getter/setter methods
- **Class Methods**: Factory method for user input
- **Static Methods**: Utility functions for equation solving
- **Polymorphism**: Different behavior for different equation types

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- NumPy library

### Required Packages
```bash
pip install numpy
```

### Alternative: Install from requirements.txt
```bash
pip install -r requirements.txt
```

### Running the Application
```bash
python "Tarek_Adel_Task_02.py"
```

## 📊 Sample Equation Examples

### Example 1: Simple System
```
Equation 1: 2x + 3y + z = 9
Equation 2: x + 2y + 3z = 14
Equation 3: 3x + y + 2z = 11

Solution:
x = 1.0
y = 2.0
z = 3.0
```

### Example 2: Real-world Application
```
# Circuit Analysis Example
Equation 1: 2I₁ + 3I₂ + I₃ = 12    # Kirchhoff's Current Law
Equation 2: I₁ + 2I₂ + 3I₃ = 18    # Kirchhoff's Voltage Law
Equation 3: 3I₁ + I₂ + 2I₃ = 15    # Ohm's Law

Solution:
I₁ = 2.0 A
I₂ = 1.5 A
I₃ = 3.0 A
```

### Example 3: Physics Problem
```
# Force Equilibrium Example
Equation 1: F₁ + F₂ + F₃ = 100     # Total force
Equation 2: 2F₁ + F₂ + 3F₃ = 200   # Moment balance
Equation 3: F₁ + 3F₂ + F₃ = 150    # Component balance

Solution:
F₁ = 25.0 N
F₂ = 50.0 N
F₃ = 25.0 N
```

## 🏗️ Code Architecture

### Class Hierarchy

```
LinearEquationSolver (Parent Class)
└── ThreeVariableEquationSolver (Child Class)
```

### Main Classes

#### 1. `LinearEquationSolver` (Parent Class)
- **Purpose**: Base class for solving linear equations
- **Attributes**: 
  - `__coefficients`: Private 3x3 matrix of equation coefficients
  - `__constants`: Private vector of equation constants
- **Methods**: 
  - `get_coefficients()` / `set_coefficients()` - coefficient accessors
  - `get_constants()` / `set_constants()` - constant accessors
  - `from_user_input()` - class method for user input
  - `core_solve_quation()` - static method for equation solving
- **Use Case**: Foundation for linear equation solving

#### 2. `ThreeVariableEquationSolver` (Child Class)
- **Purpose**: Specialized solver for three-variable systems
- **Inheritance**: Extends `LinearEquationSolver`
- **Methods**: 
  - `display_equations()` - shows the system of equations
  - `show_solve_equation()` - displays the solution
- **Use Case**: Solving 3x3 linear equation systems

## 🔧 Usage

### Running the Application

#### Step 1: Launch the Program
```bash
python "Tarek_Adel_Task_02.py"
```

#### Step 2: Input Coefficients
```
Enter the coefficients of the linear equation:
Enter the coefficient of x1 equation: 2
Enter the coefficient of y1 equation: 3
Enter the coefficient of z1 equation: 1
Enter the constant of 1 equation: 9

Enter the coefficient of x2 equation: 1
Enter the coefficient of y2 equation: 2
Enter the coefficient of z2 equation: 3
Enter the constant of 2 equation: 14

Enter the coefficient of x3 equation: 3
Enter the coefficient of y3 equation: 1
Enter the coefficient of z3 equation: 2
Enter the constant of 3 equation: 11
```

#### Step 3: View Results
```
2.0x + 3.0y + 1.0z = 9.0
--------------------------------
1.0x + 2.0y + 3.0z = 14.0
--------------------------------
3.0x + 1.0y + 2.0z = 11.0
--------------------------------

the value of x is: 1.0
the value of y is: 2.0
the value of z is: 3.0
```

### Input Format Requirements

#### Coefficient Matrix (3x3)
```
| a₁₁  a₁₂  a₁₃ |
| a₂₁  a₂₂  a₂₃ |
| a₃₁  a₃₂  a₃₃ |
```

#### Constants Vector (3x1)
```
| b₁ |
| b₂ |
| b₃ |
```

#### System Representation
```
a₁₁x + a₁₂y + a₁₃z = b₁
a₂₁x + a₂₂y + a₂₃z = b₂
a₃₁x + a₃₂y + a₃₃z = b₃
```

## 🧮 Mathematical Concepts

### Linear Algebra
- **Matrix Operations**: Coefficient matrix manipulation
- **Vector Operations**: Constants vector processing
- **System Solving**: Ax = b equation solving

### NumPy Implementation
- **Array Creation**: `np.array()` for matrix representation
- **Linear Algebra**: `np.linalg.solve()` for solution computation
- **Data Types**: Automatic floating-point precision

### Solution Method
- **Gaussian Elimination**: NumPy's optimized algorithm
- **Matrix Inversion**: Automatic handling of singular matrices
- **Numerical Stability**: Built-in error checking

## 🔍 Code Quality Features

### Object-Oriented Design
- **Encapsulation**: Private attributes with controlled access
- **Inheritance**: Logical class hierarchy for equation types
- **Class Methods**: Factory method for object creation
- **Static Methods**: Utility functions independent of instance state

### Error Handling
- **Input Validation**: Ensures numeric input values
- **Matrix Validation**: Checks for solvable systems
- **Exception Handling**: Graceful handling of mathematical errors

### Code Documentation
- **Docstrings**: Clear class and method descriptions
- **Comments**: Inline explanations for complex operations
- **Naming Conventions**: Descriptive variable and method names

## 🧪 Testing and Validation

### Built-in Validation
- **Input Type Checking**: Ensures float inputs
- **Matrix Dimensions**: Validates 3x3 coefficient matrix
- **Solution Verification**: Confirms mathematical accuracy

### Test Cases
```python
# Test case 1: Simple system
coefficients = [[2, 3, 1], [1, 2, 3], [3, 1, 2]]
constants = [9, 14, 11]
expected_solution = [1.0, 2.0, 3.0]

# Test case 2: Identity matrix
coefficients = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
constants = [5, 10, 15]
expected_solution = [5.0, 10.0, 15.0]
```

### Validation Methods
```python
# Verify solution by substitution
def verify_solution(coefficients, constants, solution):
    for i in range(3):
        result = sum(coefficients[i][j] * solution[j] for j in range(3))
        if abs(result - constants[i]) > 1e-10:
            return False
    return True
```

## 🚨 Troubleshooting

### Common Issues

#### 1. Input Errors
```
# Ensure numeric inputs
Enter the coefficient of x1 equation: 2.5    # Valid
Enter the coefficient of x1 equation: abc   # Invalid
```

#### 2. Mathematical Errors
- **Singular Matrix**: System has no unique solution
- **Inconsistent System**: Equations are contradictory
- **Underdetermined System**: Infinite solutions exist

#### 3. NumPy Import Issues
```bash
# If you get NumPy import errors:
pip install numpy

# Verify installation:
python -c "import numpy; print(numpy.__version__)"
```

### Debug Mode
Add debug prints to understand equation solving:
```python
# Add this to any method for debugging
print(f"Debug: Coefficients matrix:\n{self.get_coefficients()}")
print(f"Debug: Constants vector: {self.get_constants()}")
```

## 🔄 Extending the Code

### Adding New Equation Types
```python
class TwoVariableEquationSolver(LinearEquationSolver):
    """
    Solver for two-variable linear equations.
    """
    def __init__(self, coefficients, constants):
        # Ensure 2x2 system
        if len(coefficients) != 2 or len(coefficients[0]) != 2:
            raise ValueError("Two-variable solver requires 2x2 system")
        super().__init__(coefficients, constants)
    
    def display_equations(self):
        for i in range(2):
            print(f"{self.get_coefficients()[i][0]}x + {self.get_coefficients()[i][1]}y = {self.get_constants()[i]}")
```

### Adding Solution Methods
```python
class IterativeEquationSolver(LinearEquationSolver):
    """
    Solver using iterative methods (Gauss-Seidel, Jacobi).
    """
    def solve_gauss_seidel(self, tolerance=1e-6, max_iterations=1000):
        # Implement Gauss-Seidel iteration
        pass
    
    def solve_jacobi(self, tolerance=1e-6, max_iterations=1000):
        # Implement Jacobi iteration
        pass
```

### Adding Matrix Analysis
```python
def analyze_matrix(self):
    """
    Analyze the coefficient matrix properties.
    """
    coeff_matrix = np.array(self.get_coefficients())
    
    # Calculate determinant
    det = np.linalg.det(coeff_matrix)
    print(f"Determinant: {det}")
    
    # Check condition number
    cond = np.linalg.cond(coeff_matrix)
    print(f"Condition number: {cond}")
    
    # Eigenvalues
    eigenvals = np.linalg.eigvals(coeff_matrix)
    print(f"Eigenvalues: {eigenvals}")
```

### Adding File I/O Support
```python
@classmethod
def from_file(cls, filename):
    """
    Load equation system from file.
    """
    coefficients = []
    constants = []
    
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                parts = line.strip().split(',')
                if len(parts) == 4:  # 3 coefficients + 1 constant
                    row = [float(x) for x in parts[:3]]
                    constants.append(float(parts[3]))
                    coefficients.append(row)
    
    return cls(coefficients, constants)

def save_to_file(self, filename):
    """
    Save equation system to file.
    """
    with open(filename, 'w') as file:
        for i in range(3):
            coeffs = self.get_coefficients()[i]
            const = self.get_constants()[i]
            file.write(f"{coeffs[0]},{coeffs[1]},{coeffs[2]},{const}\n")
```

## 📚 Learning Resources

### OOP Concepts Used
- **Classes and Objects**: Equation solver classes
- **Inheritance**: Parent-child class relationship
- **Encapsulation**: Private attributes with methods
- **Class Methods**: Factory method pattern
- **Static Methods**: Utility functions

### Mathematical Concepts
- **Linear Algebra**: Matrix operations and equation solving
- **Systems of Equations**: Multiple equation solutions
- **Numerical Methods**: Computational mathematics
- **Matrix Theory**: Determinants, eigenvalues, condition numbers

### Python Programming Concepts
- **NumPy Library**: Scientific computing
- **Class Definition**: `class` keyword and methods
- **Decorators**: `@classmethod` and `@staticmethod`
- **Private Attributes**: Double underscore naming
- **Method Overriding**: Custom behavior in subclasses

### Related Topics
- Linear algebra and matrix theory
- Numerical analysis and methods
- Object-oriented programming
- Scientific computing with Python
- Mathematical modeling

## 🤝 Contributing

### Code Style Guidelines
- Follow PEP 8 Python style guide
- Use descriptive class and method names
- Add docstrings for all classes and methods
- Include error handling for edge cases
- Maintain consistent formatting

### Testing New Features
1. Test with simple equation systems first
2. Validate mathematical accuracy
3. Check error conditions
4. Update documentation
5. Test edge cases (singular matrices, etc.)

### Suggested Improvements
- **GUI Interface**: Add graphical equation input
- **Equation Library**: Pre-defined common equation systems
- **Solution Visualization**: Graphical representation of solutions
- **Advanced Methods**: Iterative and numerical methods
- **File I/O**: Save and load equation systems

## 📄 License

This project is part of the Kaitech company training program. Please respect the company's intellectual property rights.

## 👨‍💻 Author Information

- **Name**: Tarek Adel Ali
- **Company**: Kaitech
- **Date**: 2025-07-21
- **Email**: tarekadel314@gmail.com
- **Task**: 02 - Linear Equation Solver with OOP

## 🔗 Related Projects

- **Task 3**: Electrical circuit analysis with OOP
- **Task 7**: Pandas-based sensor data analysis
- **Task 8**: NumPy-based sensor data analysis

## 📞 Support

For questions or issues:
1. Check the troubleshooting section above
2. Review the code comments and class structure
3. Test with simple equation examples
4. Contact the author at tarekadel314@gmail.com

---

**Happy Equation Solving! 🧮**

*This README provides comprehensive documentation for understanding, using, and extending the Task 02 linear equation solver application with Object-Oriented Programming principles and NumPy.*
