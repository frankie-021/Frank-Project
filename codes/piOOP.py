class Microwave:
    def __init__(self, brand: str, power_rating: str):
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False


    def turn_on(self):
        if self.turned_on:
            print(f"{self.brand} microwave is already ON.")
        else:
            self.turned_on = True
            print(f"{self.brand} microwave is now ON.")


    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f"{self.brand} microwave is now OFF.")
        else:
            print(f"{self.brand} microwave is already OFF.")


    def run(self, seconds: int):
        if self.turned_on:
            print(f"{self.brand} microwave is running for {seconds} seconds at {self.power_rating}.")
        else:
            print(f"Please turn ON the {self.brand} microwave before running it.")

njie = Microwave("Njie wave", "100W")

