import psycopg2

# try:
#     connection = psycopg2.connect(host='st-writer-rds.advinow-dev.int',
#                                          database='oe2',
#                                          user='root',
#                                          password='aQfeW4D3')
# try:
#     connection = psycopg2.connect(host='ec2-50-16-108-254.compute-1.amazonaws.com',
#                                          database='d9v89qak4p5fl8',
#                                          user='rkjgpgunvofpws',
#                                          password='03cb1ce45185cb70077acf3b73fc0b4bae1f17937b0058ce9fa62254472570ac')
try:
    connection = psycopg2.connect(host='localhost',
                                         database='advi',
                                         user='postgres',
                                         password='BillGates94415')

    postgreSql_insert_query = """INSERT INTO template_section (id, name, section_id) 
                           VALUES 
('1', 'pain', 'SC001'),
('2', 'swelling', 'SC002')"""
    cursor = connection.cursor()
    cursor.execute(postgreSql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Sections table")
    cursor.close()
except psycopg2.OperationalError as error:
    print("Failed to insert record into Sections table {}".format(error))