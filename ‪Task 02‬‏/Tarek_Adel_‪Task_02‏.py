# Library   
import numpy as np

# Classes


# Parent class
class LinearEquationSolver:
    """
    This class is used to solve linear equations.
    """
    def __init__(self, coefficients, constants):  # initialize the coefficients and constants
        self.__coefficients = coefficients
        self.__constants = constants
    
    def get_coefficients(self):  # get the coefficients
        return self.__coefficients

    def get_constants(self):  # get the constants
        return self.__constants
    
    def set_coefficients(self, coefficients):  # set the coefficients
        self.__coefficients = coefficients

    def set_constants(self, constants):  # set the constants
        self.__constants = constants

    @classmethod
    def from_user_input(cls):  # get the coefficients and constants from the user
        print("Enter the coefficients of the linear equation:")
        coefficients = []
        constants = []
        for i in range(3):
            row=[]
            row.append(float(input(f"Enter the coefficient of x{i+1} equation: ")))
            row.append(float(input(f"Enter the coefficient of y{i+1} equation: ")))
            row.append(float(input(f"Enter the coefficient of z{i+1} equation: ")))
            coefficients.append(row)
            constants.append(float(input(f"Enter the constant of {i+1} equation: ")))
        return cls(coefficients, constants)
    
    @staticmethod
    def core_solve_quation(coefficients, constants):  # solve the equations
        elements=np.array(coefficients)
        const=np.array(constants)
        solve=np.linalg.solve(elements, const)
        return solve
    

# Child class
class ThreeVariableEquationSolver(LinearEquationSolver):
    """
    This class is used to solve three variable linear equations.
    """
    def display_equations(self):  # display the equations
        for i in range(3):
            print(f"{self.get_coefficients()[i][0]}x + {self.get_coefficients()[i][1]}y + {self.get_coefficients()[i][2]}z = {self.get_constants()[i]}")
            print("--------------------------------")
    
    def show_solve_equation(self):  # show the solution of the equations
        print("the value of x is: ", self.core_solve_quation(self.get_coefficients(), self.get_constants())[0])
        print("the value of y is: ", self.core_solve_quation(self.get_coefficients(), self.get_constants())[1])
        print("the value of z is: ", self.core_solve_quation(self.get_coefficients(), self.get_constants())[2])







# main program

person1=ThreeVariableEquationSolver.from_user_input()
person1.display_equations()
person1.show_solve_equation()

