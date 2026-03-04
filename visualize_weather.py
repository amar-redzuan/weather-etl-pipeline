import matplotlib.pyplot as plt
import json
from datetime import datetime

dates = []
temps = []

with open("weather_data.json", "r") as f:
    for line in f:
        record = json.loads(line)

        date = datetime.fromisoformat(record["timestamp"])
        temp = record["temperature"]

        dates.append(date)
        temps.append(temp)

plt.plot(dates, temps)
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Kuala Lumpur Temperature Over Time")
plt.show()