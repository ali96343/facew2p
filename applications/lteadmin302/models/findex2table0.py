
db.define_table('project_edittable0',
   Field( 'f0', 'string',  label= 'File Name', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'File Size', default= 'w2p f1' ), 
      )
if not db(db.project_edittable0.id ).count():
      db.project_edittable0.insert( f0= '00 project_edittable0', f1= '0w2p1 File Size', )
      db.project_edittable0.insert( f0= 'Functional-requirements.docx', f1= '49.8005 kb', f2= 'unk_17', )
      db.project_edittable0.insert( f0= 'UAT.pdf', f1= '28.4883 kb', f2= 'unk_18', )
      db.project_edittable0.insert( f0= 'Email-from-flatbal.mln', f1= '57.9003 kb', f2= 'unk_19', )
      db.project_edittable0.insert( f0= 'Logo.png', f1= '50.5190 kb', f2= 'unk_20', )
      db.project_edittable0.insert( f0= 'Contract-10_12_2014.docx', f1= '44.9715 kb', f2= 'unk_21', )
db.define_table('index3table0',
   Field( 'f0', 'string',  label= 'Product', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Price', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Sales', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'More', default= 'w2p f3' ), 
      )
if not db(db.index3table0.id ).count():
      db.index3table0.insert( f0= '00 index3table0', f1= '0w2p1 Price', f2= '0w2p2 Sales', f3= '0w2p3 More', )
      db.index3table0.insert( f0= 'Some Product', f1= '$13 USD', f2= '12% 12,000 Sold', f3= 'unk_40', )
      db.index3table0.insert( f0= 'Another Product', f1= '$29 USD', f2= '0.5% 123,234 Sold', f3= 'unk_41', )
      db.index3table0.insert( f0= 'Amazing Product', f1= '$1,230 USD', f2= '3% 198 Sold', f3= 'unk_42', )
      db.index3table0.insert( f0= 'Perfect Item NEW', f1= '$199 USD', f2= '63% 87 Sold', f3= 'unk_43', )
db.define_table('simpletable0',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Task', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Progress', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Label', default= 'w2p f3' ), 
      )
if not db(db.simpletable0.id ).count():
      db.simpletable0.insert( f0= '00 simpletable0', f1= '0w2p1 Task', f2= '0w2p2 Progress', f3= '0w2p3 Label', )
      db.simpletable0.insert( f0= '1.', f1= 'Update software', f2= 'unk_0', f3= '55%', )
      db.simpletable0.insert( f0= '2.', f1= 'Clean database', f2= 'unk_1', f3= '70%', )
      db.simpletable0.insert( f0= '3.', f1= 'Cron job running', f2= 'unk_2', f3= '30%', )
      db.simpletable0.insert( f0= '4.', f1= 'Fix and squish bugs', f2= 'unk_3', f3= '90%', )
db.define_table('simpletable1',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Task', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Progress', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Label', default= 'w2p f3' ), 
      )
if not db(db.simpletable1.id ).count():
      db.simpletable1.insert( f0= '00 simpletable1', f1= '0w2p1 Task', f2= '0w2p2 Progress', f3= '0w2p3 Label', )
      db.simpletable1.insert( f0= '1.', f1= 'Update software', f2= 'unk_4', f3= '55%', )
      db.simpletable1.insert( f0= '2.', f1= 'Clean database', f2= 'unk_5', f3= '70%', )
      db.simpletable1.insert( f0= '3.', f1= 'Cron job running', f2= 'unk_6', f3= '30%', )
      db.simpletable1.insert( f0= '4.', f1= 'Fix and squish bugs', f2= 'unk_7', f3= '90%', )
db.define_table('simpletable2',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Task', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Progress', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Label', default= 'w2p f3' ), 
      )
if not db(db.simpletable2.id ).count():
      db.simpletable2.insert( f0= '00 simpletable2', f1= '0w2p1 Task', f2= '0w2p2 Progress', f3= '0w2p3 Label', )
      db.simpletable2.insert( f0= '1.', f1= 'Update software', f2= 'unk_8', f3= '55%', )
      db.simpletable2.insert( f0= '2.', f1= 'Clean database', f2= 'unk_9', f3= '70%', )
      db.simpletable2.insert( f0= '3.', f1= 'Cron job running', f2= 'unk_10', f3= '30%', )
      db.simpletable2.insert( f0= '4.', f1= 'Fix and squish bugs', f2= 'unk_11', f3= '90%', )
