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
    postgreSql_insert_query = """INSERT INTO illness_illnessdata_symptom_groups (id, illnessdata_id, symptomgroup_id) 
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
    print(cursor.rowcount, "Record inserted successfully into Illness-SymptomGroup table")
    cursor.close()
except psycopg2.OperationalError as error:
    print("Failed to insert record into Illness-SymptomGroup table {}".format(error))