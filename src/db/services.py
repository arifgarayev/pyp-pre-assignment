import db.database as _database
import db.models as _models
import json

conn = _database.engine.connect()


def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)


def queries(start_date, end_date, option: int = None):
    """
    >>> print(queries("2013-01-01", "2014-12-12", option=1))
    :param option:
    :return:
    """

    if option == 1:

        query_res = conn.execute(
            f"""SELECT "Segment", CAST(SUM("Units Sold") AS DECIMAL(10,2)) AS "Total Units Sold (Qty)", CAST(SUM("Gross Sales") AS DECIMAL(10, 2)) AS "Total Gross Sales ($)", CAST(SUM("Discounts") AS DECIMAL(10, 2)) AS "Total Discounts (%%)", CAST(SUM("Profit") AS DECIMAL(10, 2)) AS "Total Profit ($)" FROM "data" WHERE "Date" BETWEEN '{start_date}' AND '{end_date}' GROUP BY "Segment" ;""")


    elif option == 2:
        query_res = conn.execute(
            f"""SELECT "Country", CAST(SUM("Units Sold") AS DECIMAL(10,2)) AS "Total Units Sold (Qty)", CAST(SUM("Gross Sales") AS DECIMAL(10, 2)) AS "Total Gross Sales ($)", CAST(SUM("Discounts") AS DECIMAL(10, 2)) AS "Total Discounts (%%)", CAST(SUM("Profit") AS DECIMAL(10, 2)) AS "Total Profit ($)" FROM "data" WHERE "Date" BETWEEN '{start_date}' AND '{end_date}' GROUP BY "Country" ;""")
        # print(a.fetchall())

    elif option == 3:
        query_res = conn.execute(
            f"""SELECT "Product", CAST(SUM("Units Sold") AS DECIMAL(10,2)) AS "Total Units Sold (Qty)", CAST(SUM("Gross Sales") AS DECIMAL(10, 2)) AS "Total Gross Sales ($)", CAST(SUM("Discounts") AS DECIMAL(10, 2)) AS "Total Discounts (%%)", CAST(SUM("Profit") AS DECIMAL(10, 2)) AS "Total Profit ($)" FROM "data" WHERE "Date" BETWEEN '{start_date}' AND '{end_date}' GROUP BY "Product" ;""")

    elif option == 4:
        query_res = conn.execute(
            f"""SELECT "Product", CAST(SUM("Discounts") AS DECIMAL(10, 2)) AS "Total Discounts (%%)" FROM "data" WHERE "Date" BETWEEN '{start_date}' AND '{end_date}' GROUP BY "Product" ;""")

    else:
        query_res = None


    return query_res


if __name__ == "__main__":
    import doctest
    doctest.testmod()