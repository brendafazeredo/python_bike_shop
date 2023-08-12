class Bike:
    def __init__(self, color, model, year, price, wheel_size=21):
        self.color = color
        self.model = model
        self.year = year
        self.price = price
        self.wheel_size = wheel_size
        self.gear = 1

    def honk(self):
        print("Beep, beep!")

    def stop(self):
        print("Skreeech...")
        print("Bike stopped!")

    def run(self):
        print("Vrooom!")

    def change_gear(self, gear_number):
        print("Changing gear...")
        if gear_number > self.gear:
            print("Gear changed!")
            self.gear = gear_number
        else:
            print("Unable to change gear! Please try again.")

    def __str__(self):
        attributes = [f"{key}={value}" for key, value in self.__dict__.items()]
        return f"{self.__class__.__name__}: " + ", ".join(attributes)
    
b1 = Bike("Pink", "Caloi", 2014, "$100.00")
b1.honk()
b1.run()
b1.stop()
b1.change_gear(2)
print(b1)
print(b1.color, b1.year, b1.model, b1.price, b1.wheel_size)

b2 = Bike("Yellow", "Yellow", 2020, "$150.00")
b2.run()
b2.honk()
b2.stop()
print(b2)
print(b2.color, b2.year, b2.model, b2.price, b2.wheel_size)