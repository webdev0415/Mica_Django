import psycopg2

# try:
#     connection = psycopg2.connect(host='st-writer-rds.advinow-dev.int',
#                                          database='oe2',
#                                          user='root',
#                                          password='aQfeW4D3')
try:
    connection = psycopg2.connect(host='ec2-75-101-232-85.compute-1.amazonaws.com',
                                         database='d2k0b436k14etr',
                                         user='ojllqbwycqqwoy',
                                         password='f21738c5889c44875f1afaf9ee3ffcb4ad705907af677041c4bddd8e91d3e3bb')
# try:
#     connection = psycopg2.connect(host='localhost',
#                                          database='advi',
#                                          user='postgres',
#                                          password='BillGates94415')
    postgreSql_insert_query = """INSERT INTO template_symptom_rows (id, symptom_id, symptomdatastore_id) 
                           VALUES 
('1', 1, 1),
('2', 1, 2),
('3', 1, 3),
('4', 1, 4),
('5', 2, 1),
('6', 2, 2),
('7', 2, 3),
('8', 2, 4),
('9', 3, 1),
('10', 3, 2),
('11', 3, 3),
('12', 3, 4)"""
    cursor = connection.cursor()
    cursor.execute(postgreSql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Symptom-SymptomDataStore table")
    cursor.close()
except psycopg2.OperationalError as error:
    print("Failed to insert record into Symptom-SymptomDataStore table {}".format(error))