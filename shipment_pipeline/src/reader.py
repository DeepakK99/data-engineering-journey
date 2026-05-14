import csv

def read_shipments(file_path):
    try:
        with open(file_path, mode= 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                yield row
    except Exception as e:
        ...