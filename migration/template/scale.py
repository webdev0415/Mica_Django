import psycopg2

try:
    connection = psycopg2.connect(host='st-writer-rds.advinow-dev.int',
                                         database='oe2',
                                         user='root',
                                         password='aQfeW4D3')
# try:
#     connection = psycopg2.connect(host='ec2-50-16-108-254.compute-1.amazonaws.com',
#                                          database='d9v89qak4p5fl8',
#                                          user='rkjgpgunvofpws',
#                                          password='03cb1ce45185cb70077acf3b73fc0b4bae1f17937b0058ce9fa62254472570ac')
# try:
#     connection = psycopg2.connect(host='localhost',
#                                          database='advi',
#                                          user='postgres',
#                                          password='BillGates94415')

    postgreSql_insert_query = """INSERT INTO template_scale (id, time_frame) 
                           VALUES 
('1', 'Longer'),
('1', '1-3 Days'),
('1', 'Yesterday'),
('1', '1-3 Months'),
('1', 'Less than 1 Month'),
('1', 'Less than 1 Day'),
('1', '1-3 Weeks'),
('1', 'Less than 1 Week')"""
    cursor = connection.cursor()
    cursor.execute(postgreSql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Scale table")
    cursor.close()
except psycopg2.OperationalError as error:
    print("Failed to insert record into Scale table {}".format(error))