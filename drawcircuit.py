
def main()
    parser = argparse.ArgumentParser(description="Draw a circuit")
    parser.add_argument("circuit", type=str, help="The circuit to draw")
    args = parser.parse_args()

    print(args.circuit)

class Circuit:
    def __init__(self, circuit):
        self.circuit = circuit
    
    def basecircuit(self):
        self.circuit.append(self.circuit)

    def addresistor(self, resistor):
        self.circuit.append(resistor)

if __name__ == "__main__":
    main()