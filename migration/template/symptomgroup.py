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


    postgreSql_insert_query = """INSERT INTO mica_template_symptomgroup (id, name, symptom_count, code, group_id, create_date, updated_date) 
                           VALUES 
('1', 'General', true, 'SG001', 'general', NULL, 1609796373579),
('2', 'Behaviour', true, 'SG002', 'behaviour', NULL, 1606232586755),
('3', 'Neurological', true, 'SG003', 'neurological', NULL, 1606233288533),
('4', 'Physical', true, 'SG004', 'physical', NULL, 1611345333242),
('5', 'Pain/Swelling', true, 'SG005', 'pain', NULL, 1606233288533),
('6', 'Measurements', true, 'SG006', 'measurements', NULL, 1610386758919),
('7', 'Labs', true, 'SG007', 'labs', NULL, 1604690692143),
('8', 'Causes', true, 'SG008', 'causes', NULL, 1598976440335),
('9', 'NLP', NULL, 'SG009', 'nlp', NULL, 1610138732353),
('10', 'Triage', NULL, 'SG010', 'triage', NULL, 1598976440335)"""
    cursor = connection.cursor()
    cursor.execute(postgreSql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into SymptomGroup table")
    cursor.close()
except psycopg2.OperationalError as error:
    print("Failed to insert record into SymptomGroup table {}".format(error))