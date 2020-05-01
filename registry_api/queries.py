from django.db import connection


def perform_query(sql, params):
    with connection.cursor() as cursor:
        cursor.execute(sql, params)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return data


def get_average_price(start_date=None, end_date=None, postcode=None):
    """
    This function executes a SQL query over registry_api_landtransaction table
    It groups data by month and property type and it computes the average price for each group
    """
    sql = """
    SELECT date_trunc('month', date_of_transfer) as period, avg(price) as average_price, property_type
    from registry_api_landtransaction
    """
    params = []
    where_clause = []
    if start_date or end_date or postcode:
        sql += "WHERE "

    if postcode:
        where_clause.append("postcode = %s")
        params.append(postcode)

    if start_date:
        where_clause.append("date_of_transfer >= %s")
        params.append(start_date)

    if end_date:
        where_clause.append("date_of_transfer < %s")
        params.append(end_date)

    sql += " AND ".join(where_clause)
    sql += " GROUP BY period, property_type;"
    return perform_query(sql, params)


def get_transaction_prices(start_date=None, end_date=None, postcode=None):
    """
    This function executes a query over registry_api_landtransaction table
    The query groups the price column bu price intervals automatically using 
    width_bucket function.
    """
    
    
    min_max_sql = """
        SELECT
            min(price) as min_price,
            max(price) as max_price,
            (max(price) - min(price)) / 8 as bucket_width
        FROM registry_api_landtransaction
    """

    bucketing_query = """
        SELECT width_bucket(price, min_price, max_price, 8) as bucket, count(*) as cnt
        FROM registry_api_landtransaction, min_max
    """

    params = []
    where_clause = []
    if start_date or end_date or postcode:
        min_max_sql += "WHERE "
        bucketing_query += "WHERE "

    if postcode:
        where_clause.append("postcode = %s")
        params.append(postcode)

    if start_date:
        where_clause.append("date_of_transfer >= %s")
        params.append(start_date)

    if end_date:
        where_clause.append("date_of_transfer < %s")
        params.append(end_date)

    min_max_sql += " AND ".join(where_clause)

    bucketing_query += " AND ".join(where_clause)
    bucketing_query += " group by bucket order by bucket"

    final_query = f"""
    WITH min_max AS ({min_max_sql})
    SELECT bucket, min_price+(bucket-1)*bucket_width || '-' || min_price+bucket*bucket_width as range,
    cnt from ({bucketing_query}) x, min_max;
    """

    params.extend(params)
    return perform_query(final_query, params)
