import json, requests
import csv
from datetime import datetime
from matplotlib import pyplot as plt


#1
filename = 'Final project/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    dates, precips = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        precip = float(row[3])
        precips.append(precip)

plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, precips, c='purple')

plt.title("Sitka Daily Precipitation - 2018", style='italic')
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation (in.)", fontsize=16)

plt.show()

#2
url ="http://www.omdbapi.com/?t=Python&apikey=324034ab"

response = requests.get(url)

python = json.loads(response.text)

print(f"{python['Title']} -- Released on: {python['Released']} -- Movie length: {python['Runtime']}" )
print(f"Written By: {python['Writer']} ")
print("")

#3

filename = 'Final project/nyc_temps.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='cyan')

plt.title("Daily High and Low Temperatures - 2021", fontsize=24, y=1.05)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.legend(["High","Low"], loc = "upper left")
plt.show()

print("complete")
