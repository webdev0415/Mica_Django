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
    postgreSql_insert_query = """INSERT INTO template_symptomgroup_categories (id, symptomgroup_id, symptomcategory_id) 
                           VALUES 
(1, 1, 84),
(2, 1, 47),
(3, 1, 163),
(4, 1, 55),
(5, 1, 175),
(6, 2, 230),
(7, 2, 225),
(8, 2, 166),
(9, 2, 234),
(10, 2, 105),
(11, 3, 7),
(12, 3, 131),
(13, 3, 220),
(14, 3, 187),
(15, 3, 67),
(16, 4, 192),
(17, 4, 169),
(18, 4, 158),
(19, 4, 51),
(20, 4, 115),
(21, 5, 158),
(22, 5, 161),
(23, 5, 223),
(24, 5, 212),
(25, 5, 117),
(26, 6, 139),
(27, 6, 58),
(28, 6, 57),
(29, 6, 208),
(30, 6, 91),
(31, 7, 158),
(32, 7, 107),
(33, 7, 9),
(34, 7, 192),
(35, 7, 38),
(36, 8, 225),
(37, 8, 90),
(38, 8, 238),
(39, 8, 106),
(40, 8, 17),
(41, 9, 173),
(42, 9, 8),
(43, 9, 66),
(44, 9, 143),
(45, 9, 117),
(46, 10, 69),
(47, 10, 112),
(48, 10, 108),
(49, 10, 157),
(50, 10, 10)"""
    cursor = connection.cursor()
    cursor.execute(postgreSql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into SymptomGroup-SymptomCategory table")
    cursor.close()
except psycopg2.OperationalError as error:
    print("Failed to insert record into SymptomGroup-SymptomCategory table {}".format(error))