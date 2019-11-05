
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