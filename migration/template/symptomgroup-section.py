import psycopg2

# try:
#     connection = psycopg2.connect(host='st-writer-rds.advinow-dev.int',
#                                          database='oe2',
#                                          user='root',
#                                          password='aQfeW4D3')
# try:
#     connection = psycopg2.connect(host='ec2-75-101-232-85.compute-1.amazonaws.com',
#                                          database='d2k0b436k14etr',
#                                          user='ojllqbwycqqwoy',
#                                          password='f21738c5889c44875f1afaf9ee3ffcb4ad705907af677041c4bddd8e91d3e3bb')
try:
    connection = psycopg2.connect(host='ec2-50-16-108-254.compute-1.amazonaws.com',
                                         database='d9v89qak4p5fl8',
                                         user='rkjgpgunvofpws',
                                         password='03cb1ce45185cb70077acf3b73fc0b4bae1f17937b0058ce9fa62254472570ac')
# try:
#     connection = psycopg2.connect(host='localhost',
#                                          database='advi',
#                                          user='postgres',
#                                          password='BillGates94415')
    postgreSql_insert_query = """INSERT INTO template_symptomgroup_sections (id, symptomgroup_id, section_id) 
                           VALUES 
(1, 5, 1),
(2, 5, 2)"""
    cursor = connection.cursor()
    cursor.execute(postgreSql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into SymptomGroup-Section table")
    cursor.close()
except psycopg2.OperationalError as error:
    print("Failed to insert record into SymptomGroup-Section table {}".format(error))