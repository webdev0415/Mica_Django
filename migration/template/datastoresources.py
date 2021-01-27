import psycopg2

try:
    connection = psycopg2.connect(host='st-writer-rds.advinow-dev.int',
                                         database='oe2',
                                         user='root',
                                         password='aQfeW4D3')
# try:
#     connection = psycopg2.connect(host='localhost',
#                                          database='dun',
#                                          user='postgres',
#                                          password='BillGates94415')
    postgreSql_insert_query = """INSERT INTO template_datastoresources (id, time_frame) 
                           VALUES 

"""
    cursor = connection.cursor()
    cursor.execute(postgreSql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into DataStoreSources table")
    cursor.close()
except psycopg2.OperationalError as error:
    print("Failed to insert record into DataStoreSources table {}".format(error))