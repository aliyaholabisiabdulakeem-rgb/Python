speed = float(input("Enter speed in m/s: "))
acceleration = float(input("Enter acceleration in m/s*2: "))

runway_length = (speed*speed) / (2*acceleration)

runway_length = round(runway_length, 3)
print("Runway length is", runway_length)

