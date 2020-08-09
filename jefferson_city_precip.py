import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'precip_data_2019.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, precip = [], []
    for row in reader:
        #try:
            current_date = datetime.strptime(row[2], '%Y-%m')
            p = int(float(row[4]))
        #except ValueError:
            #print(current_date, "missing data")
        #else:
            precip.append(p)
            dates.append(current_date)

    print(precip)
    print(dates)

# Plot the data.
fig = plt.figure(figsize=(15, 7))
plt.plot(dates, precip, c='blue')

# Format plot.
title = "Precipitation Jefferson City, 2019"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
#fig.autofmt_xdate()
plt.ylabel("Precipitation in Inches", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=8)

plt.show()

for index, column_header in enumerate(header_row):
    print(index, column_header)
