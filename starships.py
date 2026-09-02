import nt


class starship:
    def __init__(self, base_weight, cargo_load, final_fuel):
        self.base_weight = base_weight
        self.cargo_load = cargo_load
        self.final_fuel = final_fuel

    def display_info(self):
        print("Base Weight:", self.base_weight)
        print("Cargo Load:", self.cargo_load)
        print("Final Fuel:", self.final_fuel())

    def final_fuel(self):
        return self.base_weight + self.cargo_load * 3 == self.calculate_total_weight
        self.final_fuel * 3 = self.final_fuel


starship = starship(base_weight, cargo_load, 0)
base_weight = (50000)
cargo_load = (1000)
final_fuel = (0)

base_weight.display_info()
cargo_load.display_info()
final_fuel.display_info()
