def clean_record(record):

    record["customer_name"] = (
        record["customer_name"].strip()
    )

    record["status"] = (
        record["status"].strip().title()
    )

    record["origin"] = (
        record["origin"].strip().title()
    )

    return record