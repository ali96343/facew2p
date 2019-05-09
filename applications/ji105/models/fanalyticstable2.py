
db.define_table('index03table0',
   Field( 'f0', 'string', label= 'ID', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'Name', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Price', default= 'w2p f2' ), 
      )
if not db(db.index03table0.id ).count():
      db.index03table0.insert( f0= '00 index03table0', f1= '0w2p1 Name', f2= '0w2p2 Price', )
      db.index03table0.insert( f0= '4555', f1= 'Samsung Galaxy Mega', f2= '$921', )
      db.index03table0.insert( f0= '4556', f1= 'Huawei Ascend P6', f2= '$240', )
      db.index03table0.insert( f0= '8778', f1= 'HTC One M8', f2= '$400', )
      db.index03table0.insert( f0= '5667', f1= 'Samsung Galaxy Alpha', f2= '$870', )
      db.index03table0.insert( f0= '7886', f1= 'LG G3', f2= '$790', )
db.define_table('indextable0',
   Field( 'f0', 'string', label= 'ID', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'Name', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Price', default= 'w2p f2' ), 
      )
if not db(db.indextable0.id ).count():
      db.indextable0.insert( f0= '00 indextable0', f1= '0w2p1 Name', f2= '0w2p2 Price', )
      db.indextable0.insert( f0= '4555', f1= 'Samsung Galaxy Mega', f2= '$921', )
      db.indextable0.insert( f0= '4556', f1= 'Huawei Ascend P6', f2= '$240', )
      db.indextable0.insert( f0= '8778', f1= 'HTC One M8', f2= '$400', )
      db.indextable0.insert( f0= '5667', f1= 'Samsung Galaxy Alpha', f2= '$870', )
      db.indextable0.insert( f0= '7886', f1= 'LG G3', f2= '$790', )
db.define_table('invoicetable0',
   Field( 'f0', 'string', label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'Item Title', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Unit Price', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'Quantity', default= 'w2p f3' ), 
   Field( 'f4', 'string', label= 'Total', default= 'w2p f4' ), 
      )
if not db(db.invoicetable0.id ).count():
      db.invoicetable0.insert( f0= '00 invoicetable0', f1= '0w2p1 Item Title', f2= '0w2p2 Unit Price', f3= '0w2p3 Quantity', f4= '0w2p4 Total', )
      db.invoicetable0.insert( f0= '1', f1= 'Crusal Damperal', f2= '$500', f3= '05', f4= '$3000', )
      db.invoicetable0.insert( f0= '2', f1= 'Indriacal Superral', f2= '$650', f3= '06', f4= '$7000', )
      db.invoicetable0.insert( f0= '3', f1= 'Vidaska Adrioal', f2= '$400', f3= '03', f4= '$2000', )
      db.invoicetable0.insert( f0= '4', f1= 'Croustal Desrikal', f2= '$600', f3= '04', f4= '$7000', )
db.define_table('normal0tabletable0',
   Field( 'f0', 'string', label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'Username', default= 'w2p f3' ), 
   Field( 'f4', 'string', label= 'Nickname', default= 'w2p f4' ), 
      )
if not db(db.normal0tabletable0.id ).count():
      db.normal0tabletable0.insert( f0= '00 normal0tabletable0', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Username', f4= '0w2p4 Nickname', )
      db.normal0tabletable0.insert( f0= '1', f1= 'Alexandra', f2= 'Christopher', f3= '@makinton', f4= 'Ducky', )
      db.normal0tabletable0.insert( f0= '2', f1= 'Madeleine', f2= 'Hollaway', f3= '@hollway', f4= 'Cheese', )
      db.normal0tabletable0.insert( f0= '3', f1= 'Sebastian', f2= 'Johnston', f3= '@sebastian', f4= 'Jaycee', )
      db.normal0tabletable0.insert( f0= '4', f1= 'Mitchell', f2= 'Christin', f3= '@mitchell4u', f4= 'AdskiDeAnus', )
      db.normal0tabletable0.insert( f0= '5', f1= 'Elizabeth', f2= 'Belkitt', f3= '@belkitt', f4= 'Goat', )
      db.normal0tabletable0.insert( f0= '6', f1= 'Benjamin', f2= 'Parnell', f3= '@wayne234', f4= 'Pokie', )
      db.normal0tabletable0.insert( f0= '7', f1= 'Katherine', f2= 'Buckland', f3= '@anitabelle', f4= 'Wokie', )
      db.normal0tabletable0.insert( f0= '8', f1= 'Nicholas', f2= 'Walmart', f3= '@mwalmart', f4= 'Spike', )
db.define_table('normal0tabletable1',
   Field( 'f0', 'string', label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'Username', default= 'w2p f3' ), 
   Field( 'f4', 'string', label= 'Nickname', default= 'w2p f4' ), 
      )
if not db(db.normal0tabletable1.id ).count():
      db.normal0tabletable1.insert( f0= '00 normal0tabletable1', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Username', f4= '0w2p4 Nickname', )
      db.normal0tabletable1.insert( f0= '1', f1= 'Alexandra', f2= 'Christopher', f3= '@makinton', f4= 'Ducky', )
      db.normal0tabletable1.insert( f0= '2', f1= 'Madeleine', f2= 'Hollaway', f3= '@hollway', f4= 'Cheese', )
      db.normal0tabletable1.insert( f0= '3', f1= 'Sebastian', f2= 'Johnston', f3= '@sebastian', f4= 'Jaycee', )
      db.normal0tabletable1.insert( f0= '4', f1= 'Mitchell', f2= 'Christin', f3= '@mitchell4u', f4= 'AdskiDeAnus', )
      db.normal0tabletable1.insert( f0= '5', f1= 'Elizabeth', f2= 'Belkitt', f3= '@belkitt', f4= 'Goat', )
      db.normal0tabletable1.insert( f0= '6', f1= 'Benjamin', f2= 'Parnell', f3= '@wayne234', f4= 'Pokie', )
      db.normal0tabletable1.insert( f0= '7', f1= 'Katherine', f2= 'Buckland', f3= '@anitabelle', f4= 'Wokie', )
      db.normal0tabletable1.insert( f0= '8', f1= 'Nicholas', f2= 'Walmart', f3= '@mwalmart', f4= 'Spike', )
db.define_table('normal0tabletable2',
   Field( 'f0', 'string', label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'Username', default= 'w2p f3' ), 
   Field( 'f4', 'string', label= 'Nickname', default= 'w2p f4' ), 
      )
if not db(db.normal0tabletable2.id ).count():
      db.normal0tabletable2.insert( f0= '00 normal0tabletable2', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Username', f4= '0w2p4 Nickname', )
      db.normal0tabletable2.insert( f0= '1', f1= 'Alexandra', f2= 'Christopher', f3= '@makinton', f4= 'Ducky', )
      db.normal0tabletable2.insert( f0= '2', f1= 'Madeleine', f2= 'Hollaway', f3= '@hollway', f4= 'Cheese', )
      db.normal0tabletable2.insert( f0= '3', f1= 'Sebastian', f2= 'Johnston', f3= '@sebastian', f4= 'Jaycee', )
      db.normal0tabletable2.insert( f0= '4', f1= 'Mitchell', f2= 'Christin', f3= '@mitchell4u', f4= 'AdskiDeAnus', )
      db.normal0tabletable2.insert( f0= '5', f1= 'Elizabeth', f2= 'Belkitt', f3= '@belkitt', f4= 'Goat', )
      db.normal0tabletable2.insert( f0= '6', f1= 'Benjamin', f2= 'Parnell', f3= '@wayne234', f4= 'Pokie', )
      db.normal0tabletable2.insert( f0= '7', f1= 'Katherine', f2= 'Buckland', f3= '@anitabelle', f4= 'Wokie', )
      db.normal0tabletable2.insert( f0= '8', f1= 'Nicholas', f2= 'Walmart', f3= '@mwalmart', f4= 'Spike', )
db.define_table('normal0tabletable3',
   Field( 'f0', 'string', label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'Username', default= 'w2p f3' ), 
   Field( 'f4', 'string', label= 'Nickname', default= 'w2p f4' ), 
      )
if not db(db.normal0tabletable3.id ).count():
      db.normal0tabletable3.insert( f0= '00 normal0tabletable3', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Username', f4= '0w2p4 Nickname', )
      db.normal0tabletable3.insert( f0= '1', f1= 'Alexandra', f2= 'Christopher', f3= '@makinton', f4= 'Ducky', )
      db.normal0tabletable3.insert( f0= '2', f1= 'Madeleine', f2= 'Hollaway', f3= '@hollway', f4= 'Cheese', )
      db.normal0tabletable3.insert( f0= '3', f1= 'Sebastian', f2= 'Johnston', f3= '@sebastian', f4= 'Jaycee', )
      db.normal0tabletable3.insert( f0= '4', f1= 'Mitchell', f2= 'Christin', f3= '@mitchell4u', f4= 'AdskiDeAnus', )
      db.normal0tabletable3.insert( f0= '5', f1= 'Elizabeth', f2= 'Belkitt', f3= '@belkitt', f4= 'Goat', )
      db.normal0tabletable3.insert( f0= '6', f1= 'Benjamin', f2= 'Parnell', f3= '@wayne234', f4= 'Pokie', )
      db.normal0tabletable3.insert( f0= '7', f1= 'Katherine', f2= 'Buckland', f3= '@anitabelle', f4= 'Wokie', )
      db.normal0tabletable3.insert( f0= '8', f1= 'Nicholas', f2= 'Walmart', f3= '@mwalmart', f4= 'Spike', )
db.define_table('normal0tabletable4',
   Field( 'f0', 'string', label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'Username', default= 'w2p f3' ), 
   Field( 'f4', 'string', label= 'Nickname', default= 'w2p f4' ), 
      )
if not db(db.normal0tabletable4.id ).count():
      db.normal0tabletable4.insert( f0= '00 normal0tabletable4', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Username', f4= '0w2p4 Nickname', )
      db.normal0tabletable4.insert( f0= '1', f1= 'Alexandra', f2= 'Christopher', f3= '@makinton', f4= 'Ducky', )
      db.normal0tabletable4.insert( f0= '2', f1= 'Madeleine', f2= 'Hollaway', f3= '@hollway', f4= 'Cheese', )
      db.normal0tabletable4.insert( f0= '3', f1= 'Sebastian', f2= 'Johnston', f3= '@sebastian', f4= 'Jaycee', )
      db.normal0tabletable4.insert( f0= '4', f1= 'Mitchell', f2= 'Christin', f3= '@mitchell4u', f4= 'AdskiDeAnus', )
      db.normal0tabletable4.insert( f0= '5', f1= 'Elizabeth', f2= 'Belkitt', f3= '@belkitt', f4= 'Goat', )
      db.normal0tabletable4.insert( f0= '6', f1= 'Benjamin', f2= 'Parnell', f3= '@wayne234', f4= 'Pokie', )
      db.normal0tabletable4.insert( f0= '7', f1= 'Katherine', f2= 'Buckland', f3= '@anitabelle', f4= 'Wokie', )
      db.normal0tabletable4.insert( f0= '8', f1= 'Nicholas', f2= 'Walmart', f3= '@mwalmart', f4= 'Spike', )
db.define_table('normal0tabletable5',
   Field( 'f0', 'string', label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'Username', default= 'w2p f3' ), 
   Field( 'f4', 'string', label= 'Nickname', default= 'w2p f4' ), 
      )
if not db(db.normal0tabletable5.id ).count():
      db.normal0tabletable5.insert( f0= '00 normal0tabletable5', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Username', f4= '0w2p4 Nickname', )
      db.normal0tabletable5.insert( f0= '1', f1= 'Alexandra', f2= 'Christopher', f3= '@makinton', f4= 'Ducky', )
      db.normal0tabletable5.insert( f0= '3', f1= 'Sebastian', f2= 'Johnston', f3= '@sebastian', f4= 'Jaycee', )
      db.normal0tabletable5.insert( f0= '4', f1= 'Mitchell', f2= 'Christin', f3= '@mitchell4u', f4= 'AdskiDeAnus', )
      db.normal0tabletable5.insert( f0= '2', f1= 'Madeleine', f2= 'Hollaway', f3= '@hollway', f4= 'Cheese', )
      db.normal0tabletable5.insert( f0= '5', f1= 'Elizabeth', f2= 'Belkitt', f3= '@belkitt', f4= 'Goat', )
db.define_table('index02table0',
   Field( 'f0', 'string', label= 'ID', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'Name', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Price', default= 'w2p f2' ), 
      )
if not db(db.index02table0.id ).count():
      db.index02table0.insert( f0= '00 index02table0', f1= '0w2p1 Name', f2= '0w2p2 Price', )
      db.index02table0.insert( f0= '4555', f1= 'Samsung Galaxy Mega', f2= '$921', )
      db.index02table0.insert( f0= '4556', f1= 'Huawei Ascend P6', f2= '$240', )
      db.index02table0.insert( f0= '8778', f1= 'HTC One M8', f2= '$400', )
      db.index02table0.insert( f0= '5667', f1= 'Samsung Galaxy Alpha', f2= '$870', )
      db.index02table0.insert( f0= '7886', f1= 'LG G3', f2= '$790', )
db.define_table('index04table0',
   Field( 'f0', 'string', label= 'ID', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'Name', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Price', default= 'w2p f2' ), 
      )
if not db(db.index04table0.id ).count():
      db.index04table0.insert( f0= '00 index04table0', f1= '0w2p1 Name', f2= '0w2p2 Price', )
      db.index04table0.insert( f0= '4555', f1= 'Samsung Galaxy Mega', f2= '$921', )
      db.index04table0.insert( f0= '4556', f1= 'Huawei Ascend P6', f2= '$240', )
      db.index04table0.insert( f0= '8778', f1= 'HTC One M8', f2= '$400', )
      db.index04table0.insert( f0= '5667', f1= 'Samsung Galaxy Alpha', f2= '$870', )
      db.index04table0.insert( f0= '7886', f1= 'LG G3', f2= '$790', )
db.define_table('data0tabletable0',
   Field( 'f0', 'string', label= 'Name', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'Position', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Office', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'Age', default= 'w2p f3' ), 
   Field( 'f4', 'string', label= 'Start date', default= 'w2p f4' ), 
   Field( 'f5', 'string', label= 'Salary', default= 'w2p f5' ), 
      )
if not db(db.data0tabletable0.id ).count():
      db.data0tabletable0.insert( f0= '00 data0tabletable0', f1= '0w2p1 Position', f2= '0w2p2 Office', f3= '0w2p3 Age', f4= '0w2p4 Start date', f5= '0w2p5 Salary', )
      db.data0tabletable0.insert( f0= 'Tiger Nixon', f1= 'System Architect', f2= 'Edinburgh', f3= '61', f4= '2011/04/25', f5= '$320,800', )
      db.data0tabletable0.insert( f0= 'Garrett Winters', f1= 'Accountant', f2= 'Tokyo', f3= '63', f4= '2011/07/25', f5= '$170,750', )
      db.data0tabletable0.insert( f0= 'Ashton Cox', f1= 'Junior Technical Author', f2= 'San Francisco', f3= '66', f4= '2009/01/12', f5= '$86,000', )
      db.data0tabletable0.insert( f0= 'Cedric Kelly', f1= 'Senior Javascript Developer', f2= 'Edinburgh', f3= '22', f4= '2012/03/29', f5= '$433,060', )
      db.data0tabletable0.insert( f0= 'Airi Satou', f1= 'Accountant', f2= 'Tokyo', f3= '33', f4= '2008/11/28', f5= '$162,700', )
      db.data0tabletable0.insert( f0= 'Brielle Williamson', f1= 'Integration Specialist', f2= 'New York', f3= '61', f4= '2012/12/02', f5= '$372,000', )
      db.data0tabletable0.insert( f0= 'Herrod Chandler', f1= 'Sales Assistant', f2= 'San Francisco', f3= '59', f4= '2012/08/06', f5= '$137,500', )
      db.data0tabletable0.insert( f0= 'Rhona Davidson', f1= 'Integration Specialist', f2= 'Tokyo', f3= '55', f4= '2010/10/14', f5= '$327,900', )
      db.data0tabletable0.insert( f0= 'Colleen Hurst', f1= 'Javascript Developer', f2= 'San Francisco', f3= '39', f4= '2009/09/15', f5= '$205,500', )
      db.data0tabletable0.insert( f0= 'Sonya Frost', f1= 'Software Engineer', f2= 'Edinburgh', f3= '23', f4= '2008/12/13', f5= '$103,600', )
      db.data0tabletable0.insert( f0= 'Jena Gaines', f1= 'Office Manager', f2= 'London', f3= '30', f4= '2008/12/19', f5= '$90,560', )
      db.data0tabletable0.insert( f0= 'Quinn Flynn', f1= 'Support Lead', f2= 'Edinburgh', f3= '22', f4= '2013/03/03', f5= '$342,000', )
      db.data0tabletable0.insert( f0= 'Charde Marshall', f1= 'Regional Director', f2= 'San Francisco', f3= '36', f4= '2008/10/16', f5= '$470,600', )
      db.data0tabletable0.insert( f0= 'Haley Kennedy', f1= 'Senior Marketing Designer', f2= 'London', f3= '43', f4= '2012/12/18', f5= '$313,500', )
      db.data0tabletable0.insert( f0= 'Tatyana Fitzpatrick', f1= 'Regional Director', f2= 'London', f3= '19', f4= '2010/03/17', f5= '$385,750', )
      db.data0tabletable0.insert( f0= 'Michael Silva', f1= 'Marketing Designer', f2= 'London', f3= '66', f4= '2012/11/27', f5= '$198,500', )
      db.data0tabletable0.insert( f0= 'Paul Byrd', f1= 'Chief Financial Officer (CFO)', f2= 'New York', f3= '64', f4= '2010/06/09', f5= '$725,000', )
      db.data0tabletable0.insert( f0= 'Gloria Little', f1= 'Systems Administrator', f2= 'New York', f3= '59', f4= '2009/04/10', f5= '$237,500', )
      db.data0tabletable0.insert( f0= 'Bradley Greer', f1= 'Software Engineer', f2= 'London', f3= '41', f4= '2012/10/13', f5= '$132,000', )
      db.data0tabletable0.insert( f0= 'Dai Rios', f1= 'Personnel Lead', f2= 'Edinburgh', f3= '35', f4= '2012/09/26', f5= '$217,500', )
      db.data0tabletable0.insert( f0= 'Jenette Caldwell', f1= 'Development Lead', f2= 'New York', f3= '30', f4= '2011/09/03', f5= '$345,000', )
      db.data0tabletable0.insert( f0= 'Yuri Berry', f1= 'Chief Marketing Officer (CMO)', f2= 'New York', f3= '40', f4= '2009/06/25', f5= '$675,000', )
      db.data0tabletable0.insert( f0= 'Caesar Vance', f1= 'Pre-Sales Support', f2= 'New York', f3= '21', f4= '2011/12/12', f5= '$106,450', )
      db.data0tabletable0.insert( f0= 'Doris Wilder', f1= 'Sales Assistant', f2= 'Sidney', f3= '23', f4= '2010/09/20', f5= '$85,600', )
      db.data0tabletable0.insert( f0= 'Angelica Ramos', f1= 'Chief Executive Officer (CEO)', f2= 'London', f3= '47', f4= '2009/10/09', f5= '$1,200,000', )
      db.data0tabletable0.insert( f0= 'Gavin Joyce', f1= 'Developer', f2= 'Edinburgh', f3= '42', f4= '2010/12/22', f5= '$92,575', )
      db.data0tabletable0.insert( f0= 'Jennifer Chang', f1= 'Regional Director', f2= 'Singapore', f3= '28', f4= '2010/11/14', f5= '$357,650', )
      db.data0tabletable0.insert( f0= 'Brenden Wagner', f1= 'Software Engineer', f2= 'San Francisco', f3= '28', f4= '2011/06/07', f5= '$206,850', )
      db.data0tabletable0.insert( f0= 'Fiona Green', f1= 'Chief Operating Officer (COO)', f2= 'San Francisco', f3= '48', f4= '2010/03/11', f5= '$850,000', )
      db.data0tabletable0.insert( f0= 'Shou Itou', f1= 'Regional Marketing', f2= 'Tokyo', f3= '20', f4= '2011/08/14', f5= '$163,000', )
      db.data0tabletable0.insert( f0= 'Michelle House', f1= 'Integration Specialist', f2= 'Sidney', f3= '37', f4= '2011/06/02', f5= '$95,400', )
      db.data0tabletable0.insert( f0= 'Suki Burks', f1= 'Developer', f2= 'London', f3= '53', f4= '2009/10/22', f5= '$114,500', )
      db.data0tabletable0.insert( f0= 'Prescott Bartlett', f1= 'Technical Author', f2= 'London', f3= '27', f4= '2011/05/07', f5= '$145,000', )
      db.data0tabletable0.insert( f0= 'Gavin Cortez', f1= 'Team Leader', f2= 'San Francisco', f3= '22', f4= '2008/10/26', f5= '$235,500', )
      db.data0tabletable0.insert( f0= 'Martena Mccray', f1= 'Post-Sales support', f2= 'Edinburgh', f3= '46', f4= '2011/03/09', f5= '$324,050', )
      db.data0tabletable0.insert( f0= 'Unity Butler', f1= 'Marketing Designer', f2= 'San Francisco', f3= '47', f4= '2009/12/09', f5= '$85,675', )
      db.data0tabletable0.insert( f0= 'Howard Hatfield', f1= 'Office Manager', f2= 'San Francisco', f3= '51', f4= '2008/12/16', f5= '$164,500', )
      db.data0tabletable0.insert( f0= 'Hope Fuentes', f1= 'Secretary', f2= 'San Francisco', f3= '41', f4= '2010/02/12', f5= '$109,850', )
      db.data0tabletable0.insert( f0= 'Vivian Harrell', f1= 'Financial Controller', f2= 'San Francisco', f3= '62', f4= '2009/02/14', f5= '$452,500', )
      db.data0tabletable0.insert( f0= 'Timothy Mooney', f1= 'Office Manager', f2= 'London', f3= '37', f4= '2008/12/11', f5= '$136,200', )
      db.data0tabletable0.insert( f0= 'Jackson Bradshaw', f1= 'Director', f2= 'New York', f3= '65', f4= '2008/09/26', f5= '$645,750', )
      db.data0tabletable0.insert( f0= 'Olivia Liang', f1= 'Support Engineer', f2= 'Singapore', f3= '64', f4= '2011/02/03', f5= '$234,500', )
      db.data0tabletable0.insert( f0= 'Bruno Nash', f1= 'Software Engineer', f2= 'London', f3= '38', f4= '2011/05/03', f5= '$163,500', )
      db.data0tabletable0.insert( f0= 'Sakura Yamamoto', f1= 'Support Engineer', f2= 'Tokyo', f3= '37', f4= '2009/08/19', f5= '$139,575', )
      db.data0tabletable0.insert( f0= 'Thor Walton', f1= 'Developer', f2= 'New York', f3= '61', f4= '2013/08/11', f5= '$98,540', )
      db.data0tabletable0.insert( f0= 'Finn Camacho', f1= 'Support Engineer', f2= 'San Francisco', f3= '47', f4= '2009/07/07', f5= '$87,500', )
      db.data0tabletable0.insert( f0= 'Serge Baldwin', f1= 'Data Coordinator', f2= 'Singapore', f3= '64', f4= '2012/04/09', f5= '$138,575', )
      db.data0tabletable0.insert( f0= 'Zenaida Frank', f1= 'Software Engineer', f2= 'New York', f3= '63', f4= '2010/01/04', f5= '$125,250', )
      db.data0tabletable0.insert( f0= 'Zorita Serrano', f1= 'Software Engineer', f2= 'San Francisco', f3= '56', f4= '2012/06/01', f5= '$115,000', )
      db.data0tabletable0.insert( f0= 'Jennifer Acosta', f1= 'Junior Javascript Developer', f2= 'Edinburgh', f3= '43', f4= '2013/02/01', f5= '$75,650', )
      db.data0tabletable0.insert( f0= 'Cara Stevens', f1= 'Sales Assistant', f2= 'New York', f3= '46', f4= '2011/12/06', f5= '$145,600', )
      db.data0tabletable0.insert( f0= 'Hermione Butler', f1= 'Regional Director', f2= 'London', f3= '47', f4= '2011/03/21', f5= '$356,250', )
      db.data0tabletable0.insert( f0= 'Lael Greer', f1= 'Systems Administrator', f2= 'London', f3= '21', f4= '2009/02/27', f5= '$103,500', )
      db.data0tabletable0.insert( f0= 'Jonas Alexander', f1= 'Developer', f2= 'San Francisco', f3= '30', f4= '2010/07/14', f5= '$86,500', )
      db.data0tabletable0.insert( f0= 'Shad Decker', f1= 'Regional Director', f2= 'Edinburgh', f3= '51', f4= '2008/11/13', f5= '$183,000', )
      db.data0tabletable0.insert( f0= 'Michael Bruce', f1= 'Javascript Developer', f2= 'Singapore', f3= '29', f4= '2011/06/27', f5= '$183,000', )
      db.data0tabletable0.insert( f0= 'Donna Snider', f1= 'Customer Support', f2= 'New York', f3= '27', f4= '2011/01/25', f5= '$112,000', )
      db.data0tabletable0.insert( f0= 'Name', f1= 'Position', f2= 'Office', f3= 'Age', f4= 'Start date', f5= 'Salary', )
db.define_table('analyticstable0',
   Field( 'f0', 'string', label= 'Search Engine', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'Visitors', default= 'w2p f1' ), 
      )
if not db(db.analyticstable0.id ).count():
      db.analyticstable0.insert( f0= '00 analyticstable0', f1= '0w2p1 Visitors', )
      db.analyticstable0.insert( f0= 'Google', f1= '3831', )
      db.analyticstable0.insert( f0= 'Bing', f1= '2123', )
      db.analyticstable0.insert( f0= 'Baidu', f1= '4375', )
      db.analyticstable0.insert( f0= 'Yahoo', f1= '4020', )
      db.analyticstable0.insert( f0= 'DuckDuckGo', f1= '2064', )
      db.analyticstable0.insert( f0= 'Yandex', f1= '936', )
db.define_table('analyticstable1',
   Field( 'f0', 'string', label= 'Website', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'Visitors', default= 'w2p f1' ), 
      )
if not db(db.analyticstable1.id ).count():
      db.analyticstable1.insert( f0= '00 analyticstable1', f1= '0w2p1 Visitors', )
      db.analyticstable1.insert( f0= 'themeforest.net', f1= '620', )
      db.analyticstable1.insert( f0= 'codecanyon.net', f1= '432', )
      db.analyticstable1.insert( f0= 'google.com', f1= '8702', )
      db.analyticstable1.insert( f0= 'yahoo.com', f1= '683', )
      db.analyticstable1.insert( f0= 'youtube.com', f1= '253', )
      db.analyticstable1.insert( f0= 'bing.com', f1= '3018', )
db.define_table('analyticstable2',
   Field( 'f0', 'string', label= 'Work Flow', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'Counter', default= 'w2p f1' ), 
      )
if not db(db.analyticstable2.id ).count():
      db.analyticstable2.insert( f0= '00 analyticstable2', f1= '0w2p1 Counter', )
      db.analyticstable2.insert( f0= 'External Backlinks', f1= '54,302', )
      db.analyticstable2.insert( f0= 'Page Speed Score', f1= '87', )
      db.analyticstable2.insert( f0= 'Citation Flow', f1= '987', )
      db.analyticstable2.insert( f0= 'Mozrank', f1= '9.43', )
      db.analyticstable2.insert( f0= 'Domain Authority', f1= '455', )
      db.analyticstable2.insert( f0= 'Alexa Rank', f1= '342,234', )