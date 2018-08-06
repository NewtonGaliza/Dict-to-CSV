import csv

csv_columns = ['Tweet Text', 'Polarity']

dict_data = [
{'Tweet Text': 't1', 'Polarity': 0.10},
{'Tweet Text': 't2', 'Polarity': 0.11},
{'Tweet Text': 't3', 'Polarity': 0.12}
]

csv_file = "SA.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error") 
