from datetime import datetime

def transform_record(record):

    if record["delivery_date"]:
        delivery_date = datetime.strptime(record["delivery_date"], "%Y-%m-%d")
        shipment_date = datetime.strptime(record["shipment_date"], "%Y-%m-%d")

        delivery_days = (delivery_date - shipment_date).days
    else:
        delivery_days = None
    
    
    record["delivery_days"] = delivery_days
    record["delayed_flag"] = (delivery_days is not None and delivery_days > 3)
    
    record["cost"] = float(record["cost"])

    return record

