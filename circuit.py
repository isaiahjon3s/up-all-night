class Circuit:
    def __init__(self, resistance, voltage):
        self.resistance = resistance
        self.voltage = voltage

    def calculate_current(self):
        return self.voltage / self.resistance

    def calculate_power(self):
        return self.voltage * self.calculate_current()

    def calculate_resistance(self):
        return self.voltage / self.calculate_current()

    def calculate_voltage(self):
        return self.calculate_current() * self.resistance

def main():
    circuit = Circuit(10, 100)
    print(f"Current: {circuit.calculate_current()}")
    print(f"Power: {circuit.calculate_power()}")
    print(f"Resistance: {circuit.calculate_resistance()}")
    print(f"Voltage: {circuit.calculate_voltage()}")

if __name__ == "__main__":
    main()
