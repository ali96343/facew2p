
db.define_table('dashboardtable0',
   Field( 'f0', 'string', label= 'Country', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'Visit', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Time', default= 'w2p f2' ), 
      )
if not db(db.dashboardtable0.id ).count():
      db.dashboardtable0.insert( f0= '00 dashboardtable0', f1= '0w2p1 Visit', f2= '0w2p2 Time', )
      db.dashboardtable0.insert( f0= 'Andorra', f1= '1126', f2= '00:00:15', )
      db.dashboardtable0.insert( f0= 'Belarus', f1= '350', f2= '00:01:20', )
      db.dashboardtable0.insert( f0= 'Paraguay', f1= '43', f2= '00:00:30', )
      db.dashboardtable0.insert( f0= 'Malta', f1= '547', f2= '00:10:20', )
      db.dashboardtable0.insert( f0= 'Australia', f1= '560', f2= '00:00:10', )
      db.dashboardtable0.insert( f0= 'Kenya', f1= '97', f2= '00:20:00', )
      db.dashboardtable0.insert( f0= 'Italy', f1= '2450', f2= '00:10:00', )
db.define_table('tabletable0',
   Field( 'f0', 'integer', label= 'Rendering engine', default= 0 ), 
   Field( 'f1', 'boolean', label= 'Browser' , default= True), 
   Field( 'f2', 'double', label= 'Platform(s)', default= 0.0 ), 
   Field( 'f3', 'datetime', label= 'Engine version', default = request.now, requires = IS_DATETIME(format=T('%d.%m.%Y %H:%M:%S') )), 
   Field( 'f4', 'date', label= 'CSS grade', default = request.now, requires = IS_DATE(format=('%d.%m.%Y')),  ), 
      )
if not db(db.tabletable0.id ).count():
         from gluon.contrib.populate import populate
         populate(db.tabletable0  , 58) 

db.define_table('tabletable1',
   Field( 'f0', 'string', label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'Score', default= 'w2p f3' ), 
      )
if not db(db.tabletable1.id ).count():
      db.tabletable1.insert( f0= '00 tabletable1', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Score', )
      db.tabletable1.insert( f0= '1', f1= 'Jill', f2= 'Smith', f3= '50', )
      db.tabletable1.insert( f0= '2', f1= 'Eve', f2= 'Jackson', f3= '94', )
      db.tabletable1.insert( f0= '3', f1= 'John', f2= 'Doe', f3= '80', )
      db.tabletable1.insert( f0= '4', f1= 'Adam', f2= 'Johnson', f3= '67', )
db.define_table('tabletable2',
   Field( 'f0', 'string', label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'Score', default= 'w2p f3' ), 
      )
if not db(db.tabletable2.id ).count():
      db.tabletable2.insert( f0= '00 tabletable2', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Score', )
      db.tabletable2.insert( f0= '1', f1= 'Jill', f2= 'Smith', f3= '50', )
      db.tabletable2.insert( f0= '2', f1= 'Eve', f2= 'Jackson', f3= '94', )
      db.tabletable2.insert( f0= '3', f1= 'John', f2= 'Doe', f3= '80', )
      db.tabletable2.insert( f0= '4', f1= 'Adam', f2= 'Johnson', f3= '67', )
db.define_table('tabletable3',
   Field( 'f0', 'string', label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'Score', default= 'w2p f3' ), 
      )
if not db(db.tabletable3.id ).count():
      db.tabletable3.insert( f0= '00 tabletable3', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Score', )
      db.tabletable3.insert( f0= '1', f1= 'Jill', f2= 'Smith', f3= '50', )
      db.tabletable3.insert( f0= '2', f1= 'Eve', f2= 'Jackson', f3= '94', )
      db.tabletable3.insert( f0= '3', f1= 'John', f2= 'Doe', f3= '80', )
      db.tabletable3.insert( f0= '4', f1= 'Adam', f2= 'Johnson', f3= '67', )
db.define_table('tabletable4',
   Field( 'f0', 'string', label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'Score', default= 'w2p f3' ), 
      )
if not db(db.tabletable4.id ).count():
      db.tabletable4.insert( f0= '00 tabletable4', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Score', )
      db.tabletable4.insert( f0= '1', f1= 'Jill', f2= 'Smith', f3= '50', )
      db.tabletable4.insert( f0= '2', f1= 'Eve', f2= 'Jackson', f3= '94', )
      db.tabletable4.insert( f0= '3', f1= 'John', f2= 'Doe', f3= '80', )
      db.tabletable4.insert( f0= '4', f1= 'Adam', f2= 'Johnson', f3= '67', )
db.define_table('tabletable5',
   Field( 'f0', 'string', label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'Score', default= 'w2p f3' ), 
      )
if not db(db.tabletable5.id ).count():
      db.tabletable5.insert( f0= '00 tabletable5', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Score', )
      db.tabletable5.insert( f0= '1', f1= 'Jill', f2= 'Smith', f3= '50', )
      db.tabletable5.insert( f0= '2', f1= 'Eve', f2= 'Jackson', f3= '94', )
      db.tabletable5.insert( f0= '3', f1= 'John', f2= 'Doe', f3= '80', )
      db.tabletable5.insert( f0= '4', f1= 'Adam', f2= 'Johnson', f3= '67', )
db.define_table('tabletable6',
   Field( 'f0', 'string', label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string', label= 'Score', default= 'w2p f3' ), 
      )
if not db(db.tabletable6.id ).count():
      db.tabletable6.insert( f0= '00 tabletable6', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Score', )
      db.tabletable6.insert( f0= '1', f1= 'Jill', f2= 'Smith', f3= '50', )
      db.tabletable6.insert( f0= '2', f1= 'Eve', f2= 'Jackson', f3= '94', )
      db.tabletable6.insert( f0= '3', f1= 'John', f2= 'Doe', f3= '80', )
      db.tabletable6.insert( f0= '4', f1= 'Adam', f2= 'Johnson', f3= '67', )
db.define_table('typographytable0',
   Field( 'f0', 'string', label= 'Labels', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'Markup', default= 'w2p f1' ), 
      )
if not db(db.typographytable0.id ).count():
      db.typographytable0.insert( f0= '00 typographytable0', f1= '0w2p1 Markup', )
      db.typographytable0.insert( f0= 'Default', f1= '<span class= label label-default >Default</span>', )
      db.typographytable0.insert( f0= 'Success', f1= '<span class= label label-success >Success</span>', )
      db.typographytable0.insert( f0= 'Warning', f1= '<span class= label label-warning >Warning</span>', )
      db.typographytable0.insert( f0= 'Danger', f1= '<span class= label label-danger >Important</span>', )
      db.typographytable0.insert( f0= 'Info', f1= '<span class= label label-info >Info</span>', )
db.define_table('typographytable1',
   Field( 'f0', 'string', label= 'Name', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'Example', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Markup', default= 'w2p f2' ), 
      )
if not db(db.typographytable1.id ).count():
      db.typographytable1.insert( f0= '00 typographytable1', f1= '0w2p1 Example', f2= '0w2p2 Markup', )
      db.typographytable1.insert( f0= 'Default', f1= '1', f2= '<span class= badge >1</span>', )
db.define_table('alternetable0',
   Field( 'f0', 'string', label= 'Country', default= 'w2p f0' ), 
   Field( 'f1', 'string', label= 'Visit', default= 'w2p f1' ), 
   Field( 'f2', 'string', label= 'Time', default= 'w2p f2' ), 
      )
if not db(db.alternetable0.id ).count():
      db.alternetable0.insert( f0= '00 alternetable0', f1= '0w2p1 Visit', f2= '0w2p2 Time', )
      db.alternetable0.insert( f0= 'Andorra', f1= '1126', f2= '00:00:15', )
      db.alternetable0.insert( f0= 'Belarus', f1= '350', f2= '00:01:20', )
      db.alternetable0.insert( f0= 'Paraguay', f1= '43', f2= '00:00:30', )
      db.alternetable0.insert( f0= 'Malta', f1= '547', f2= '00:10:20', )
      db.alternetable0.insert( f0= 'Australia', f1= '560', f2= '00:00:10', )
      db.alternetable0.insert( f0= 'Kenya', f1= '97', f2= '00:20:00', )
      db.alternetable0.insert( f0= 'Italy', f1= '2450', f2= '00:10:00', )