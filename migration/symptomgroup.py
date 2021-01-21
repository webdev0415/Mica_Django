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

    postgreSql_insert_query = """INSERT INTO template_symptomgroup (id, name, symptom_count, code, group_id, category) 
                           VALUES 
('1', 'General', true, 'SG001', 'general', '{1,2,3}'),
('2', 'Behaviour', true, 'SG002', 'behaviour', '{1,2,3}'),
('3', 'Neurological', true, 'SG003', 'neurological', '{1,2,3}'),
('4', 'Physical', true, 'SG004', 'physical', '{1,2,3}'),
('5', 'Pain/Swelling', true, 'SG005', 'pain', '{1,2,3}'),
('6', 'Measurements', true, 'SG006', 'measurements', '{1,2,3}'),
('7', 'Labs', true, 'SG007', 'labs', '{1,2,3}'),
('8', 'Causes', true, 'SG008', 'causes', '{1,2,3}'),
('9', 'NLP', NULL, 'SG009', 'nlp', '{1,2,3}'),
('10', 'Triage', NULL, 'SG010', 'triage', '{1,2,3}')"""
    cursor = connection.cursor()
    cursor.execute(postgreSql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into SymptomGroup table")
    cursor.close()
except psycopg2.OperationalError as error:
    print("Failed to insert record into SnomedCode table {}".format(error))