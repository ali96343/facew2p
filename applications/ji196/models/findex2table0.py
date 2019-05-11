
db.define_table('indextable0',
   Field( 'f0', 'string', label= 'date', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'order ID', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'name', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'price', default= 'w2p f3' ), 
   Field( 'f4', 'string', label= 'quantity', default= 'w2p f4' ), 
   Field( 'f5', 'string', label= 'total', default= 'w2p f5' ), 
      )
if not db(db.indextable0.id ).count():
      db.indextable0.insert( f0= '00 indextable0', f1= '0w2p1 order ID', f2= '0w2p2 name', f3= '0w2p3 price', f4= '0w2p4 quantity', f5= '0w2p5 total', )
      db.indextable0.insert( f0= '2018-09-29 05:57', f1= '100398', f2= 'iPhone X 64Gb Grey', f3= '$999.00', f4= '1', f5= '$999.00', )
      db.indextable0.insert( f0= '2018-09-28 01:22', f1= '100397', f2= 'Samsung S8 Black', f3= '$756.00', f4= '1', f5= '$756.00', )
      db.indextable0.insert( f0= '2018-09-27 02:12', f1= '100396', f2= 'Game Console Controller', f3= '$22.00', f4= '2', f5= '$44.00', )
      db.indextable0.insert( f0= '2018-09-26 23:06', f1= '100395', f2= 'iPhone X 256Gb Black', f3= '$1199.00', f4= '1', f5= '$1199.00', )
      db.indextable0.insert( f0= '2018-09-25 19:03', f1= '100393', f2= 'USB 3.0 Cable', f3= '$10.00', f4= '3', f5= '$30.00', )
      db.indextable0.insert( f0= '2018-09-29 05:57', f1= '100392', f2= 'Smartwatch 4.0 LTE Wifi', f3= '$199.00', f4= '6', f5= '$1494.00', )
      db.indextable0.insert( f0= '2018-09-24 19:10', f1= '100391', f2= 'Camera C430W 4k', f3= '$699.00', f4= '1', f5= '$699.00', )
      db.indextable0.insert( f0= '2018-09-22 00:43', f1= '100393', f2= 'USB 3.0 Cable', f3= '$10.00', f4= '3', f5= '$30.00', )
db.define_table('tabletable0',
   Field( 'f0', 'string', label= 'date', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'order ID', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'name', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'price', default= 'w2p f3' ), 
   Field( 'f4', 'string', label= 'quantity', default= 'w2p f4' ), 
   Field( 'f5', 'string', label= 'total', default= 'w2p f5' ), 
      )
if not db(db.tabletable0.id ).count():
      db.tabletable0.insert( f0= '00 tabletable0', f1= '0w2p1 order ID', f2= '0w2p2 name', f3= '0w2p3 price', f4= '0w2p4 quantity', f5= '0w2p5 total', )
      db.tabletable0.insert( f0= '2018-09-29 05:57', f1= '100398', f2= 'iPhone X 64Gb Grey', f3= '$999.00', f4= '1', f5= '$999.00', )
      db.tabletable0.insert( f0= '2018-09-28 01:22', f1= '100397', f2= 'Samsung S8 Black', f3= '$756.00', f4= '1', f5= '$756.00', )
      db.tabletable0.insert( f0= '2018-09-27 02:12', f1= '100396', f2= 'Game Console Controller', f3= '$22.00', f4= '2', f5= '$44.00', )
      db.tabletable0.insert( f0= '2018-09-26 23:06', f1= '100395', f2= 'iPhone X 256Gb Black', f3= '$1199.00', f4= '1', f5= '$1199.00', )
      db.tabletable0.insert( f0= '2018-09-25 19:03', f1= '100393', f2= 'USB 3.0 Cable', f3= '$10.00', f4= '3', f5= '$30.00', )
      db.tabletable0.insert( f0= '2018-09-29 05:57', f1= '100392', f2= 'Smartwatch 4.0 LTE Wifi', f3= '$199.00', f4= '6', f5= '$1494.00', )
      db.tabletable0.insert( f0= '2018-09-24 19:10', f1= '100391', f2= 'Camera C430W 4k', f3= '$699.00', f4= '1', f5= '$699.00', )
      db.tabletable0.insert( f0= '2018-09-22 00:43', f1= '100393', f2= 'USB 3.0 Cable', f3= '$10.00', f4= '3', f5= '$30.00', )
