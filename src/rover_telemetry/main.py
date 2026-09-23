import random
import time

battery_level = 100
temperature = 25.0
speed = 0.0
position_x = 0
position_y = 0

print(f"Battery level: {battery_level}")
print(f"Temperature: {temperature}")
print(f"Speed: {speed}")
print(f"X position: {position_x}")
print(f"Y position: {position_y}")

while(battery_level > 0 and temperature < 100):
    speed = speed + random.randint(1,6)
    position_x = position_x + speed
    battery_level = battery_level - 1
    temperature = temperature + random.randint(1,10)
    time.sleep(1)
    if speed >= 30:
        print("UWAGA! Przekroczono prędkość 30km/h")
    print(f"Speed: {speed}")

    print(f"X position: {position_x}")

    if battery_level <= 0:
        print("Bateria rozładowana.")
        raise SystemExit
    elif battery_level <= 20:
        print("UWAGA! Niski poziom baterii.")
    print(f"Battery level: {battery_level}")

    if temperature >= 100:
        print("Temperatura wzrosła do stanu krytycznego. Zatrzymanie łazika.")
        raise SystemExit
    elif temperature >= 80:
        print("UWAGA! Wysoka temperatura.")
    print(f"Temperature: {temperature}")