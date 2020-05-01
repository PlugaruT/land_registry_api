from django.db import connection


def perform_query(sql, params):
    with connection.cursor() as cursor:
        cursor.execute(sql, params)
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return data


def get_average_price(start_date=None, end_date=None, postcode=None):
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

def get_number_of_transactions(start_date=None, end_date=None, postcode=None):
    pass
