temperature_readings = [25, 28, 21, 24, 27]

temperature_readings.sort()

averageTemp = sum(num for num in temperature_readings)
averageTemp /= len(temperature_readings)

print(f"Average Temperature: {averageTemp}")
print(f"Highest Temperature: {temperature_readings[len(temperature_readings) - 1]}")
print(f"Lowest Temperature: {temperature_readings[0]}")