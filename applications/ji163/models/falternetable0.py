
db.define_table('dashboardtable0',
   Field( 'f0', 'string',  label= 'Country', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Visit', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Time', default= 'w2p f2' ), 
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
   Field( 'f0', 'string',  label= 'Rendering engine', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Browser', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Platform(s)', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Engine version', default= 'w2p f3' ), 
   Field( 'f4', 'string',  label= 'CSS grade', default= 'w2p f4' ), 
      )
if not db(db.tabletable0.id ).count():
      db.tabletable0.insert( f0= '00 tabletable0', f1= '0w2p1 Browser', f2= '0w2p2 Platform(s)', f3= '0w2p3 Engine version', f4= '0w2p4 CSS grade', )
      db.tabletable0.insert( f0= 'Trident', f1= 'Internet Explorer 4.0', f2= 'Win 95+', f3= '4', f4= 'X', )
      db.tabletable0.insert( f0= 'Trident', f1= 'Internet Explorer 5.0', f2= 'Win 95+', f3= '5', f4= 'C', )
      db.tabletable0.insert( f0= 'Trident', f1= 'Internet Explorer 5.5', f2= 'Win 95+', f3= '5.5', f4= 'A', )
      db.tabletable0.insert( f0= 'Trident', f1= 'Internet Explorer 6', f2= 'Win 98+', f3= '6', f4= 'A', )
      db.tabletable0.insert( f0= 'Trident', f1= 'Internet Explorer 7', f2= 'Win XP SP2+', f3= '7', f4= 'A', )
      db.tabletable0.insert( f0= 'Trident', f1= 'AOL browser (AOL desktop)', f2= 'Win XP', f3= '6', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Firefox 1.0', f2= 'Win 98+ / OSX.2+', f3= '1.7', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Firefox 1.5', f2= 'Win 98+ / OSX.2+', f3= '1.8', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Firefox 2.0', f2= 'Win 98+ / OSX.2+', f3= '1.8', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Firefox 3.0', f2= 'Win 2k+ / OSX.3+', f3= '1.9', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Camino 1.0', f2= 'OSX.2+', f3= '1.8', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Camino 1.5', f2= 'OSX.3+', f3= '1.8', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Netscape 7.2', f2= 'Win 95+ / Mac OS 8.6-9.2', f3= '1.7', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Netscape Browser 8', f2= 'Win 98SE+', f3= '1.7', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Netscape Navigator 9', f2= 'Win 98+ / OSX.2+', f3= '1.8', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Mozilla 1.0', f2= 'Win 95+ / OSX.1+', f3= '1', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Mozilla 1.1', f2= 'Win 95+ / OSX.1+', f3= '1.1', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Mozilla 1.2', f2= 'Win 95+ / OSX.1+', f3= '1.2', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Mozilla 1.3', f2= 'Win 95+ / OSX.1+', f3= '1.3', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Mozilla 1.4', f2= 'Win 95+ / OSX.1+', f3= '1.4', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Mozilla 1.5', f2= 'Win 95+ / OSX.1+', f3= '1.5', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Mozilla 1.6', f2= 'Win 95+ / OSX.1+', f3= '1.6', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Mozilla 1.7', f2= 'Win 98+ / OSX.1+', f3= '1.7', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Mozilla 1.8', f2= 'Win 98+ / OSX.1+', f3= '1.8', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Seamonkey 1.1', f2= 'Win 98+ / OSX.2+', f3= '1.8', f4= 'A', )
      db.tabletable0.insert( f0= 'Gecko', f1= 'Epiphany 2.20', f2= 'Gnome', f3= '1.8', f4= 'A', )
      db.tabletable0.insert( f0= 'Webkit', f1= 'Safari 1.2', f2= 'OSX.3', f3= '125.5', f4= 'A', )
      db.tabletable0.insert( f0= 'Webkit', f1= 'Safari 1.3', f2= 'OSX.3', f3= '312.8', f4= 'A', )
      db.tabletable0.insert( f0= 'Webkit', f1= 'Safari 2.0', f2= 'OSX.4+', f3= '419.3', f4= 'A', )
      db.tabletable0.insert( f0= 'Webkit', f1= 'Safari 3.0', f2= 'OSX.4+', f3= '522.1', f4= 'A', )
      db.tabletable0.insert( f0= 'Webkit', f1= 'OmniWeb 5.5', f2= 'OSX.4+', f3= '420', f4= 'A', )
      db.tabletable0.insert( f0= 'Webkit', f1= 'iPod Touch / iPhone', f2= 'iPod', f3= '420.1', f4= 'A', )
      db.tabletable0.insert( f0= 'Webkit', f1= 'S60', f2= 'S60', f3= '413', f4= 'A', )
      db.tabletable0.insert( f0= 'Presto', f1= 'Opera 7.0', f2= 'Win 95+ / OSX.1+', f3= '-', f4= 'A', )
      db.tabletable0.insert( f0= 'Presto', f1= 'Opera 7.5', f2= 'Win 95+ / OSX.2+', f3= '-', f4= 'A', )
      db.tabletable0.insert( f0= 'Presto', f1= 'Opera 8.0', f2= 'Win 95+ / OSX.2+', f3= '-', f4= 'A', )
      db.tabletable0.insert( f0= 'Presto', f1= 'Opera 8.5', f2= 'Win 95+ / OSX.2+', f3= '-', f4= 'A', )
      db.tabletable0.insert( f0= 'Presto', f1= 'Opera 9.0', f2= 'Win 95+ / OSX.3+', f3= '-', f4= 'A', )
      db.tabletable0.insert( f0= 'Presto', f1= 'Opera 9.2', f2= 'Win 88+ / OSX.3+', f3= '-', f4= 'A', )
      db.tabletable0.insert( f0= 'Presto', f1= 'Opera 9.5', f2= 'Win 88+ / OSX.3+', f3= '-', f4= 'A', )
      db.tabletable0.insert( f0= 'Presto', f1= 'Opera for Wii', f2= 'Wii', f3= '-', f4= 'A', )
      db.tabletable0.insert( f0= 'Presto', f1= 'Nokia N800', f2= 'N800', f3= '-', f4= 'A', )
      db.tabletable0.insert( f0= 'Presto', f1= 'Nintendo DS browser', f2= 'Nintendo DS', f3= '8.5', f4= 'C/A1', )
      db.tabletable0.insert( f0= 'KHTML', f1= 'Konqureror 3.1', f2= 'KDE 3.1', f3= '3.1', f4= 'C', )
      db.tabletable0.insert( f0= 'KHTML', f1= 'Konqureror 3.3', f2= 'KDE 3.3', f3= '3.3', f4= 'A', )
      db.tabletable0.insert( f0= 'KHTML', f1= 'Konqureror 3.5', f2= 'KDE 3.5', f3= '3.5', f4= 'A', )
      db.tabletable0.insert( f0= 'Tasman', f1= 'Internet Explorer 4.5', f2= 'Mac OS 8-9', f3= '-', f4= 'X', )
      db.tabletable0.insert( f0= 'Tasman', f1= 'Internet Explorer 5.1', f2= 'Mac OS 7.6-9', f3= '1', f4= 'C', )
      db.tabletable0.insert( f0= 'Tasman', f1= 'Internet Explorer 5.2', f2= 'Mac OS 8-X', f3= '1', f4= 'C', )
      db.tabletable0.insert( f0= 'Misc', f1= 'NetFront 3.1', f2= 'Embedded devices', f3= '-', f4= 'C', )
      db.tabletable0.insert( f0= 'Misc', f1= 'NetFront 3.4', f2= 'Embedded devices', f3= '-', f4= 'A', )
      db.tabletable0.insert( f0= 'Misc', f1= 'Dillo 0.8', f2= 'Embedded devices', f3= '-', f4= 'X', )
      db.tabletable0.insert( f0= 'Misc', f1= 'Links', f2= 'Text only', f3= '-', f4= 'X', )
      db.tabletable0.insert( f0= 'Misc', f1= 'Lynx', f2= 'Text only', f3= '-', f4= 'X', )
      db.tabletable0.insert( f0= 'Misc', f1= 'IE Mobile', f2= 'Windows Mobile 6', f3= '-', f4= 'C', )
      db.tabletable0.insert( f0= 'Misc', f1= 'PSP browser', f2= 'PSP', f3= '-', f4= 'C', )
      db.tabletable0.insert( f0= 'Other browsers', f1= 'All others', f2= '-', f3= '-', f4= 'U', )
db.define_table('tabletable1',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Score', default= 'w2p f3' ), 
      )
if not db(db.tabletable1.id ).count():
      db.tabletable1.insert( f0= '00 tabletable1', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Score', )
      db.tabletable1.insert( f0= '1', f1= 'Jill', f2= 'Smith', f3= '50', )
      db.tabletable1.insert( f0= '2', f1= 'Eve', f2= 'Jackson', f3= '94', )
      db.tabletable1.insert( f0= '3', f1= 'John', f2= 'Doe', f3= '80', )
      db.tabletable1.insert( f0= '4', f1= 'Adam', f2= 'Johnson', f3= '67', )
db.define_table('tabletable2',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Score', default= 'w2p f3' ), 
      )
if not db(db.tabletable2.id ).count():
      db.tabletable2.insert( f0= '00 tabletable2', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Score', )
      db.tabletable2.insert( f0= '1', f1= 'Jill', f2= 'Smith', f3= '50', )
      db.tabletable2.insert( f0= '2', f1= 'Eve', f2= 'Jackson', f3= '94', )
      db.tabletable2.insert( f0= '3', f1= 'John', f2= 'Doe', f3= '80', )
      db.tabletable2.insert( f0= '4', f1= 'Adam', f2= 'Johnson', f3= '67', )
db.define_table('tabletable3',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Score', default= 'w2p f3' ), 
      )
if not db(db.tabletable3.id ).count():
      db.tabletable3.insert( f0= '00 tabletable3', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Score', )
      db.tabletable3.insert( f0= '1', f1= 'Jill', f2= 'Smith', f3= '50', )
      db.tabletable3.insert( f0= '2', f1= 'Eve', f2= 'Jackson', f3= '94', )
      db.tabletable3.insert( f0= '3', f1= 'John', f2= 'Doe', f3= '80', )
      db.tabletable3.insert( f0= '4', f1= 'Adam', f2= 'Johnson', f3= '67', )
db.define_table('tabletable4',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Score', default= 'w2p f3' ), 
      )
if not db(db.tabletable4.id ).count():
      db.tabletable4.insert( f0= '00 tabletable4', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Score', )
      db.tabletable4.insert( f0= '1', f1= 'Jill', f2= 'Smith', f3= '50', )
      db.tabletable4.insert( f0= '2', f1= 'Eve', f2= 'Jackson', f3= '94', )
      db.tabletable4.insert( f0= '3', f1= 'John', f2= 'Doe', f3= '80', )
      db.tabletable4.insert( f0= '4', f1= 'Adam', f2= 'Johnson', f3= '67', )
db.define_table('tabletable5',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Score', default= 'w2p f3' ), 
      )
if not db(db.tabletable5.id ).count():
      db.tabletable5.insert( f0= '00 tabletable5', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Score', )
      db.tabletable5.insert( f0= '1', f1= 'Jill', f2= 'Smith', f3= '50', )
      db.tabletable5.insert( f0= '2', f1= 'Eve', f2= 'Jackson', f3= '94', )
      db.tabletable5.insert( f0= '3', f1= 'John', f2= 'Doe', f3= '80', )
      db.tabletable5.insert( f0= '4', f1= 'Adam', f2= 'Johnson', f3= '67', )
db.define_table('tabletable6',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'First Name', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Last Name', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Score', default= 'w2p f3' ), 
      )
if not db(db.tabletable6.id ).count():
      db.tabletable6.insert( f0= '00 tabletable6', f1= '0w2p1 First Name', f2= '0w2p2 Last Name', f3= '0w2p3 Score', )
      db.tabletable6.insert( f0= '1', f1= 'Jill', f2= 'Smith', f3= '50', )
      db.tabletable6.insert( f0= '2', f1= 'Eve', f2= 'Jackson', f3= '94', )
      db.tabletable6.insert( f0= '3', f1= 'John', f2= 'Doe', f3= '80', )
      db.tabletable6.insert( f0= '4', f1= 'Adam', f2= 'Johnson', f3= '67', )
db.define_table('typographytable0',
   Field( 'f0', 'string',  label= 'Labels', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Markup', default= 'w2p f1' ), 
      )
if not db(db.typographytable0.id ).count():
      db.typographytable0.insert( f0= '00 typographytable0', f1= '0w2p1 Markup', )
      db.typographytable0.insert( f0= 'Default', f1= '<span class= label label-default >Default</span>', )
      db.typographytable0.insert( f0= 'Success', f1= '<span class= label label-success >Success</span>', )
      db.typographytable0.insert( f0= 'Warning', f1= '<span class= label label-warning >Warning</span>', )
      db.typographytable0.insert( f0= 'Danger', f1= '<span class= label label-danger >Important</span>', )
      db.typographytable0.insert( f0= 'Info', f1= '<span class= label label-info >Info</span>', )
db.define_table('typographytable1',
   Field( 'f0', 'string',  label= 'Name', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Example', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Markup', default= 'w2p f2' ), 
      )
if not db(db.typographytable1.id ).count():
      db.typographytable1.insert( f0= '00 typographytable1', f1= '0w2p1 Example', f2= '0w2p2 Markup', )
      db.typographytable1.insert( f0= 'Default', f1= '1', f2= '<span class= badge >1</span>', )
db.define_table('alternetable0',
   Field( 'f0', 'string',  label= 'Country', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Visit', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Time', default= 'w2p f2' ), 
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