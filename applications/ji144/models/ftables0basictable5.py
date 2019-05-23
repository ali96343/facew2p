
db.define_table('ui0switchestable0',
   Field( 'f0', 'string',  label= 'Size', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Example', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'CSS Class', default= 'w2p f2' ), 
      )
if not db(db.ui0switchestable0.id ).count():
      db.ui0switchestable0.insert( f0= '00 ui0switchestable0', f1= '0w2p1 Example', f2= '0w2p2 CSS Class', )
      db.ui0switchestable0.insert( f0= 'Large', f1= 'unk_0', f2= 'Add following code size= lg', )
      db.ui0switchestable0.insert( f0= 'Default', f1= 'unk_1', f2= 'unk_2', )
      db.ui0switchestable0.insert( f0= 'Small', f1= 'unk_3', f2= 'Add following code size= sm', )
      db.ui0switchestable0.insert( f0= 'Extra small', f1= 'unk_4', f2= 'Add following code size= xs', )
db.define_table('tables0datatable0',
   Field( 'f0', 'string',  label= 'Name', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Position', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Office', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Salary', default= 'w2p f3' ), 
      )
if not db(db.tables0datatable0.id ).count():
      db.tables0datatable0.insert( f0= '00 tables0datatable0', f1= '0w2p1 Position', f2= '0w2p2 Office', f3= '0w2p3 Salary', )
      db.tables0datatable0.insert( f0= 'Tiger Nixon', f1= 'System Architect', f2= 'Edinburgh', f3= '$320,800', )
      db.tables0datatable0.insert( f0= 'Garrett Winters', f1= 'Accountant', f2= 'Tokyo', f3= '$170,750', )
      db.tables0datatable0.insert( f0= 'Ashton Cox', f1= 'Junior Technical Author', f2= 'San Francisco', f3= '$86,000', )
      db.tables0datatable0.insert( f0= 'Cedric Kelly', f1= 'Senior Javascript Developer', f2= 'Edinburgh', f3= '$433,060', )
      db.tables0datatable0.insert( f0= 'Airi Satou', f1= 'Accountant', f2= 'Tokyo', f3= '$162,700', )
      db.tables0datatable0.insert( f0= 'Brielle Williamson', f1= 'Integration Specialist', f2= 'New York', f3= '$372,000', )
      db.tables0datatable0.insert( f0= 'Herrod Chandler', f1= 'Sales Assistant', f2= 'San Francisco', f3= '$137,500', )
      db.tables0datatable0.insert( f0= 'Rhona Davidson', f1= 'Integration Specialist', f2= 'Tokyo', f3= '$327,900', )
      db.tables0datatable0.insert( f0= 'Colleen Hurst', f1= 'Javascript Developer', f2= 'San Francisco', f3= '$205,500', )
      db.tables0datatable0.insert( f0= 'Sonya Frost', f1= 'Software Engineer', f2= 'Edinburgh', f3= '$103,600', )
      db.tables0datatable0.insert( f0= 'Jena Gaines', f1= 'Office Manager', f2= 'London', f3= '$90,560', )
      db.tables0datatable0.insert( f0= 'Quinn Flynn', f1= 'Support Lead', f2= 'Edinburgh', f3= '$342,000', )
      db.tables0datatable0.insert( f0= 'Charde Marshall', f1= 'Regional Director', f2= 'San Francisco', f3= '$470,600', )
      db.tables0datatable0.insert( f0= 'Haley Kennedy', f1= 'Senior Marketing Designer', f2= 'London', f3= '$313,500', )
      db.tables0datatable0.insert( f0= 'Tatyana Fitzpatrick', f1= 'Regional Director', f2= 'London', f3= '$385,750', )
      db.tables0datatable0.insert( f0= 'Michael Silva', f1= 'Marketing Designer', f2= 'London', f3= '$198,500', )
      db.tables0datatable0.insert( f0= 'Paul Byrd', f1= 'Chief Financial Officer (CFO)', f2= 'New York', f3= '$725,000', )
      db.tables0datatable0.insert( f0= 'Gloria Little', f1= 'Systems Administrator', f2= 'New York', f3= '$237,500', )
      db.tables0datatable0.insert( f0= 'Bradley Greer', f1= 'Software Engineer', f2= 'London', f3= '$132,000', )
      db.tables0datatable0.insert( f0= 'Dai Rios', f1= 'Personnel Lead', f2= 'Edinburgh', f3= '$217,500', )
      db.tables0datatable0.insert( f0= 'Jenette Caldwell', f1= 'Development Lead', f2= 'New York', f3= '$345,000', )
      db.tables0datatable0.insert( f0= 'Yuri Berry', f1= 'Chief Marketing Officer (CMO)', f2= 'New York', f3= '$675,000', )
      db.tables0datatable0.insert( f0= 'Caesar Vance', f1= 'Pre-Sales Support', f2= 'New York', f3= '$106,450', )
      db.tables0datatable0.insert( f0= 'Doris Wilder', f1= 'Sales Assistant', f2= 'Sidney', f3= '$85,600', )
      db.tables0datatable0.insert( f0= 'Angelica Ramos', f1= 'Chief Executive Officer (CEO)', f2= 'London', f3= '$1,200,000', )
      db.tables0datatable0.insert( f0= 'Gavin Joyce', f1= 'Developer', f2= 'Edinburgh', f3= '$92,575', )
      db.tables0datatable0.insert( f0= 'Jennifer Chang', f1= 'Regional Director', f2= 'Singapore', f3= '$357,650', )
      db.tables0datatable0.insert( f0= 'Brenden Wagner', f1= 'Software Engineer', f2= 'San Francisco', f3= '$206,850', )
      db.tables0datatable0.insert( f0= 'Fiona Green', f1= 'Chief Operating Officer (COO)', f2= 'San Francisco', f3= '$850,000', )
      db.tables0datatable0.insert( f0= 'Shou Itou', f1= 'Regional Marketing', f2= 'Tokyo', f3= '$163,000', )
      db.tables0datatable0.insert( f0= 'Michelle House', f1= 'Integration Specialist', f2= 'Sidney', f3= '$95,400', )
      db.tables0datatable0.insert( f0= 'Suki Burks', f1= 'Developer', f2= 'London', f3= '$114,500', )
      db.tables0datatable0.insert( f0= 'Prescott Bartlett', f1= 'Technical Author', f2= 'London', f3= '$145,000', )
      db.tables0datatable0.insert( f0= 'Gavin Cortez', f1= 'Team Leader', f2= 'San Francisco', f3= '$235,500', )
      db.tables0datatable0.insert( f0= 'Martena Mccray', f1= 'Post-Sales support', f2= 'Edinburgh', f3= '$324,050', )
      db.tables0datatable0.insert( f0= 'Unity Butler', f1= 'Marketing Designer', f2= 'San Francisco', f3= '$85,675', )
      db.tables0datatable0.insert( f0= 'Howard Hatfield', f1= 'Office Manager', f2= 'San Francisco', f3= '$164,500', )
      db.tables0datatable0.insert( f0= 'Hope Fuentes', f1= 'Secretary', f2= 'San Francisco', f3= '$109,850', )
      db.tables0datatable0.insert( f0= 'Vivian Harrell', f1= 'Financial Controller', f2= 'San Francisco', f3= '$452,500', )
      db.tables0datatable0.insert( f0= 'Timothy Mooney', f1= 'Office Manager', f2= 'London', f3= '$136,200', )
      db.tables0datatable0.insert( f0= 'Jackson Bradshaw', f1= 'Director', f2= 'New York', f3= '$645,750', )
      db.tables0datatable0.insert( f0= 'Olivia Liang', f1= 'Support Engineer', f2= 'Singapore', f3= '$234,500', )
      db.tables0datatable0.insert( f0= 'Bruno Nash', f1= 'Software Engineer', f2= 'London', f3= '$163,500', )
      db.tables0datatable0.insert( f0= 'Sakura Yamamoto', f1= 'Support Engineer', f2= 'Tokyo', f3= '$139,575', )
      db.tables0datatable0.insert( f0= 'Thor Walton', f1= 'Developer', f2= 'New York', f3= '$98,540', )
      db.tables0datatable0.insert( f0= 'Finn Camacho', f1= 'Support Engineer', f2= 'San Francisco', f3= '$87,500', )
      db.tables0datatable0.insert( f0= 'Serge Baldwin', f1= 'Data Coordinator', f2= 'Singapore', f3= '$138,575', )
      db.tables0datatable0.insert( f0= 'Zenaida Frank', f1= 'Software Engineer', f2= 'New York', f3= '$125,250', )
      db.tables0datatable0.insert( f0= 'Zorita Serrano', f1= 'Software Engineer', f2= 'San Francisco', f3= '$115,000', )
      db.tables0datatable0.insert( f0= 'Jennifer Acosta', f1= 'Junior Javascript Developer', f2= 'Edinburgh', f3= '$75,650', )
      db.tables0datatable0.insert( f0= 'Cara Stevens', f1= 'Sales Assistant', f2= 'New York', f3= '$145,600', )
      db.tables0datatable0.insert( f0= 'Hermione Butler', f1= 'Regional Director', f2= 'London', f3= '$356,250', )
      db.tables0datatable0.insert( f0= 'Lael Greer', f1= 'Systems Administrator', f2= 'London', f3= '$103,500', )
      db.tables0datatable0.insert( f0= 'Jonas Alexander', f1= 'Developer', f2= 'San Francisco', f3= '$86,500', )
      db.tables0datatable0.insert( f0= 'Shad Decker', f1= 'Regional Director', f2= 'Edinburgh', f3= '$183,000', )
      db.tables0datatable0.insert( f0= 'Michael Bruce', f1= 'Javascript Developer', f2= 'Singapore', f3= '$183,000', )
      db.tables0datatable0.insert( f0= 'Donna Snider', f1= 'Customer Support', f2= 'New York', f3= '$112,000', )
db.define_table('tables0basictable0',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'First', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Last', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Handle', default= 'w2p f3' ), 
      )
if not db(db.tables0basictable0.id ).count():
      db.tables0basictable0.insert( f0= '00 tables0basictable0', f1= '0w2p1 First', f2= '0w2p2 Last', f3= '0w2p3 Handle', )
      db.tables0basictable0.insert( f0= '1', f1= 'Mark', f2= 'Otto', f3= '@mdo', )
      db.tables0basictable0.insert( f0= '2', f1= 'Jacob', f2= 'Thornton', f3= '@fat', )
      db.tables0basictable0.insert( f0= '3', f1= 'Larry', f2= 'the Bird', f3= '@twitter', )
db.define_table('tables0basictable1',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'First', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Last', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Handle', default= 'w2p f3' ), 
      )