db.define_table('simpletable3',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Task', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Progress', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Label', default= 'w2p f3' ), 
      )
if not db(db.simpletable3.id ).count():
      db.simpletable3.insert( f0= '00 simpletable3', f1= '0w2p1 Task', f2= '0w2p2 Progress', f3= '0w2p3 Label', )
      db.simpletable3.insert( f0= '1.', f1= 'Update software', f2= 'unk_12', f3= '55%', )
      db.simpletable3.insert( f0= '2.', f1= 'Clean database', f2= 'unk_13', f3= '70%', )
      db.simpletable3.insert( f0= '3.', f1= 'Cron job running', f2= 'unk_14', f3= '30%', )
      db.simpletable3.insert( f0= '4.', f1= 'Fix and squish bugs', f2= 'unk_15', f3= '90%', )
db.define_table('simpletable4',
   Field( 'f0', 'string',  label= 'ID', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'User', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Date', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Status', default= 'w2p f3' ), 
   Field( 'f4', 'string',  label= 'Reason', default= 'w2p f4' ), 
      )
if not db(db.simpletable4.id ).count():
      db.simpletable4.insert( f0= '00 simpletable4', f1= '0w2p1 User', f2= '0w2p2 Date', f3= '0w2p3 Status', f4= '0w2p4 Reason', )
      db.simpletable4.insert( f0= '183', f1= 'John Doe', f2= '11-7-2014', f3= 'Approved', f4= 'Bacon ipsum dolor sit amet salami venison chicken flank fatback doner.', )
      db.simpletable4.insert( f0= '219', f1= 'Alexander Pierce', f2= '11-7-2014', f3= 'Pending', f4= 'Bacon ipsum dolor sit amet salami venison chicken flank fatback doner.', )
      db.simpletable4.insert( f0= '657', f1= 'Bob Doe', f2= '11-7-2014', f3= 'Approved', f4= 'Bacon ipsum dolor sit amet salami venison chicken flank fatback doner.', )
      db.simpletable4.insert( f0= '175', f1= 'Mike Doe', f2= '11-7-2014', f3= 'Denied', f4= 'Bacon ipsum dolor sit amet salami venison chicken flank fatback doner.', )
db.define_table('simpletable5',
   Field( 'f0', 'string',  label= 'ID', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'User', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Date', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Status', default= 'w2p f3' ), 
   Field( 'f4', 'string',  label= 'Reason', default= 'w2p f4' ), 
      )
if not db(db.simpletable5.id ).count():
      db.simpletable5.insert( f0= '00 simpletable5', f1= '0w2p1 User', f2= '0w2p2 Date', f3= '0w2p3 Status', f4= '0w2p4 Reason', )
      db.simpletable5.insert( f0= '183', f1= 'John Doe', f2= '11-7-2014', f3= 'Approved', f4= 'Bacon ipsum dolor sit amet salami venison chicken flank fatback doner.', )
      db.simpletable5.insert( f0= '219', f1= 'Alexander Pierce', f2= '11-7-2014', f3= 'Pending', f4= 'Bacon ipsum dolor sit amet salami venison chicken flank fatback doner.', )
      db.simpletable5.insert( f0= '657', f1= 'Bob Doe', f2= '11-7-2014', f3= 'Approved', f4= 'Bacon ipsum dolor sit amet salami venison chicken flank fatback doner.', )
      db.simpletable5.insert( f0= '175', f1= 'Mike Doe', f2= '11-7-2014', f3= 'Denied', f4= 'Bacon ipsum dolor sit amet salami venison chicken flank fatback doner.', )
      db.simpletable5.insert( f0= '134', f1= 'Jim Doe', f2= '11-7-2014', f3= 'Approved', f4= 'Bacon ipsum dolor sit amet salami venison chicken flank fatback doner.', )
      db.simpletable5.insert( f0= '494', f1= 'Victoria Doe', f2= '11-7-2014', f3= 'Pending', f4= 'Bacon ipsum dolor sit amet salami venison chicken flank fatback doner.', )
      db.simpletable5.insert( f0= '832', f1= 'Michael Doe', f2= '11-7-2014', f3= 'Approved', f4= 'Bacon ipsum dolor sit amet salami venison chicken flank fatback doner.', )
      db.simpletable5.insert( f0= '982', f1= 'Rocky Doe', f2= '11-7-2014', f3= 'Denied', f4= 'Bacon ipsum dolor sit amet salami venison chicken flank fatback doner.', )
