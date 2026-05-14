from datetime import datetime


def transform_record(record):

    shipment_date = datetime.strptime(record["shipment_date"], "%Y-%m-%d")

    if record["delivery_date"]:

        delivery_date = datetime.strptime(record["delivery_date"], "%Y-%m-%d")

    else:

        delivery_date = None

    delivery_days = (delivery_date - shipment_date).days if delivery_date else None

    record["delivery_days"] = delivery_days

    record["delayed_flag"] = delivery_days is not None and delivery_days > 3

    record["cost"] = float(record["cost"])

    record["shipment_date"] = shipment_date

    record["delivery_date"] = delivery_date

    return record