db.define_table('index4table0',
   Field( 'f0', 'string', label= 'date', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'type', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'description', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'status', default= 'w2p f3' ), 
   Field( 'f4', 'string', label= 'price', default= 'w2p f4' ), 
      )
if not db(db.index4table0.id ).count():
      db.index4table0.insert( f0= '00 index4table0', f1= '0w2p1 type', f2= '0w2p2 description', f3= '0w2p3 status', f4= '0w2p4 price', )
      db.index4table0.insert( f0= '2018-09-29 05:57', f1= 'Mobile', f2= 'iPhone X 64Gb Grey', f3= 'Processed', f4= '$999.00', )
      db.index4table0.insert( f0= '2018-09-28 01:22', f1= 'Mobile', f2= 'Samsung S8 Black', f3= 'Processed', f4= '$756.00', )
      db.index4table0.insert( f0= '2018-09-27 02:12', f1= 'Game', f2= 'Game Console Controller', f3= 'Denied', f4= '$22.00', )
      db.index4table0.insert( f0= '2018-09-26 23:06', f1= 'Mobile', f2= 'iPhone X 256Gb Black', f3= 'Denied', f4= '$1199.00', )
      db.index4table0.insert( f0= '2018-09-25 19:03', f1= 'Accessories', f2= 'USB 3.0 Cable', f3= 'Processed', f4= '$10.00', )
      db.index4table0.insert( f0= '2018-09-29 05:57', f1= 'Accesories', f2= 'Smartwatch 4.0 LTE Wifi', f3= 'Denied', f4= '$199.00', )
      db.index4table0.insert( f0= '2018-09-24 19:10', f1= 'Camera', f2= 'Camera C430W 4k', f3= 'Processed', f4= '$699.00', )
      db.index4table0.insert( f0= '2018-09-22 00:43', f1= 'Computer', f2= 'Macbook Pro Retina 2017', f3= 'Processed', f4= '$10.00', )
db.define_table('switchtable0',
   Field( 'f0', 'string', label= 'Size', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'Example', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'CSS Class', default= 'w2p f2' ), 
      )
if not db(db.switchtable0.id ).count():
      db.switchtable0.insert( f0= '00 switchtable0', f1= '0w2p1 Example', f2= '0w2p2 CSS Class', )
      db.switchtable0.insert( f0= 'Large', f1= 'unk_0', f2= 'Add following code size= lg', )
      db.switchtable0.insert( f0= 'Default', f1= 'unk_1', f2= 'unk_2', )
      db.switchtable0.insert( f0= 'Small', f1= 'unk_3', f2= 'Add following code size= sm', )
      db.switchtable0.insert( f0= 'Extra small', f1= 'unk_4', f2= 'Add following code size= xs', )
db.define_table('index2table0',
   Field( 'f0', 'string', label= 'name', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'role', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'type', default= 'w2p f2' ), 
      )
if not db(db.index2table0.id ).count():
      db.index2table0.insert( f0= '00 index2table0', f1= '0w2p1 role', f2= '0w2p2 type', )
      db.index2table0.insert( f0= 'unk_7', f1= 'lori lynch johndoe@gmail.com', f2= 'admin', f3= 'Full Control Post Watch', f4= 'unk_8', )
      db.index2table0.insert( f0= 'unk_9', f1= 'lori lynch johndoe@gmail.com', f2= 'user', f3= 'Full Control Post Watch', f4= 'unk_10', )
      db.index2table0.insert( f0= 'unk_11', f1= 'lori lynch johndoe@gmail.com', f2= 'user', f3= 'Full Control Post Watch', f4= 'unk_12', )
      db.index2table0.insert( f0= 'unk_13', f1= 'lori lynch johndoe@gmail.com', f2= 'member', f3= 'Full Control Post Watch', f4= 'unk_14', )