if not db(db.tables0basictable1.id ).count():
      db.tables0basictable1.insert( f0= '00 tables0basictable1', f1= '0w2p1 First', f2= '0w2p2 Last', f3= '0w2p3 Handle', )
      db.tables0basictable1.insert( f0= '1', f1= 'Mark', f2= 'Otto', f3= '@mdo', )
      db.tables0basictable1.insert( f0= '2', f1= 'Jacob', f2= 'Thornton', f3= '@fat', )
      db.tables0basictable1.insert( f0= '3', f1= 'Larry', f2= 'the Bird', f3= '@twitter', )
db.define_table('tables0basictable2',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'First', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Last', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Handle', default= 'w2p f3' ), 
      )
if not db(db.tables0basictable2.id ).count():
      db.tables0basictable2.insert( f0= '00 tables0basictable2', f1= '0w2p1 First', f2= '0w2p2 Last', f3= '0w2p3 Handle', )
      db.tables0basictable2.insert( f0= '1', f1= 'Mark', f2= 'Otto', f3= '@mdo', )
      db.tables0basictable2.insert( f0= '2', f1= 'Jacob', f2= 'Thornton', f3= '@fat', )
      db.tables0basictable2.insert( f0= '3', f1= 'Larry', f2= 'the Bird', f3= '@twitter', )
