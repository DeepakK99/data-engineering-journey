CREATE TABLE shipment_analytics (
    shipment_id TEXT PRIMARY KEY,
    customer_name TEXT,
    origin TEXT,
    destination TEXT,
    shipment_date DATE,
    delivery_date DATE,
    status TEXT,
    cost NUMERIC,
    delivery_days INT,
    delayed_flag BOOLEAN
);