db.define_table('datatable0',
   Field( 'f0', 'string',  label= 'Rendering engine', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Browser', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Platform(s)', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Engine version', default= 'w2p f3' ), 
   Field( 'f4', 'string',  label= 'CSS grade', default= 'w2p f4' ), 
      )
if not db(db.datatable0.id ).count():
      db.datatable0.insert( f0= '00 datatable0', f1= '0w2p1 Browser', f2= '0w2p2 Platform(s)', f3= '0w2p3 Engine version', f4= '0w2p4 CSS grade', )
      db.datatable0.insert( f0= 'Trident', f1= 'Internet Explorer 4.0', f2= 'Win 95+', f3= '4', f4= 'X', )
      db.datatable0.insert( f0= 'Trident', f1= 'Internet Explorer 5.0', f2= 'Win 95+', f3= '5', f4= 'C', )
      db.datatable0.insert( f0= 'Trident', f1= 'Internet Explorer 5.5', f2= 'Win 95+', f3= '5.5', f4= 'A', )
      db.datatable0.insert( f0= 'Trident', f1= 'Internet Explorer 6', f2= 'Win 98+', f3= '6', f4= 'A', )
      db.datatable0.insert( f0= 'Trident', f1= 'Internet Explorer 7', f2= 'Win XP SP2+', f3= '7', f4= 'A', )
      db.datatable0.insert( f0= 'Trident', f1= 'AOL browser (AOL desktop)', f2= 'Win XP', f3= '6', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Firefox 1.0', f2= 'Win 98+ / OSX.2+', f3= '1.7', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Firefox 1.5', f2= 'Win 98+ / OSX.2+', f3= '1.8', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Firefox 2.0', f2= 'Win 98+ / OSX.2+', f3= '1.8', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Firefox 3.0', f2= 'Win 2k+ / OSX.3+', f3= '1.9', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Camino 1.0', f2= 'OSX.2+', f3= '1.8', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Camino 1.5', f2= 'OSX.3+', f3= '1.8', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Netscape 7.2', f2= 'Win 95+ / Mac OS 8.6-9.2', f3= '1.7', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Netscape Browser 8', f2= 'Win 98SE+', f3= '1.7', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Netscape Navigator 9', f2= 'Win 98+ / OSX.2+', f3= '1.8', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Mozilla 1.0', f2= 'Win 95+ / OSX.1+', f3= '1', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Mozilla 1.1', f2= 'Win 95+ / OSX.1+', f3= '1.1', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Mozilla 1.2', f2= 'Win 95+ / OSX.1+', f3= '1.2', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Mozilla 1.3', f2= 'Win 95+ / OSX.1+', f3= '1.3', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Mozilla 1.4', f2= 'Win 95+ / OSX.1+', f3= '1.4', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Mozilla 1.5', f2= 'Win 95+ / OSX.1+', f3= '1.5', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Mozilla 1.6', f2= 'Win 95+ / OSX.1+', f3= '1.6', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Mozilla 1.7', f2= 'Win 98+ / OSX.1+', f3= '1.7', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Mozilla 1.8', f2= 'Win 98+ / OSX.1+', f3= '1.8', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Seamonkey 1.1', f2= 'Win 98+ / OSX.2+', f3= '1.8', f4= 'A', )
      db.datatable0.insert( f0= 'Gecko', f1= 'Epiphany 2.20', f2= 'Gnome', f3= '1.8', f4= 'A', )
      db.datatable0.insert( f0= 'Webkit', f1= 'Safari 1.2', f2= 'OSX.3', f3= '125.5', f4= 'A', )
      db.datatable0.insert( f0= 'Webkit', f1= 'Safari 1.3', f2= 'OSX.3', f3= '312.8', f4= 'A', )
      db.datatable0.insert( f0= 'Webkit', f1= 'Safari 2.0', f2= 'OSX.4+', f3= '419.3', f4= 'A', )
      db.datatable0.insert( f0= 'Webkit', f1= 'Safari 3.0', f2= 'OSX.4+', f3= '522.1', f4= 'A', )
      db.datatable0.insert( f0= 'Webkit', f1= 'OmniWeb 5.5', f2= 'OSX.4+', f3= '420', f4= 'A', )
      db.datatable0.insert( f0= 'Webkit', f1= 'iPod Touch / iPhone', f2= 'iPod', f3= '420.1', f4= 'A', )
      db.datatable0.insert( f0= 'Webkit', f1= 'S60', f2= 'S60', f3= '413', f4= 'A', )
      db.datatable0.insert( f0= 'Presto', f1= 'Opera 7.0', f2= 'Win 95+ / OSX.1+', f3= '-', f4= 'A', )
      db.datatable0.insert( f0= 'Presto', f1= 'Opera 7.5', f2= 'Win 95+ / OSX.2+', f3= '-', f4= 'A', )
      db.datatable0.insert( f0= 'Presto', f1= 'Opera 8.0', f2= 'Win 95+ / OSX.2+', f3= '-', f4= 'A', )
      db.datatable0.insert( f0= 'Presto', f1= 'Opera 8.5', f2= 'Win 95+ / OSX.2+', f3= '-', f4= 'A', )
      db.datatable0.insert( f0= 'Presto', f1= 'Opera 9.0', f2= 'Win 95+ / OSX.3+', f3= '-', f4= 'A', )
      db.datatable0.insert( f0= 'Presto', f1= 'Opera 9.2', f2= 'Win 88+ / OSX.3+', f3= '-', f4= 'A', )
      db.datatable0.insert( f0= 'Presto', f1= 'Opera 9.5', f2= 'Win 88+ / OSX.3+', f3= '-', f4= 'A', )
      db.datatable0.insert( f0= 'Presto', f1= 'Opera for Wii', f2= 'Wii', f3= '-', f4= 'A', )
      db.datatable0.insert( f0= 'Presto', f1= 'Nokia N800', f2= 'N800', f3= '-', f4= 'A', )
      db.datatable0.insert( f0= 'Presto', f1= 'Nintendo DS browser', f2= 'Nintendo DS', f3= '8.5', f4= 'C/A1', )
      db.datatable0.insert( f0= 'KHTML', f1= 'Konqureror 3.1', f2= 'KDE 3.1', f3= '3.1', f4= 'C', )
      db.datatable0.insert( f0= 'KHTML', f1= 'Konqureror 3.3', f2= 'KDE 3.3', f3= '3.3', f4= 'A', )
      db.datatable0.insert( f0= 'KHTML', f1= 'Konqureror 3.5', f2= 'KDE 3.5', f3= '3.5', f4= 'A', )
      db.datatable0.insert( f0= 'Tasman', f1= 'Internet Explorer 4.5', f2= 'Mac OS 8-9', f3= '-', f4= 'X', )
      db.datatable0.insert( f0= 'Tasman', f1= 'Internet Explorer 5.1', f2= 'Mac OS 7.6-9', f3= '1', f4= 'C', )
      db.datatable0.insert( f0= 'Tasman', f1= 'Internet Explorer 5.2', f2= 'Mac OS 8-X', f3= '1', f4= 'C', )
      db.datatable0.insert( f0= 'Misc', f1= 'NetFront 3.1', f2= 'Embedded devices', f3= '-', f4= 'C', )
      db.datatable0.insert( f0= 'Misc', f1= 'NetFront 3.4', f2= 'Embedded devices', f3= '-', f4= 'A', )
      db.datatable0.insert( f0= 'Misc', f1= 'Dillo 0.8', f2= 'Embedded devices', f3= '-', f4= 'X', )
      db.datatable0.insert( f0= 'Misc', f1= 'Links', f2= 'Text only', f3= '-', f4= 'X', )
      db.datatable0.insert( f0= 'Misc', f1= 'Lynx', f2= 'Text only', f3= '-', f4= 'X', )
      db.datatable0.insert( f0= 'Misc', f1= 'IE Mobile', f2= 'Windows Mobile 6', f3= '-', f4= 'C', )
      db.datatable0.insert( f0= 'Misc', f1= 'PSP browser', f2= 'PSP', f3= '-', f4= 'C', )
      db.datatable0.insert( f0= 'Other browsers', f1= 'All others', f2= '-', f3= '-', f4= 'U', )
      db.datatable0.insert( f0= 'Rendering engine', f1= 'Browser', f2= 'Platform(s)', f3= 'Engine version', f4= 'CSS grade', )
db.define_table('datatable1',
   Field( 'f0', 'string',  label= 'Rendering engine', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Browser', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Platform(s)', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Engine version', default= 'w2p f3' ), 
   Field( 'f4', 'string',  label= 'CSS grade', default= 'w2p f4' ), 
      )
if not db(db.datatable1.id ).count():
      db.datatable1.insert( f0= '00 datatable1', f1= '0w2p1 Browser', f2= '0w2p2 Platform(s)', f3= '0w2p3 Engine version', f4= '0w2p4 CSS grade', )
      db.datatable1.insert( f0= 'Trident', f1= 'Internet Explorer 4.0', f2= 'Win 95+', f3= '4', f4= 'X', )
      db.datatable1.insert( f0= 'Trident', f1= 'Internet Explorer 5.0', f2= 'Win 95+', f3= '5', f4= 'C', )
      db.datatable1.insert( f0= 'Trident', f1= 'Internet Explorer 5.5', f2= 'Win 95+', f3= '5.5', f4= 'A', )
      db.datatable1.insert( f0= 'Trident', f1= 'Internet Explorer 6', f2= 'Win 98+', f3= '6', f4= 'A', )
      db.datatable1.insert( f0= 'Trident', f1= 'Internet Explorer 7', f2= 'Win XP SP2+', f3= '7', f4= 'A', )
      db.datatable1.insert( f0= 'Trident', f1= 'AOL browser (AOL desktop)', f2= 'Win XP', f3= '6', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Firefox 1.0', f2= 'Win 98+ / OSX.2+', f3= '1.7', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Firefox 1.5', f2= 'Win 98+ / OSX.2+', f3= '1.8', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Firefox 2.0', f2= 'Win 98+ / OSX.2+', f3= '1.8', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Firefox 3.0', f2= 'Win 2k+ / OSX.3+', f3= '1.9', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Camino 1.0', f2= 'OSX.2+', f3= '1.8', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Camino 1.5', f2= 'OSX.3+', f3= '1.8', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Netscape 7.2', f2= 'Win 95+ / Mac OS 8.6-9.2', f3= '1.7', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Netscape Browser 8', f2= 'Win 98SE+', f3= '1.7', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Netscape Navigator 9', f2= 'Win 98+ / OSX.2+', f3= '1.8', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Mozilla 1.0', f2= 'Win 95+ / OSX.1+', f3= '1', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Mozilla 1.1', f2= 'Win 95+ / OSX.1+', f3= '1.1', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Mozilla 1.2', f2= 'Win 95+ / OSX.1+', f3= '1.2', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Mozilla 1.3', f2= 'Win 95+ / OSX.1+', f3= '1.3', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Mozilla 1.4', f2= 'Win 95+ / OSX.1+', f3= '1.4', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Mozilla 1.5', f2= 'Win 95+ / OSX.1+', f3= '1.5', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Mozilla 1.6', f2= 'Win 95+ / OSX.1+', f3= '1.6', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Mozilla 1.7', f2= 'Win 98+ / OSX.1+', f3= '1.7', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Mozilla 1.8', f2= 'Win 98+ / OSX.1+', f3= '1.8', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Seamonkey 1.1', f2= 'Win 98+ / OSX.2+', f3= '1.8', f4= 'A', )
      db.datatable1.insert( f0= 'Gecko', f1= 'Epiphany 2.20', f2= 'Gnome', f3= '1.8', f4= 'A', )
      db.datatable1.insert( f0= 'Webkit', f1= 'Safari 1.2', f2= 'OSX.3', f3= '125.5', f4= 'A', )
      db.datatable1.insert( f0= 'Webkit', f1= 'Safari 1.3', f2= 'OSX.3', f3= '312.8', f4= 'A', )
      db.datatable1.insert( f0= 'Webkit', f1= 'Safari 2.0', f2= 'OSX.4+', f3= '419.3', f4= 'A', )
      db.datatable1.insert( f0= 'Webkit', f1= 'Safari 3.0', f2= 'OSX.4+', f3= '522.1', f4= 'A', )
      db.datatable1.insert( f0= 'Webkit', f1= 'OmniWeb 5.5', f2= 'OSX.4+', f3= '420', f4= 'A', )
      db.datatable1.insert( f0= 'Webkit', f1= 'iPod Touch / iPhone', f2= 'iPod', f3= '420.1', f4= 'A', )
      db.datatable1.insert( f0= 'Webkit', f1= 'S60', f2= 'S60', f3= '413', f4= 'A', )
      db.datatable1.insert( f0= 'Presto', f1= 'Opera 7.0', f2= 'Win 95+ / OSX.1+', f3= '-', f4= 'A', )
      db.datatable1.insert( f0= 'Presto', f1= 'Opera 7.5', f2= 'Win 95+ / OSX.2+', f3= '-', f4= 'A', )
      db.datatable1.insert( f0= 'Presto', f1= 'Opera 8.0', f2= 'Win 95+ / OSX.2+', f3= '-', f4= 'A', )
      db.datatable1.insert( f0= 'Presto', f1= 'Opera 8.5', f2= 'Win 95+ / OSX.2+', f3= '-', f4= 'A', )
      db.datatable1.insert( f0= 'Presto', f1= 'Opera 9.0', f2= 'Win 95+ / OSX.3+', f3= '-', f4= 'A', )
      db.datatable1.insert( f0= 'Presto', f1= 'Opera 9.2', f2= 'Win 88+ / OSX.3+', f3= '-', f4= 'A', )
      db.datatable1.insert( f0= 'Presto', f1= 'Opera 9.5', f2= 'Win 88+ / OSX.3+', f3= '-', f4= 'A', )
      db.datatable1.insert( f0= 'Presto', f1= 'Opera for Wii', f2= 'Wii', f3= '-', f4= 'A', )
      db.datatable1.insert( f0= 'Presto', f1= 'Nokia N800', f2= 'N800', f3= '-', f4= 'A', )
      db.datatable1.insert( f0= 'Presto', f1= 'Nintendo DS browser', f2= 'Nintendo DS', f3= '8.5', f4= 'C/A1', )
      db.datatable1.insert( f0= 'KHTML', f1= 'Konqureror 3.1', f2= 'KDE 3.1', f3= '3.1', f4= 'C', )
      db.datatable1.insert( f0= 'KHTML', f1= 'Konqureror 3.3', f2= 'KDE 3.3', f3= '3.3', f4= 'A', )
      db.datatable1.insert( f0= 'KHTML', f1= 'Konqureror 3.5', f2= 'KDE 3.5', f3= '3.5', f4= 'A', )
      db.datatable1.insert( f0= 'Tasman', f1= 'Internet Explorer 4.5', f2= 'Mac OS 8-9', f3= '-', f4= 'X', )
      db.datatable1.insert( f0= 'Tasman', f1= 'Internet Explorer 5.1', f2= 'Mac OS 7.6-9', f3= '1', f4= 'C', )
      db.datatable1.insert( f0= 'Tasman', f1= 'Internet Explorer 5.2', f2= 'Mac OS 8-X', f3= '1', f4= 'C', )
      db.datatable1.insert( f0= 'Misc', f1= 'NetFront 3.1', f2= 'Embedded devices', f3= '-', f4= 'C', )
      db.datatable1.insert( f0= 'Misc', f1= 'NetFront 3.4', f2= 'Embedded devices', f3= '-', f4= 'A', )
      db.datatable1.insert( f0= 'Misc', f1= 'Dillo 0.8', f2= 'Embedded devices', f3= '-', f4= 'X', )
      db.datatable1.insert( f0= 'Misc', f1= 'Links', f2= 'Text only', f3= '-', f4= 'X', )
      db.datatable1.insert( f0= 'Misc', f1= 'Lynx', f2= 'Text only', f3= '-', f4= 'X', )
      db.datatable1.insert( f0= 'Misc', f1= 'IE Mobile', f2= 'Windows Mobile 6', f3= '-', f4= 'C', )
      db.datatable1.insert( f0= 'Misc', f1= 'PSP browser', f2= 'PSP', f3= '-', f4= 'C', )
      db.datatable1.insert( f0= 'Other browsers', f1= 'All others', f2= '-', f3= '-', f4= 'U', )
      db.datatable1.insert( f0= 'Rendering engine', f1= 'Browser', f2= 'Platform(s)', f3= 'Engine version', f4= 'CSS grade', )
db.define_table('invoicetable0',
   Field( 'f0', 'string',  label= 'Qty', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Product', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Serial #', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Description', default= 'w2p f3' ), 
   Field( 'f4', 'string',  label= 'Subtotal', default= 'w2p f4' ), 
      )
if not db(db.invoicetable0.id ).count():
      db.invoicetable0.insert( f0= '00 invoicetable0', f1= '0w2p1 Product', f2= '0w2p2 Serial #', f3= '0w2p3 Description', f4= '0w2p4 Subtotal', )
      db.invoicetable0.insert( f0= '1', f1= 'Call of Duty', f2= '455-981-221', f3= 'El snort testosterone trophy driving gloves handsome', f4= '$64.50', )
      db.invoicetable0.insert( f0= '1', f1= 'Need for Speed IV', f2= '247-925-726', f3= 'Wes Anderson umami biodiesel', f4= '$50.00', )
      db.invoicetable0.insert( f0= '1', f1= 'Monsters DVD', f2= '735-845-642', f3= 'Terry Richardson helvetica tousled street art master', f4= '$10.70', )
      db.invoicetable0.insert( f0= '1', f1= 'Grown Ups Blue Ray', f2= '422-568-642', f3= 'Tousled lomo letterpress', f4= '$25.99', )
db.define_table('invoice0printtable0',
   Field( 'f0', 'string',  label= 'Qty', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Product', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Serial #', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Description', default= 'w2p f3' ), 
   Field( 'f4', 'string',  label= 'Subtotal', default= 'w2p f4' ), 
      )
if not db(db.invoice0printtable0.id ).count():
      db.invoice0printtable0.insert( f0= '00 invoice0printtable0', f1= '0w2p1 Product', f2= '0w2p2 Serial #', f3= '0w2p3 Description', f4= '0w2p4 Subtotal', )
      db.invoice0printtable0.insert( f0= '1', f1= 'Call of Duty', f2= '455-981-221', f3= 'El snort testosterone trophy driving gloves handsome', f4= '$64.50', )
      db.invoice0printtable0.insert( f0= '1', f1= 'Need for Speed IV', f2= '247-925-726', f3= 'Wes Anderson umami biodiesel', f4= '$50.00', )
      db.invoice0printtable0.insert( f0= '1', f1= 'Monsters DVD', f2= '735-845-642', f3= 'Terry Richardson helvetica tousled street art master', f4= '$10.70', )
      db.invoice0printtable0.insert( f0= '1', f1= 'Grown Ups Blue Ray', f2= '422-568-642', f3= 'Tousled lomo letterpress', f4= '$25.99', )
db.define_table('projectstable0',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'unk_22', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'unk_23', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Project Name', default= 'w2p f3' ), 
   Field( 'f4', 'string',  label= 'unk_24', default= 'w2p f4' ), 
   Field( 'f5', 'string',  label= 'unk_25', default= 'w2p f5' ), 
   Field( 'f6', 'string',  label= 'Team Members', default= 'w2p f6' ), 
   Field( 'f7', 'string',  label= 'unk_26', default= 'w2p f7' ), 
   Field( 'f8', 'string',  label= 'unk_27', default= 'w2p f8' ), 
   Field( 'f9', 'string',  label= 'Project Progress', default= 'w2p f9' ), 
   Field( 'f10', 'string',  label= 'unk_28', default= 'w2p f10' ), 
   Field( 'f11', 'string',  label= 'unk_29', default= 'w2p f11' ), 
   Field( 'f12', 'string',  label= 'Status', default= 'w2p f12' ), 
      )
if not db(db.projectstable0.id ).count():
      db.projectstable0.insert( f0= '00 projectstable0', f1= '0w2p1 unk_22', f2= '0w2p2 unk_23', f3= '0w2p3 Project Name', f4= '0w2p4 unk_24', f5= '0w2p5 unk_25', f6= '0w2p6 Team Members', f7= '0w2p7 unk_26', f8= '0w2p8 unk_27', f9= '0w2p9 Project Progress', f10= '0w2p10 unk_28', f11= '0w2p11 unk_29', f12= '0w2p12 Status', )
      db.projectstable0.insert( f0= '#', f1= 'AdminLTE v3 Created 01.01.2019', f2= 'unk_31', f3= '57% Complete', f4= 'Success', f5= 'View Edit Delete', )
      db.projectstable0.insert( f0= '#', f1= 'AdminLTE v3 Created 01.01.2019', f2= 'unk_32', f3= '47% Complete', f4= 'Success', f5= 'View Edit Delete', )
      db.projectstable0.insert( f0= '#', f1= 'AdminLTE v3 Created 01.01.2019', f2= 'unk_33', f3= '77% Complete', f4= 'Success', f5= 'View Edit Delete', )
      db.projectstable0.insert( f0= '#', f1= 'AdminLTE v3 Created 01.01.2019', f2= 'unk_34', f3= '60% Complete', f4= 'Success', f5= 'View Edit Delete', )
      db.projectstable0.insert( f0= '#', f1= 'AdminLTE v3 Created 01.01.2019', f2= 'unk_35', f3= '12% Complete', f4= 'Success', f5= 'View Edit Delete', )
      db.projectstable0.insert( f0= '#', f1= 'AdminLTE v3 Created 01.01.2019', f2= 'unk_36', f3= '35% Complete', f4= 'Success', f5= 'View Edit Delete', )
      db.projectstable0.insert( f0= '#', f1= 'AdminLTE v3 Created 01.01.2019', f2= 'unk_37', f3= '87% Complete', f4= 'Success', f5= 'View Edit Delete', )
      db.projectstable0.insert( f0= '#', f1= 'AdminLTE v3 Created 01.01.2019', f2= 'unk_38', f3= '77% Complete', f4= 'Success', f5= 'View Edit Delete', )
      db.projectstable0.insert( f0= '#', f1= 'AdminLTE v3 Created 01.01.2019', f2= 'unk_39', f3= '77% Complete', f4= 'Success', f5= 'View Edit Delete', )
db.define_table('index2table0',
   Field( 'f0', 'string',  label= 'Order ID', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Item', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Status', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Popularity', default= 'w2p f3' ), 
      )
if not db(db.index2table0.id ).count():
      db.index2table0.insert( f0= '00 index2table0', f1= '0w2p1 Item', f2= '0w2p2 Status', f3= '0w2p3 Popularity', )
      db.index2table0.insert( f0= 'OR9842', f1= 'Call of Duty IV', f2= 'Shipped', f3= '90,80,90,-70,61,-83,63', )
      db.index2table0.insert( f0= 'OR1848', f1= 'Samsung Smart TV', f2= 'Pending', f3= '90,80,-90,70,61,-83,68', )
      db.index2table0.insert( f0= 'OR7429', f1= 'iPhone 6 Plus', f2= 'Delivered', f3= '90,-80,90,70,-61,83,63', )
      db.index2table0.insert( f0= 'OR7429', f1= 'Samsung Smart TV', f2= 'Processing', f3= '90,80,-90,70,-61,83,63', )
      db.index2table0.insert( f0= 'OR1848', f1= 'Samsung Smart TV', f2= 'Pending', f3= '90,80,-90,70,61,-83,68', )
      db.index2table0.insert( f0= 'OR7429', f1= 'iPhone 6 Plus', f2= 'Delivered', f3= '90,-80,90,70,-61,83,63', )
      db.index2table0.insert( f0= 'OR9842', f1= 'Call of Duty IV', f2= 'Shipped', f3= '90,80,90,-70,61,-83,63', )