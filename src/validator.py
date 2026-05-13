from datetime import datetime

VALID_STATUSES = {"Delivered", "Delayed", "In Transit", "Pending"}


def validate_record(record):

    if not record["shipment_id"]:
        return False

    status = record["status"]

    if status not in VALID_STATUSES:
        return False

    try:
        cost = float(record["cost"])

        if cost < 0:
            return False

    except ValueError:
        return False

    try:
        shipment_date = datetime.strptime(record["shipment_date"], "%Y-%m-%d")

    except ValueError:
        return False

    delivery_date_str = record["delivery_date"]

    # delivery date optional for pending shipments
    if delivery_date_str:

        try:
            delivery_date = datetime.strptime(delivery_date_str, "%Y-%m-%d")

            if delivery_date < shipment_date:
                return False

        except ValueError:
            return False

    return True
