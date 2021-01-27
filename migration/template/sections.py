import psycopg2

# try:
#     connection = psycopg2.connect(host='st-writer-rds.advinow-dev.int',
#                                          database='oe2',
#                                          user='root',
#                                          password='aQfeW4D3')
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