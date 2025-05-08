class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == "side_a":
            if value <= 0:
                raise ValueError("Side length must be greater than 0")
        elif key == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Angle must be between 0 and 180 degrees")
            object.__setattr__(self, "angle_b", 180 - value)
        object.__setattr__(self, key, value)

    def __str__(self):
        return f"Rhombus: side = {self.side_a}, angle_a = {self.angle_a}, angle_b = {self.angle_b}"


# Valid example
rhombus1 = Rhombus(10, 60)
print(rhombus1)

# Invalid angle (too big)
try:
    rhombus2 = Rhombus(8, 190)
except ValueError as e:
    print("Error:", e)

# Invalid side (negative)
try:
    rhombus3 = Rhombus(-5, 60)
except ValueError as e:
    print("Error:", e)
