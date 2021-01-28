import psycopg2

try:
    connection = psycopg2.connect(host='st-writer-rds.advinow-dev.int',
                                         database='oe2',
                                         user='root',
                                         password='aQfeW4D3')
try:
    connection = psycopg2.connect(host='ec2-54-224-124-241.compute-1.amazonaws.com',
                                         database='d6m3jhsgo1lsed',
                                         user='qkxkflfqjvnlzr',
                                         password='433644d041ee0701bd60b800251da4ad9dcb07696ebb736e7837212538151370')
# try:
#     connection = psycopg2.connect(host='localhost',
#                                          database='advi',
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