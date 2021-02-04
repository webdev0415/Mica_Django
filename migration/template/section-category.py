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

    postgreSql_insert_query = """INSERT INTO template_section_categories (id, section_id, symptomcategory_id) 
                           VALUES 
(1, 1, 237 ),
(2, 1, 235 ),
(3, 1, 236 ),
(4, 1, 213 ),
(5, 1, 214 ),
(6, 1, 212 ),
(7, 1, 215 ),
(8, 1, 186 ),
(9, 1, 187 ),
(10, 1, 184 ),
(11, 1, 185 ),
(12, 1, 181 ),
(13, 1, 180 ),
(14, 1, 163 ),
(15, 1, 164 ),
(16, 1, 161 ),
(17, 1, 162 ),
(18, 1, 159 ),
(19, 1, 160 ),
(20, 1, 175 ),
(21, 1, 147 ),
(22, 1, 146 ),
(23, 1, 141 ),
(24, 1, 140 ),
(25, 1, 139 ),
(26, 1, 145 ),
(27, 1, 144 ),
(28, 1, 143 ),
(29, 1, 142 ),
(30, 1, 115 ),
(31, 1, 122 ),
(32, 1, 123 ),
(33, 1, 120 ),
(34, 1, 121 ),
(35, 1, 118 ),
(36, 1, 119 ),
(37, 1, 116 ),
(38, 1, 117 ),
(39, 1, 24 ),
(40, 1, 23 ),
(41, 1, 22 ),
(42, 1, 21 ),
(43, 1, 20 ),
(44, 1, 3 ),
(45, 1, 2 ),
(46, 1, 5 ),
(47, 1, 4 ),
(48, 1, 7 ),
(49, 1, 6 ),
(50, 1, 9 ),
(51, 1, 8 ),
(52, 1, 133 ),
(53, 1, 132 ),
(54, 1, 135 ),
(55, 1, 134 ),
(56, 1, 137 ),
(57, 1, 136 ),
(58, 1, 1 ),
(59, 1, 138 ),
(60, 1, 18 ),
(61, 1, 19 ),
(62, 1, 10 ),
(63, 1, 11 ),
(64, 1, 12 ),
(65, 1, 13 ),
(66, 1, 14 ),
(67, 1, 15 ),
(68, 1, 16 ),
(69, 1, 17 ),
(70, 1, 125 ),
(71, 1, 124 ),
(72, 1, 127 ),
(73, 1, 126 ),
(74, 1, 129 ),
(75, 1, 128 ),
(76, 1, 131 ),
(77, 1, 130 ),
(78, 2, 238 ),
(79, 2, 239 ),
(80, 2, 232 ),
(81, 2, 217 ),
(82, 2, 218 ),
(83, 2, 216 ),
(84, 2, 219 ),
(85, 2, 191 ),
(86, 2, 190 ),
(87, 2, 188 ),
(88, 2, 189 ),
(89, 2, 183 ),
(90, 2, 182 ),
(91, 2, 176 ),
(92, 2, 165 ),
(93, 2, 166 ),
(94, 2, 167 ),
(95, 2, 168 ),
(96, 2, 169 ),
(97, 2, 170 ),
(98, 2, 149 ),
(99, 2, 148 ),
(100, 2, 153 ),
(101, 2, 152 ),
(102, 2, 151 ),
(103, 2, 150 ),
(104, 2, 155 ),
(105, 2, 154 ),
(106, 2, 156 ),
(107, 2, 37 ),
(108, 2, 36 ),
(109, 2, 39 ),
(110, 2, 38 ),
(111, 2, 33 ),
(112, 2, 32 ),
(113, 2, 35 ),
(114, 2, 34 ),
(115, 2, 45 ),
(116, 2, 72 ),
(117, 2, 61 ),
(118, 2, 60 ),
(119, 2, 63 ),
(120, 2, 62 ),
(121, 2, 57 ),
(122, 2, 56 ),
(123, 2, 59 ),
(124, 2, 58 ),
(125, 2, 53 ),
(126, 2, 52 ),
(127, 2, 55 ),
(128, 2, 54 ),
(129, 2, 49 ),
(130, 2, 48 ),
(131, 2, 51 ),
(132, 2, 50 ),
(133, 2, 70 ),
(134, 2, 71 ),
(135, 2, 66 ),
(136, 2, 67 ),
(137, 2, 68 ),
(138, 2, 69 ),
(139, 2, 64 ),
(140, 2, 65 ),
(141, 2, 27 ),
(142, 2, 26 ),
(143, 2, 25 ),
(144, 2, 31 ),
(145, 2, 30 ),
(146, 2, 29 ),
(147, 2, 28 ),
(148, 2, 42 ),
(149, 2, 43 ),
(150, 2, 40 ),
(151, 2, 41 ),
(152, 2, 46 ),
(153, 2, 47 ),
(154, 2, 44 )"""
    cursor = connection.cursor()
    cursor.execute(postgreSql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Section-Category table")
    cursor.close()
except psycopg2.OperationalError as error:
    print("Failed to insert record into Section-Category table {}".format(error))