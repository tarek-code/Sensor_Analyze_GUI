#Classes

class Component:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    def get_name(self):
        return self.__name

    def get_value(self):
        return self.__value
    
    def set_value(self, value):
        self.__value = value
    
    def set_name(self, name):
        self.__name = name



class Resistor(Component):
    def show_info(self):
        print("The name of the resistor is = ", self.get_name())
        print("The value of the resistor is = ", self.get_value())



class VoltageSource(Component):
    def show_info(self):
        print("The name of the voltage source is = ", self.get_name())
        print("The value of the voltage source is = ", self.get_value())





class Circuit():
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    

class DCCircuit(Circuit):
    def get_voltage(self):
        for component in self.components:
            if isinstance(component, VoltageSource):
                return component.get_value()
        return 0
    
    def calculate_total_current(self):
        total_resistance = self.calculate_total_resistance()
        voltage = self.get_voltage()
        if total_resistance == 0:
            return 0  # short circuit
        else:
            return voltage / total_resistance

    def calculate_voltage_drops(self):
        current = self.calculate_total_current()
        print("\n--- Voltage  on Each Resistor ---")
        for component in self.components:
            if isinstance(component, Resistor):
                voltage_drop = current * component.get_value()
                print(f"{component.get_name()}: {round(voltage_drop, 3)} V")


class SeriesCircuit(DCCircuit):
    def calculate_total_resistance(self):
        total = 0
        for component in self.components:
            if isinstance(component, Resistor):
                total += component.get_value()
        return total


class ParallelCircuit(DCCircuit):
    def calculate_total_resistance(self):
        inverse_total = 0
        for component in self.components:
            if isinstance(component, Resistor):
                inverse_total += 1 / component.get_value()
        return 1 / inverse_total if inverse_total != 0 else 0

    def calculate_branch_currents(self):
        voltage = self.get_voltage()
        print("\n--- Current in Each Branch ---")
        for component in self.components:
            if isinstance(component, Resistor):
                current = voltage / component.get_value()
                print(f"{component.get_name()}: {round(current, 3)} A")

class DisplayInfo:
    def display_info(self, user_object ):
        print("\n--- Circuit Info ---")
        for component in user_object.components:
            component.show_info()

        if isinstance(user_object, DCCircuit):
            print("\nTotal Voltage: ", user_object.get_voltage(), "V")
            print("Total Resistance: ", user_object.calculate_total_resistance(), "Ohms")
            print("Total Current: ", round(user_object.calculate_total_current(), 3), "A")

            if isinstance(user_object, SeriesCircuit):
                user_object.calculate_voltage_drops()

            if isinstance(user_object, ParallelCircuit):
                user_object.calculate_branch_currents()




# User Program

def build_user_circuit():
    print("Choose the circuit type:")
    print("1. Series Circuit")
    print("2. Parallel Circuit")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        user_circuit = SeriesCircuit()
    elif choice == '2':
        user_circuit = ParallelCircuit()
    else:
        print("Invalid choice.")
        return

    while True:
        print("\nWhat would you like to add?")
        print("1. Resistor")
        print("2. Voltage Source")
        print("3. Done, calculate results")
        action = input("Enter your choice: ")

        if action == '1':
            name = input("Enter resistor name: ")
            value = float(input("Enter resistance value (Ohms): "))
            user_circuit.add_component(Resistor(name, value))

        elif action == '2':
            name = input("Enter voltage source name: ")
            value = float(input("Enter voltage value (Volts): "))
            user_circuit.add_component(VoltageSource(name, value))

        elif action == '3':
            break

        else:
            print("Invalid input.")

    # Display results
    display = DisplayInfo()
    display.display_info(user_circuit)


# Main program
build_user_circuit()


    
            






