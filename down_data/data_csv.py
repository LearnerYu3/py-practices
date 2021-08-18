import csv
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime

filename = "./death_valley_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']

ax.set_title("2018 年 7 月每日最高温度", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("温度（F）", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
# for index, column_header in enumerate(header_row):
#     print(index, column_header)
