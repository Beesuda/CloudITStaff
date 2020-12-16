import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                  password="HYSmki13553",
                                  host="node7511-itstaff-cloud.app.ruk-com.cloud",
                                  #host="node7074-itstaff-cloud00.googlejp.app.ruk-com.cloud",
                                  port="11065",
                                  database="CloudDB")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
