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
    postgreSql_insert_query = """INSERT INTO treatment_treatmenttyperefmodel (id, name, active, type_id, tre_type) 
                           VALUES 
('1', 'Physical Exam', false, 11, 'physicalexam'),
('2', 'OTC Drugs', true, 12, 'otcdrugs'),
('3', 'Prescription Drugs', true, 0, 'prescription'),
('4', 'Diet', true, 1, 'diet'),
('5', 'Activity', true, 2, 'activity'),
('6', 'Physical Therapy', true, 3, 'therapy' ),
('7', 'Counseling', true, 4, 'counseling' ),
('8', 'Return to Work/School Status', true, 5, 'work'),
('9', 'Wound Care', true, 6, 'woundcare'),
('10', 'Imaging', true, 7, 'imaging'),
('11', 'Labs', true, 8, 'labs'),
('12', 'Procedures', true, 9, 'procedures'),
('13', 'Discharge Disposition', true, 10, 'discharge')"""
    cursor = connection.cursor()
    cursor.execute(postgreSql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into TreatmentTypeRef table")
    cursor.close()
except psycopg2.OperationalError as error:
    print("Failed to insert record into TreatmentTypeRef table {}".format(error))