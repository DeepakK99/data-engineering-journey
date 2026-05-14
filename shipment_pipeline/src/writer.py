import csv

fieldnames = [
    "shipment_id",
    "customer_name",
    "origin",
    "destination",
    "shipment_date",
    "delivery_date",
    "status",
    "cost",
    "delivery_days",
    "delayed_flag"
]

def write_shipments(file_path, records):
    with open(file_path, mode= 'w', newline= '') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames) # ignores extra, fills empty "" for missing fields

        writer.writeheader()

        for record in records:
            writer.writerow({
                key: record.get(key, None)
                for key in fieldnames
            })