from setup_db import create_db
from queries import get_summary, get_high_sales
from analysis import export_csv

create_db()

avg, max_val, min_val = get_summary()
print("Average:", avg)
print("Max:", max_val)
print("Min:", min_val)

print("\nHigh Sales Days:")
for row in get_high_sales():
    print(row)

export_csv()

print("\nCSV report generated!")
