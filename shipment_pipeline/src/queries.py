import logging

def get_delayed_shipments(conn):
    if not conn:
        return
    
    try:

        cursor = conn.cursor()

        query = """
        SELECT *
        FROM shipment_analytics
        WHERE delayed_flag = TRUE;
        """

        cursor.execute(query)

        results = cursor.fetchall()

        return results

    except Exception as e:

        logging.error(f"Query failed: {e}")

        return []

def get_average_delivery_time(conn):
    if not conn:
        return
    
    try:

        cursor = conn.cursor()

        query = """
        SELECT AVG(delivery_days)
        FROM shipment_analytics;
        """

        cursor.execute(query)

        results = cursor.fetchall()

        return results

    except Exception as e:

        logging.error(f"Query failed: {e}")

        return []
    
def get_revenue_by_route(conn):
    if not conn:
        return
    
    try:

        cursor = conn.cursor()

        query = """
        SELECT
            origin,
            destination,
            SUM(cost) AS total_revenue
        FROM shipment_analytics
        GROUP BY origin, destination
        ORDER BY total_revenue DESC;
        """

        cursor.execute(query)

        results = cursor.fetchall()

        return results

    except Exception as e:

        logging.error(f"Query failed: {e}")

        return []

def get_top_customers(conn):
    if not conn:
        return
    
    try:

        cursor = conn.cursor()

        query = """
        SELECT
            customer_name,
            SUM(cost) AS total_spent
        FROM shipment_analytics
        GROUP BY customer_name
        ORDER BY total_spent DESC;
        """

        cursor.execute(query)

        results = cursor.fetchall()

        return results

    except Exception as e:

        logging.error(f"Query failed: {e}")

        return []