db.define_table('tables0basictable3',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'First', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Last', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Handle', default= 'w2p f3' ), 
      )
if not db(db.tables0basictable3.id ).count():
      db.tables0basictable3.insert( f0= '00 tables0basictable3', f1= '0w2p1 First', f2= '0w2p2 Last', f3= '0w2p3 Handle', )
      db.tables0basictable3.insert( f0= '1', f1= 'Mark', f2= 'Otto', f3= '@mdo', )
      db.tables0basictable3.insert( f0= '2', f1= 'Jacob', f2= 'Thornton', f3= '@fat', )
      db.tables0basictable3.insert( f0= '3', f1= 'Larry', f2= 'the Bird', f3= '@twitter', )
db.define_table('tables0basictable4',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'First', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Last', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Handle', default= 'w2p f3' ), 
      )
if not db(db.tables0basictable4.id ).count():
      db.tables0basictable4.insert( f0= '00 tables0basictable4', f1= '0w2p1 First', f2= '0w2p2 Last', f3= '0w2p3 Handle', )
      db.tables0basictable4.insert( f0= '1', f1= 'Mark', f2= 'Otto', f3= '@mdo', )
      db.tables0basictable4.insert( f0= '2', f1= 'Jacob', f2= 'Thornton', f3= '@fat', )
      db.tables0basictable4.insert( f0= '3', f1= 'Larry the Bird', f2= '@twitter', )
db.define_table('tables0basictable5',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'First', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Last', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Handle', default= 'w2p f3' ), 
      )
if not db(db.tables0basictable5.id ).count():
      db.tables0basictable5.insert( f0= '00 tables0basictable5', f1= '0w2p1 First', f2= '0w2p2 Last', f3= '0w2p3 Handle', )
      db.tables0basictable5.insert( f0= '1', f1= 'Mark', f2= 'Otto', f3= '@mdo', )
      db.tables0basictable5.insert( f0= '2', f1= 'Jacob', f2= 'Thornton', f3= '@fat', )
      db.tables0basictable5.insert( f0= '3', f1= 'Larry the Bird', f2= '@twitter', )