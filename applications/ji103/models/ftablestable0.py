
db.define_table('indextable0',
   Field( 'f0', 'string', label= 'ЩЩЩ Name', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'ЧЧЧЧ Position', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'ЪЪЪЪ Office', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'ЮЮЮ Age', default= 'w2p f3' ), 
   Field( 'f4', 'datetime', label= 'ЗЗЗ Start date', default = request.now, requires = IS_DATETIME(format=T('%d.%m.%Y %H:%M:%S') )), 
   Field( 'f5', 'string', label= 'Salary', default= 'w2p f5' ), 
      )
if not db(db.indextable0.id ).count():
         from gluon.contrib.populate import populate
         populate(db.indextable0  , 59) 

db.define_table('tablestable0',
   Field( 'f0', 'string', label= 'Name', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'Position', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Office', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'Age', default= 'w2p f3' ), 
   Field( 'f4', 'string', label= 'Start date', default= 'w2p f4' ), 
   Field( 'f5', 'string', label= 'Salary', default= 'w2p f5' ), 
      )
if not db(db.tablestable0.id ).count():
      db.tablestable0.insert( f0= '00 tablestable0', f1= '0w2p1 Position', f2= '0w2p2 Office', f3= '0w2p3 Age', f4= '0w2p4 Start date', f5= '0w2p5 Salary', )
      db.tablestable0.insert( f0= 'Name', f1= 'Position', f2= 'Office', f3= 'Age', f4= 'Start date', f5= 'Salary', )
      db.tablestable0.insert( f0= 'Tiger Nixon', f1= 'System Architect', f2= 'Edinburgh', f3= '61', f4= '2011/04/25', f5= '$320,800', )
      db.tablestable0.insert( f0= 'Garrett Winters', f1= 'Accountant', f2= 'Tokyo', f3= '63', f4= '2011/07/25', f5= '$170,750', )
      db.tablestable0.insert( f0= 'Ashton Cox', f1= 'Junior Technical Author', f2= 'San Francisco', f3= '66', f4= '2009/01/12', f5= '$86,000', )
      db.tablestable0.insert( f0= 'Cedric Kelly', f1= 'Senior Javascript Developer', f2= 'Edinburgh', f3= '22', f4= '2012/03/29', f5= '$433,060', )
      db.tablestable0.insert( f0= 'Airi Satou', f1= 'Accountant', f2= 'Tokyo', f3= '33', f4= '2008/11/28', f5= '$162,700', )
      db.tablestable0.insert( f0= 'Brielle Williamson', f1= 'Integration Specialist', f2= 'New York', f3= '61', f4= '2012/12/02', f5= '$372,000', )
      db.tablestable0.insert( f0= 'Herrod Chandler', f1= 'Sales Assistant', f2= 'San Francisco', f3= '59', f4= '2012/08/06', f5= '$137,500', )
      db.tablestable0.insert( f0= 'Rhona Davidson', f1= 'Integration Specialist', f2= 'Tokyo', f3= '55', f4= '2010/10/14', f5= '$327,900', )
      db.tablestable0.insert( f0= 'Colleen Hurst', f1= 'Javascript Developer', f2= 'San Francisco', f3= '39', f4= '2009/09/15', f5= '$205,500', )
      db.tablestable0.insert( f0= 'Sonya Frost', f1= 'Software Engineer', f2= 'Edinburgh', f3= '23', f4= '2008/12/13', f5= '$103,600', )
      db.tablestable0.insert( f0= 'Jena Gaines', f1= 'Office Manager', f2= 'London', f3= '30', f4= '2008/12/19', f5= '$90,560', )
      db.tablestable0.insert( f0= 'Quinn Flynn', f1= 'Support Lead', f2= 'Edinburgh', f3= '22', f4= '2013/03/03', f5= '$342,000', )
      db.tablestable0.insert( f0= 'Charde Marshall', f1= 'Regional Director', f2= 'San Francisco', f3= '36', f4= '2008/10/16', f5= '$470,600', )
      db.tablestable0.insert( f0= 'Haley Kennedy', f1= 'Senior Marketing Designer', f2= 'London', f3= '43', f4= '2012/12/18', f5= '$313,500', )
      db.tablestable0.insert( f0= 'Tatyana Fitzpatrick', f1= 'Regional Director', f2= 'London', f3= '19', f4= '2010/03/17', f5= '$385,750', )
      db.tablestable0.insert( f0= 'Michael Silva', f1= 'Marketing Designer', f2= 'London', f3= '66', f4= '2012/11/27', f5= '$198,500', )
      db.tablestable0.insert( f0= 'Paul Byrd', f1= 'Chief Financial Officer (CFO)', f2= 'New York', f3= '64', f4= '2010/06/09', f5= '$725,000', )
      db.tablestable0.insert( f0= 'Gloria Little', f1= 'Systems Administrator', f2= 'New York', f3= '59', f4= '2009/04/10', f5= '$237,500', )
      db.tablestable0.insert( f0= 'Bradley Greer', f1= 'Software Engineer', f2= 'London', f3= '41', f4= '2012/10/13', f5= '$132,000', )
      db.tablestable0.insert( f0= 'Dai Rios', f1= 'Personnel Lead', f2= 'Edinburgh', f3= '35', f4= '2012/09/26', f5= '$217,500', )
      db.tablestable0.insert( f0= 'Jenette Caldwell', f1= 'Development Lead', f2= 'New York', f3= '30', f4= '2011/09/03', f5= '$345,000', )
      db.tablestable0.insert( f0= 'Yuri Berry', f1= 'Chief Marketing Officer (CMO)', f2= 'New York', f3= '40', f4= '2009/06/25', f5= '$675,000', )
      db.tablestable0.insert( f0= 'Caesar Vance', f1= 'Pre-Sales Support', f2= 'New York', f3= '21', f4= '2011/12/12', f5= '$106,450', )
      db.tablestable0.insert( f0= 'Doris Wilder', f1= 'Sales Assistant', f2= 'Sidney', f3= '23', f4= '2010/09/20', f5= '$85,600', )
      db.tablestable0.insert( f0= 'Angelica Ramos', f1= 'Chief Executive Officer (CEO)', f2= 'London', f3= '47', f4= '2009/10/09', f5= '$1,200,000', )
      db.tablestable0.insert( f0= 'Gavin Joyce', f1= 'Developer', f2= 'Edinburgh', f3= '42', f4= '2010/12/22', f5= '$92,575', )
      db.tablestable0.insert( f0= 'Jennifer Chang', f1= 'Regional Director', f2= 'Singapore', f3= '28', f4= '2010/11/14', f5= '$357,650', )
      db.tablestable0.insert( f0= 'Brenden Wagner', f1= 'Software Engineer', f2= 'San Francisco', f3= '28', f4= '2011/06/07', f5= '$206,850', )
      db.tablestable0.insert( f0= 'Fiona Green', f1= 'Chief Operating Officer (COO)', f2= 'San Francisco', f3= '48', f4= '2010/03/11', f5= '$850,000', )
      db.tablestable0.insert( f0= 'Shou Itou', f1= 'Regional Marketing', f2= 'Tokyo', f3= '20', f4= '2011/08/14', f5= '$163,000', )
      db.tablestable0.insert( f0= 'Michelle House', f1= 'Integration Specialist', f2= 'Sidney', f3= '37', f4= '2011/06/02', f5= '$95,400', )
      db.tablestable0.insert( f0= 'Suki Burks', f1= 'Developer', f2= 'London', f3= '53', f4= '2009/10/22', f5= '$114,500', )
      db.tablestable0.insert( f0= 'Prescott Bartlett', f1= 'Technical Author', f2= 'London', f3= '27', f4= '2011/05/07', f5= '$145,000', )
      db.tablestable0.insert( f0= 'Gavin Cortez', f1= 'Team Leader', f2= 'San Francisco', f3= '22', f4= '2008/10/26', f5= '$235,500', )
      db.tablestable0.insert( f0= 'Martena Mccray', f1= 'Post-Sales support', f2= 'Edinburgh', f3= '46', f4= '2011/03/09', f5= '$324,050', )
      db.tablestable0.insert( f0= 'Unity Butler', f1= 'Marketing Designer', f2= 'San Francisco', f3= '47', f4= '2009/12/09', f5= '$85,675', )
      db.tablestable0.insert( f0= 'Howard Hatfield', f1= 'Office Manager', f2= 'San Francisco', f3= '51', f4= '2008/12/16', f5= '$164,500', )
      db.tablestable0.insert( f0= 'Hope Fuentes', f1= 'Secretary', f2= 'San Francisco', f3= '41', f4= '2010/02/12', f5= '$109,850', )
      db.tablestable0.insert( f0= 'Vivian Harrell', f1= 'Financial Controller', f2= 'San Francisco', f3= '62', f4= '2009/02/14', f5= '$452,500', )
      db.tablestable0.insert( f0= 'Timothy Mooney', f1= 'Office Manager', f2= 'London', f3= '37', f4= '2008/12/11', f5= '$136,200', )
      db.tablestable0.insert( f0= 'Jackson Bradshaw', f1= 'Director', f2= 'New York', f3= '65', f4= '2008/09/26', f5= '$645,750', )
      db.tablestable0.insert( f0= 'Olivia Liang', f1= 'Support Engineer', f2= 'Singapore', f3= '64', f4= '2011/02/03', f5= '$234,500', )
      db.tablestable0.insert( f0= 'Bruno Nash', f1= 'Software Engineer', f2= 'London', f3= '38', f4= '2011/05/03', f5= '$163,500', )
      db.tablestable0.insert( f0= 'Sakura Yamamoto', f1= 'Support Engineer', f2= 'Tokyo', f3= '37', f4= '2009/08/19', f5= '$139,575', )
      db.tablestable0.insert( f0= 'Thor Walton', f1= 'Developer', f2= 'New York', f3= '61', f4= '2013/08/11', f5= '$98,540', )
      db.tablestable0.insert( f0= 'Finn Camacho', f1= 'Support Engineer', f2= 'San Francisco', f3= '47', f4= '2009/07/07', f5= '$87,500', )
      db.tablestable0.insert( f0= 'Serge Baldwin', f1= 'Data Coordinator', f2= 'Singapore', f3= '64', f4= '2012/04/09', f5= '$138,575', )
      db.tablestable0.insert( f0= 'Zenaida Frank', f1= 'Software Engineer', f2= 'New York', f3= '63', f4= '2010/01/04', f5= '$125,250', )
      db.tablestable0.insert( f0= 'Zorita Serrano', f1= 'Software Engineer', f2= 'San Francisco', f3= '56', f4= '2012/06/01', f5= '$115,000', )
      db.tablestable0.insert( f0= 'Jennifer Acosta', f1= 'Junior Javascript Developer', f2= 'Edinburgh', f3= '43', f4= '2013/02/01', f5= '$75,650', )
      db.tablestable0.insert( f0= 'Cara Stevens', f1= 'Sales Assistant', f2= 'New York', f3= '46', f4= '2011/12/06', f5= '$145,600', )
      db.tablestable0.insert( f0= 'Hermione Butler', f1= 'Regional Director', f2= 'London', f3= '47', f4= '2011/03/21', f5= '$356,250', )
      db.tablestable0.insert( f0= 'Lael Greer', f1= 'Systems Administrator', f2= 'London', f3= '21', f4= '2009/02/27', f5= '$103,500', )
      db.tablestable0.insert( f0= 'Jonas Alexander', f1= 'Developer', f2= 'San Francisco', f3= '30', f4= '2010/07/14', f5= '$86,500', )
      db.tablestable0.insert( f0= 'Shad Decker', f1= 'Regional Director', f2= 'Edinburgh', f3= '51', f4= '2008/11/13', f5= '$183,000', )
      db.tablestable0.insert( f0= 'Michael Bruce', f1= 'Javascript Developer', f2= 'Singapore', f3= '29', f4= '2011/06/27', f5= '$183,000', )
      db.tablestable0.insert( f0= 'Donna Snider', f1= 'Customer Support', f2= 'New York', f3= '27', f4= '2011/01/25', f5= '$112,000', )