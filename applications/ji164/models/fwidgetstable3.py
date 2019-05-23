
db.define_table('peitytable0',
   Field( 'f0', 'string',  label= 'Graph', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Code', default= 'w2p f1' ), 
      )
if not db(db.peitytable0.id ).count():
      db.peitytable0.insert( f0= '00 peitytable0', f1= '0w2p1 Code', )
      db.peitytable0.insert( f0= '1/6', f1= '<span class= pie >1/6</span>', )
      db.peitytable0.insert( f0= '230/360', f1= '<span class= pie >230/360</span>', )
      db.peitytable0.insert( f0= '0.42/1.461', f1= '<span class= pie >0.42/1.461</span>', )
      db.peitytable0.insert( f0= '2,7', f1= '<span class= pie >2,7</span>', )
      db.peitytable0.insert( f0= '236,133', f1= '<span class= pie >236,133</span>', )
      db.peitytable0.insert( f0= '0.42,1.051', f1= '<span class= pie >0.42,1.051</span>', )
db.define_table('peitytable1',
   Field( 'f0', 'string',  label= 'Graph', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Code', default= 'w2p f1' ), 
      )
if not db(db.peitytable1.id ).count():
      db.peitytable1.insert( f0= '00 peitytable1', f1= '0w2p1 Code', )
      db.peitytable1.insert( f0= '2,5,9,6,5,9,7,3,5,2,5,3,9,6,5,8,7,8,5,2', f1= '<span class= line >2,5,9,6,5,9,7,3,5,2,5,3,9,6,5,8,7,8,5,2</span>', )
      db.peitytable1.insert( f0= '8,5,2,-1,-3,-2,8,3,5,3', f1= '<span class= line >8,5,2,-1,-3,-2,8,3,5,3</span>', )
      db.peitytable1.insert( f0= '0,-5,-6,-4,-5,-4,-7,-3,-3,-5', f1= '<span class= line >0,-5,-6,-4,-5,-4,-7,-3,-3,-5</span>', )
      db.peitytable1.insert( f0= '5,3,9,6,5,9,7,3,5,2', f1= '<span class= bar >5,3,9,6,5,9,7,3,5,2</span>', )
      db.peitytable1.insert( f0= '5,3,2,-1,-3,-2,2,3,5,2', f1= '<span class= bar >5,3,2,-1,-3,-2,2,3,5,2</span>', )
db.define_table('sparklinetable0',
   Field( 'f0', 'string',  label= 'Graph', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Type', default= 'w2p f1' ), 
      )
if not db(db.sparklinetable0.id ).count():
      db.sparklinetable0.insert( f0= '00 sparklinetable0', f1= '0w2p1 Type', )
      db.sparklinetable0.insert( f0= 'unk_3', f1= 'Inline line chart', )
      db.sparklinetable0.insert( f0= 'unk_4', f1= 'Bar chart', )
      db.sparklinetable0.insert( f0= 'unk_5', f1= 'Bar chart Positive', )
      db.sparklinetable0.insert( f0= 'unk_6', f1= 'Pie chart', )
      db.sparklinetable0.insert( f0= 'unk_7', f1= 'Long inline chart', )
      db.sparklinetable0.insert( f0= 'unk_8', f1= 'Tristate chart', )
      db.sparklinetable0.insert( f0= 'unk_9', f1= 'Discrete chart', )
db.define_table('static0tabletable0',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Username', default= 'w2p f3' ), 
      )
if not db(db.static0tabletable0.id ).count():
      db.static0tabletable0.insert( f0= '00 static0tabletable0', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Username', )
      db.static0tabletable0.insert( f0= '1', f1= 'Mamun', f2= 'Roshid', f3= '@Facebook', )
      db.static0tabletable0.insert( f0= '2', f1= 'Suhag', f2= 'Khan', f3= '@Twitter', )
      db.static0tabletable0.insert( f0= '3', f1= 'Sakil', f2= 'Shak', f3= '@Linkedin', )
db.define_table('static0tabletable1',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Data', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'User', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Value', default= 'w2p f3' ), 
      )
if not db(db.static0tabletable1.id ).count():
      db.static0tabletable1.insert( f0= '00 static0tabletable1', f1= '0w2p1 Data', f2= '0w2p2 User', f3= '0w2p3 Value', )
      db.static0tabletable1.insert( f0= '1', f1= 'unk_0', f2= 'Roshid', f3= '50%', )
      db.static0tabletable1.insert( f0= '2', f1= 'unk_1', f2= 'Khan', f3= '70%', )
      db.static0tabletable1.insert( f0= '3', f1= 'unk_2', f2= 'Shak', f3= '90%', )
db.define_table('static0tabletable2',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Username', default= 'w2p f3' ), 
      )
if not db(db.static0tabletable2.id ).count():
      db.static0tabletable2.insert( f0= '00 static0tabletable2', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Username', )
      db.static0tabletable2.insert( f0= '1', f1= 'Mamun', f2= 'Roshid', f3= '@Facebook', )
      db.static0tabletable2.insert( f0= '2', f1= 'Suhag', f2= 'Khan', f3= '@Twitter', )
      db.static0tabletable2.insert( f0= '3', f1= 'Sakil', f2= 'Shak', f3= '@Linkedin', )
db.define_table('static0tabletable3',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Data', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'User', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Value', default= 'w2p f3' ), 
      )
if not db(db.static0tabletable3.id ).count():
      db.static0tabletable3.insert( f0= '00 static0tabletable3', f1= '0w2p1 Data', f2= '0w2p2 User', f3= '0w2p3 Value', )
      db.static0tabletable3.insert( f0= '1', f1= '1/6', f2= 'Roshid', f3= '55%', )
      db.static0tabletable3.insert( f0= '2', f1= '230/360', f2= 'Khan', f3= '75%', )
      db.static0tabletable3.insert( f0= '3', f1= '2,7', f2= 'Shak', f3= '95%', )
db.define_table('static0tabletable4',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Username', default= 'w2p f3' ), 
      )
if not db(db.static0tabletable4.id ).count():
      db.static0tabletable4.insert( f0= '00 static0tabletable4', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Username', )
      db.static0tabletable4.insert( f0= '1', f1= 'Mamun', f2= 'Roshid', f3= '@Facebook', )
      db.static0tabletable4.insert( f0= '2', f1= 'Suhag', f2= 'Khan', f3= '@Twitter', )
      db.static0tabletable4.insert( f0= '3', f1= 'Sakil', f2= 'Shak', f3= '@Linkedin', )
db.define_table('static0tabletable5',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Data', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'User', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Value', default= 'w2p f3' ), 
      )
if not db(db.static0tabletable5.id ).count():
      db.static0tabletable5.insert( f0= '00 static0tabletable5', f1= '0w2p1 Data', f2= '0w2p2 User', f3= '0w2p3 Value', )
      db.static0tabletable5.insert( f0= '1', f1= '2,5,9,6,5,9,7,3,5,2,5,3,9,6,5,8,7,8,5,2', f2= 'Roshid', f3= '55%', )
      db.static0tabletable5.insert( f0= '2', f1= '8,5,2,-1,-3,-2,8,3,5,3', f2= 'Khan', f3= '75%', )
      db.static0tabletable5.insert( f0= '3', f1= '5,3,9,6,5,9,7,3,5,2', f2= 'Shak', f3= '95%', )
db.define_table('data0tabletable0',
   Field( 'f0', 'string',  label= 'ID', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Product Title', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Stock', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Price', default= 'w2p f3' ), 
   Field( 'f4', 'string',  label= 'Date', default= 'w2p f4' ), 
   Field( 'f5', 'string',  label= 'Status', default= 'w2p f5' ), 
   Field( 'f6', 'string',  label= 'Total Sales', default= 'w2p f6' ), 
   Field( 'f7', 'string',  label= 'Action', default= 'w2p f7' ), 
      )
if not db(db.data0tabletable0.id ).count():
      db.data0tabletable0.insert( f0= '00 data0tabletable0', f1= '0w2p1 Product Title', f2= '0w2p2 Stock', f3= '0w2p3 Price', f4= '0w2p4 Date', f5= '0w2p5 Status', f6= '0w2p6 Total Sales', f7= '0w2p7 Action', )
      db.data0tabletable0.insert( f0= 'unk_11', f1= '1', f2= 'Product Title', f3= 'Out Of Stock', f4= '$54', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_12', )
      db.data0tabletable0.insert( f0= 'unk_13', f1= '2', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_14', )
      db.data0tabletable0.insert( f0= 'unk_15', f1= '3', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_16', )
      db.data0tabletable0.insert( f0= 'unk_17', f1= '4', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_18', )
      db.data0tabletable0.insert( f0= 'unk_19', f1= '5', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_20', )
      db.data0tabletable0.insert( f0= 'unk_21', f1= '6', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_22', )
      db.data0tabletable0.insert( f0= 'unk_23', f1= '7', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_24', )
      db.data0tabletable0.insert( f0= 'unk_25', f1= '8', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_26', )
      db.data0tabletable0.insert( f0= 'unk_27', f1= '9', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_28', )
      db.data0tabletable0.insert( f0= 'unk_29', f1= '10', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_30', )
      db.data0tabletable0.insert( f0= 'unk_31', f1= '11', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_32', )
      db.data0tabletable0.insert( f0= 'unk_33', f1= '12', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_34', )
      db.data0tabletable0.insert( f0= 'unk_35', f1= '13', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_36', )
      db.data0tabletable0.insert( f0= 'unk_37', f1= '14', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_38', )
      db.data0tabletable0.insert( f0= 'unk_39', f1= '15', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_40', )
      db.data0tabletable0.insert( f0= 'unk_41', f1= '16', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_42', )
      db.data0tabletable0.insert( f0= 'unk_43', f1= '17', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_44', )
      db.data0tabletable0.insert( f0= 'unk_45', f1= '18', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_46', )
      db.data0tabletable0.insert( f0= 'unk_47', f1= '19', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_48', )
      db.data0tabletable0.insert( f0= 'unk_49', f1= '20', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_50', )
      db.data0tabletable0.insert( f0= 'unk_51', f1= '21', f2= 'Product Title', f3= 'In Of Stock', f4= '$5', f5= 'Jul 14, 2017', f6= 'Active', f7= '$700', f8= 'unk_52', )
db.define_table('widgetstable0',
   Field( 'f0', 'string',  label= 'Task', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Date', default= 'w2p f1' ), 
      )
if not db(db.widgetstable0.id ).count():
      db.widgetstable0.insert( f0= '00 widgetstable0', f1= '0w2p1 Date', )
      db.widgetstable0.insert( f0= 'Lorem ipsum', f1= 'Jul 14, 2013', )
      db.widgetstable0.insert( f0= 'Lorem ipsum', f1= 'Jul 09, 2015', )
      db.widgetstable0.insert( f0= 'Lorem ipsum', f1= 'Jul 24, 2014', )
db.define_table('widgetstable1',
   Field( 'f0', 'string',  label= 'Task', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Date', default= 'w2p f1' ), 
      )
if not db(db.widgetstable1.id ).count():
      db.widgetstable1.insert( f0= '00 widgetstable1', f1= '0w2p1 Date', )
      db.widgetstable1.insert( f0= 'Lorem ipsum', f1= 'Jul 14, 2013', )
      db.widgetstable1.insert( f0= 'Lorem ipsum', f1= 'Jul 09, 2015', )
      db.widgetstable1.insert( f0= 'Lorem ipsum', f1= 'Jul 24, 2014', )
db.define_table('widgetstable2',
   Field( 'f0', 'string',  label= 'Task', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Date', default= 'w2p f1' ), 
      )
if not db(db.widgetstable2.id ).count():
      db.widgetstable2.insert( f0= '00 widgetstable2', f1= '0w2p1 Date', )
      db.widgetstable2.insert( f0= 'Lorem ipsum', f1= 'Jul 14, 2013', )
      db.widgetstable2.insert( f0= 'Lorem ipsum', f1= 'Jul 09, 2015', )
      db.widgetstable2.insert( f0= 'Lorem ipsum', f1= 'Jul 24, 2014', )
db.define_table('widgetstable3',
   Field( 'f0', 'string',  label= 'Task', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Date', default= 'w2p f1' ), 
      )
if not db(db.widgetstable3.id ).count():
      db.widgetstable3.insert( f0= '00 widgetstable3', f1= '0w2p1 Date', )
      db.widgetstable3.insert( f0= 'Lorem ipsum', f1= 'Jul 14, 2013', )
      db.widgetstable3.insert( f0= 'Lorem ipsum', f1= 'Jul 09, 2015', )
      db.widgetstable3.insert( f0= 'Lorem ipsum', f1= 'Jul 24, 2014', )