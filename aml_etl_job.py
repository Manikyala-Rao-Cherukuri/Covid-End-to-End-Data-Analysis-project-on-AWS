import redshift_connector

try:
    # establishing the connection with Redshift using redshift_connector
    conn = redshift_connector.connect(
        host='manik-redshift-cluster-1.clmickzggmkl.us-east-1.redshift.amazonaws.com',
        port = 5439,
        database='dev',
        user='awsuser',
        password='Password1'
    )
    # by default it will execute after the query select statement
    conn.autocommit = True

    # command to get the redshift cursor
    cursor = redshift_connector.Cursor = conn.cursor()

    try:
        cursor.execute("""CREATE TABLE "customer_table" (
              "index" INTEGER,
              "customer_id" TEXT,
              "first_name" TEXT,
              "second_name" TEXT,
              "country" TEXT,
              "country_code" TEXT
              )""")

        cursor.execute("""CREATE TABLE "xref_table" (
              "index" INTEGER,
              "customer_id" TEXT,
              "account_num" INTEGER,
              "account_unique_id" TEXT
              )""")

        cursor.execute("""CREATE TABLE "swift_table" (
            "index" INTEGER,
              "extract_date" TEXT,
              "source_system" TEXT,
              "txn_ref_no_aml" TEXT,
              "receiver_account_id" TEXT,
              "reci_bank_id" TEXT,
              "stg_tag59_benfcust_account" TEXT,
              "stg_tag59_benfcust_name" TEXT,
              "stg_tag59_benfcust_address1" TEXT,
              "business_effective_date" TEXT
            )""")
    except Exception as e:
        # Handle the exception/error for the first data ingestion command
        print("Error occurred during the Tables creation:", e)

    try:
        cursor.execute("""
            copy customer_table from 's3://manik-sample-bucket/output1/cust_data.csv'
            credentials 'arn:aws:iam::267475256392:role/manik_role'
            delimiter ','
            region 'us-east-1'
            IGNOREHEADER 1
            """)
    except Exception as e:
        print("Error: Issue with inserting data into table")
        print(e)

    try:
        cursor.execute("""
            copy xref_table from 's3://manik-sample-bucket/output1/xref_data.csv'
            credentials 'arn:aws:iam::267475256392:role/manik_role'
            delimiter ','
            region 'us-east-1'
            IGNOREHEADER 1
            """)
    except Exception as e:
        print("Error: Issue with inserting data into table")
        print(e)

    try:
        cursor.execute("""
            copy swift_table from 's3://manik-sample-bucket/output1/swift_data.csv'
            credentials 'arn:aws:iam::267475256392:role/manik_role'
            delimiter ','
            region 'us-east-1'
            IGNOREHEADER 1
            """)
    except Exception as e:
        print("Error: Issue with inserting data into table")
        print(e)

except Exception as e:
    print("Issue with making connection to Redshift Data Warehouse\n")
    print(e)
finally:
    conn.close()
    cursor.close()
