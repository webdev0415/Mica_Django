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
    postgreSql_insert_query = """INSERT INTO illness_category (id, code) 
                           VALUES 
('1', 'SW_BODYPART08'),
('2', 'PAIN_BODYPART93'),
('3', 'SW_BODYPART07'),
('4', 'SW_BODYPART72'),
('5', 'SW_BODYPART39'),
('6', 'PAIN_BODYPART98'),
('7', 'SW_BODYPART30'),
('8', 'PAIN_BODYPART96'),
('9', 'PAIN_BODYPART12'),
('10', 'SW_BODYPART19'),
('11', 'SW_BODYPART48'),
('12', 'SW_BODYPART62'),
('13', 'SW_BODYPART09'),
('14', 'PAIN_BODYPART79'),
('15', 'SW_BODYPART97'),
('16', 'PAIN_BODYPART81'),
('17', 'PAIN_BODYPART64'),
('18', 'PAIN_BODYPART34'),
('19', 'SYMPTCG25'),
('20', 'SW_BODYPART33'),
('21', 'SW_BODYPART27'),
('22', 'BODYPART55'),
('23', 'BODYPART57'),
('24', 'BODYPART16'),
('25', 'BODYPART14'),
('26', 'SW_BODYPART92'),
('27', 'SW_BODYPART61'),
('28', 'BODYPART53'),
('29', 'PAIN_BODYPART67'),
('30', 'SW_BODYPART94'),
('31', 'SW_BODYPART88'),
('32', 'SW_BODYPART57'),
('33', 'PAIN_BODYPART94'),
('34', 'PAIN_BODYPART55'),
('35', 'BODYPART08'),
('36', 'BODYPART48'),
('37', 'SW_BODYPART41'),
('38', 'BODYPART35'),
('39', 'PAIN_BODYPART17'),
('40', 'BODYPART09'),
('41', 'PAIN_BODYPART71'),
('42', 'PAIN_BODYPART83'),
('43', 'SW_BODYPART02'),
('44', 'SW_BODYPART17'),
('45', 'PAIN_BODYPART75'),
('46', 'SW_BODYPART21'),
('47', 'PAIN_BODYPART57'),
('48', 'BODYPART41'),
('49', 'BODYPART44'),
('50', 'BODYPART34'),
('51', 'PAIN_BODYPART24'),
('52', 'BODYPART02'),
('53', 'BODYPART05'),
('54', 'PAIN_BODYPART08'),
('55', 'BODYPART46'),
('56', 'SW_BODYPART84'),
('57', 'BODYPART19'),
('58', 'BODYPART17'),
('59', 'PAIN_BODYPART16'),
('60', 'PAIN_BODYPART62'),
('61', 'SW_BODYPART63'),
('62', 'SW_BODYPART70'),
('63', 'SW_BODYPART67'),
('64', 'PAIN_BODYPART38'),
('65', 'BODYPART27'),
('66', 'SW_BODYPART06'),
('67', 'PAIN_BODYPART89'),
('68', 'PAIN_BODYPART85'),
('69', 'BODYPART42'),
('70', 'BODYPART50'),
('71', 'SYMPTCG21'),
('72', 'SW_BODYPART64'),
('73', 'BODYPART26'),
('74', 'PAIN_BODYPART31'),
('75', 'SW_BODYPART98'),
('76', 'PAIN_BODYPART02'),
('77', 'SW_BODYPART82'),
('78', 'SYMPTCG13'),
('79', 'BODYPART13'),
('80', 'PAIN_BODYPART30'),
('81', 'SW_BODYPART44'),
('82', 'PAIN_BODYPART19'),
('83', 'PAIN_BODYPART91'),
('84', 'SW_BODYPART59'),
('85', 'SW_BODYPART91'),
('86', 'BODYPART22'),
('87', 'PAIN_BODYPART78'),
('88', 'PAIN_BODYPART95'),
('89', 'PAIN_BODYPART18'),
('90', 'SW_BODYPART68'),
('91', 'BODYPART15'),
('92', 'PAIN_BODYPART10'),
('93', 'SW_BODYPART37'),
('94', 'BODYPART54'),
('95', 'SYMPTCG32'),
('96', 'PAIN_BODYPART74'),
('97', 'SW_BODYPART75'),
('98', 'SYMPTCG28'),
('99', 'SYMPTCG26'),
('100', 'SW_BODYPART73'),
('101', 'SYMPTCG18'),
('102', 'BODYPART23'),
('103', 'SW_BODYPART69'),
('104', 'SYMPTCG24'),
('105', 'SYMPTCG06'),
('106', 'BODYPART21'),
('107', 'PAIN_BODYPART06'),
('108', 'PAIN_BODYPART82'),
('109', 'BODYPART51'),
('110', 'SYMPTCG14'),
('111', 'PAIN_BODYPART76'),
('112', 'PAIN_BODYPART23'),
('113', 'SYMPTCG30'),
('114', 'PAIN_BODYPART59'),
('115', 'BODYPART06'),
('116', 'PAIN_BODYPART29'),
('117', 'SYMPTCG04'),
('118', 'SYMPTCG35'),
('119', 'SYMPTCG09'),
('120', 'BODYPART20'),
('121', 'BODYPART38'),
('122', 'SW_BODYPART12'),
('123', 'SW_BODYPART53'),
('124', 'SW_BODYPART23'),
('125', 'PAIN_BODYPART26'),
('126', 'PAIN_BODYPART87'),
('127', 'SW_BODYPART13'),
('128', 'SW_BODYPART28'),
('129', 'BODYPART45'),
('130', 'SW_BODYPART35'),
('131', 'SW_BODYPART49'),
('132', 'BODYPART29'),
('133', 'PAIN_BODYPART52'),
('134', 'SW_BODYPART85'),
('135', 'PAIN_BODYPART58'),
('136', 'SW_BODYPART36'),
('137', 'BODYPART07'),
('138', 'SW_BODYPART54'),
('139', 'SW_BODYPART01'),
('140', 'PAIN_BODYPART45'),
('141', 'PAIN_BODYPART90'),
('142', 'BODYPART43'),
('143', 'SYMPTCG02'),
('144', 'SW_BODYPART66'),
('145', 'PAIN_BODYPART69'),
('146', 'PAIN_BODYPART51'),
('147', 'BODYPART12'),
('148', 'SW_BODYPART04'),
('149', 'PAIN_BODYPART50'),
('150', 'PAIN_BODYPART73'),
('151', 'SYMPTCG17'),
('152', 'BODYPART37'),
('153', 'SW_BODYPART05'),
('154', 'SW_BODYPART24'),
('155', 'SW_BODYPART93'),
('156', 'SW_BODYPART20'),
('157', 'BODYPART18'),
('158', 'PAIN_BODYPART36'),
('159', 'PAIN_BODYPART37'),
('160', 'SW_BODYPART29'),
('161', 'SW_BODYPART83'),
('162', 'BODYPART39'),
('163', 'PAIN_BODYPART68'),
('164', 'SW_BODYPART80'),
('165', 'SW_BODYPART18'),
('166', 'SW_BODYPART65'),
('167', 'SW_BODYPART10'),
('168', 'SW_BODYPART90'),
('169', 'PAIN_BODYPART15'),
('170', 'BODYPART59'),
('171', 'PAIN_BODYPART07'),
('172', 'PAIN_BODYPART70'),
('173', 'PAIN_BODYPART49'),
('174', 'PAIN_BODYPART09'),
('175', 'BODYPART49'),
('176', 'SW_BODYPART11'),
('177', 'PAIN_BODYPART25'),
('178', 'SW_BODYPART71'),
('179', 'BODYPART03'),
('180', 'BODYPART11'),
('181', 'PAIN_BODYPART28'),
('182', 'SW_BODYPART38'),
('183', 'PAIN_BODYPART14'),
('184', 'BODYPART36'),
('185', 'SW_BODYPART40'),
('186', 'PAIN_BODYPART61'),
('187', 'SYMPTCG27'),
('188', 'BODYPART60'),
('189', 'SYMPTCG19'),
('190', 'SW_BODYPART74'),
('191', 'SYMPTCG16'),
('192', 'PAIN_BODYPART04'),
('193', 'PAIN_BODYPART46'),
('194', 'SW_BODYPART22'),
('195', 'PAIN_BODYPART84'),
('196', 'PAIN_BODYPART72'),
('197', 'SW_BODYPART15'),
('198', 'SW_BODYPART16'),
('199', 'SW_BODYPART96'),
('200', 'SW_BODYPART81'),
('201', 'PAIN_BODYPART77'),
('202', 'PAIN_BODYPART40'),
('203', 'SYMPTCG22'),
('204', 'SYMPTCG10'),
('205', 'BODYPART10'),
('206', 'BODYPART32'),
('207', 'PAIN_BODYPART35'),
('208', 'SW_BODYPART87'),
('209', 'SYMPTCG01'),
('210', 'SYMPTCG20'),
('211', 'BODYPART01'),
('212', 'SW_BODYPART51'),
('213', 'PAIN_BODYPART80'),
('214', 'PAIN_BODYPART20'),
('215', 'BODYPART47'),
('216', 'SYMPTCG07'),
('217', 'SYMPTCG15'),
('218', 'SW_BODYPART89'),
('219', 'SW_BODYPART79'),
('220', 'PAIN_BODYPART33'),
('221', 'SW_BODYPART14'),
('222', 'SW_BODYPART26'),
('223', 'PAIN_BODYPART22'),
('224', 'PAIN_BODYPART05'),
('225', 'SW_BODYPART47'),
('226', 'PAIN_BODYPART44'),
('227', 'PAIN_BODYPART56'),
('228', 'BODYPART31'),
('229', 'SW_BODYPART58'),
('230', 'SW_BODYPART32'),
('231', 'SW_BODYPART31'),
('232', 'PAIN_BODYPART03'),
('233', 'BODYPART04'),
('234', 'PAIN_BODYPART41'),
('235', 'PAIN_BODYPART53'),
('236', 'PAIN_BODYPART21'),
('237', 'SW_BODYPART52'),
('238', 'SW_BODYPART50'),
('239', 'PAIN_BODYPART47'),
('240', 'PAIN_BODYPART54'),
('241', 'SW_BODYPART46'),
('242', 'SW_BODYPART55'),
('243', 'PAIN_BODYPART13'),
('244', 'PAIN_BODYPART48'),
('245', 'PAIN_BODYPART39'),
('246', 'SW_BODYPART25'),
('247', 'SW_BODYPART03'),
('248', 'PAIN_BODYPART32'),
('249', 'PAIN_BODYPART11'),
('250', 'SW_BODYPART56'),
('251', 'SW_BODYPART43'),
('252', 'PAIN_BODYPART01'),
('253', 'SW_BODYPART42'),
('254', 'PAIN_BODYPART43'),
('255', 'PAIN_BODYPART42'),
('256', 'PAIN_BODYPART27'),
('257', 'SW_BODYPART34'),
('258', 'SW_BODYPART45'),
('259', 'PAIN_BODYPART60'),
('260', 'PAIN_BODYPART86'),
('261', 'SW_BODYPART60'),
('262', 'BODYPART56'),
('263', 'PAIN_BODYPART65'),
('264', 'SW_BODYPART78'),
('265', 'SYMPTCG12'),
('266', 'PAIN_BODYPART88'),
('267', 'BODYPART40'),
('268', 'PAIN_BODYPART97'),
('269', 'SYMPTCG03'),
('270', 'PAIN_BODYPART92'),
('271', 'SYMPTCG05'),
('272', 'SYMPTCG11'),
('273', 'PAIN_BODYPART63'),
('274', 'SW_BODYPART100'),
('275', 'PAIN_BODYPART66'),
('276', 'SW_BODYPART77'),
('277', 'SW_BODYPART86'),
('278', 'SYMPTCG29'),
('279', 'SYMPTCG31'),
('280', 'SW_BODYPART76'),
('281', 'BODYPART52'),
('282', 'SYMPTCG23'),
('283', 'SW_BODYPART95')"""
    cursor = connection.cursor()
    cursor.execute(postgreSql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Category table")
    cursor.close()
except psycopg2.OperationalError as error:
    print("Failed to insert record into Category table {}".format(error))