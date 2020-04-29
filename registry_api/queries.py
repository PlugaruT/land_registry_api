from django.db import connection

def perform_query(sql, params):
    with connection.cursor() as cursor:
        cursor.execute(sql, params)
        data = cursor.fetchall()

    return data

def get_average_price(start_date, end_date, postcode):
    sql = """
    SELECT date_trunc('month', date_of_transfer) as period, avg(price) as average_price, property_type
    FROM registry_api_landtransaction
    WHERE postcode = %s
    GROUP BY period, property_type
    """
    
    
    return perform_query(sql, [start_date, end_date, postcode])
    
    
    
