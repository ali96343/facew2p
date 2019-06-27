
db.define_table('widgetstable0',
   Field( 'f0', 'string',  label= 'User', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'unk_2', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'unk_3', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'unk_4', default= 'w2p f3' ), 
   Field( 'f4', 'string',  label= '@', default= 'w2p f4' ), 
   Field( 'f5', 'string',  label= 'Email', default= 'w2p f5' ), 
   Field( 'f6', 'string',  label= 'unk_5', default= 'w2p f6' ), 
   Field( 'f7', 'string',  label= 'Status', default= 'w2p f7' ), 
      )
if not db(db.widgetstable0.id ).count():
      db.widgetstable0.insert( f0= '00 widgetstable0', f1= '0w2p1 unk_2', f2= '0w2p2 unk_3', f3= '0w2p3 unk_4', f4= '0w2p4 @', f5= '0w2p5 Email', f6= '0w2p6 unk_5', f7= '0w2p7 Status', )
      db.widgetstable0.insert( f0= 'Alex', f1= 'alex@email.com', f2= 'Pending', )
      db.widgetstable0.insert( f0= 'Fred', f1= 'fred@email.com', f2= 'Approved', )
      db.widgetstable0.insert( f0= 'Jack', f1= 'jack@email.com', f2= 'Pending', )
      db.widgetstable0.insert( f0= 'John', f1= 'john@email.com', f2= 'Blocked', )
      db.widgetstable0.insert( f0= 'James', f1= 'james@email.com', f2= 'Online', )
db.define_table('tablestable0',
   Field( 'f0', 'string',  label= 'Details', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Domain', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Price', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Clicks', default= 'w2p f3' ), 
   Field( 'f4', 'string',  label= 'unk_6', default= 'w2p f4' ), 
   Field( 'f5', 'string',  label= 'unk_7', default= 'w2p f5' ), 
   Field( 'f6', 'string',  label= 'unk_8', default= 'w2p f6' ), 
   Field( 'f7', 'string',  label= 'Update', default= 'w2p f7' ), 
   Field( 'f8', 'string',  label= 'unk_9', default= 'w2p f8' ), 
   Field( 'f9', 'string',  label= 'Status', default= 'w2p f9' ), 
      )
if not db(db.tablestable0.id ).count():
      db.tablestable0.insert( f0= '00 tablestable0', f1= '0w2p1 Domain', f2= '0w2p2 Price', f3= '0w2p3 Clicks', f4= '0w2p4 unk_6', f5= '0w2p5 unk_7', f6= '0w2p6 unk_8', f7= '0w2p7 Update', f8= '0w2p8 unk_9', f9= '0w2p9 Status', )
      db.tablestable0.insert( f0= 'unk_12', f1= 'Details', f2= 'ace.com', f3= '$45', f4= '3,330', f5= 'Feb 12', f6= 'Expiring', f7= 'unk_13', )
      db.tablestable0.insert( f0= 'Alex M. Doe Username alexdoe Location Netherlands, Amsterdam Age 38 Joined 2010/06/20 Last Online 3 hours ago About Me Bio Send a message to Alex Email me a copy Submit', )
      db.tablestable0.insert( f0= 'unk_14', f1= 'Details', f2= 'base.com', f3= '$35', f4= '2,595', f5= 'Feb 18', f6= 'Registered', f7= 'unk_15', )
      db.tablestable0.insert( f0= 'Alex M. Doe Username alexdoe Location Netherlands, Amsterdam Age 38 Joined 2010/06/20 Last Online 3 hours ago About Me Bio Send a message to Alex Email me a copy Submit', )
      db.tablestable0.insert( f0= 'unk_16', f1= 'Details', f2= 'max.com', f3= '$60', f4= '4,400', f5= 'Mar 11', f6= 'Expiring', f7= 'unk_17', )
      db.tablestable0.insert( f0= 'Alex M. Doe Username alexdoe Location Netherlands, Amsterdam Age 38 Joined 2010/06/20 Last Online 3 hours ago About Me Bio Send a message to Alex Email me a copy Submit', )
      db.tablestable0.insert( f0= 'unk_18', f1= 'Details', f2= 'best.com', f3= '$75', f4= '6,500', f5= 'Apr 03', f6= 'Flagged', f7= 'unk_19', )
      db.tablestable0.insert( f0= 'Alex M. Doe Username alexdoe Location Netherlands, Amsterdam Age 38 Joined 2010/06/20 Last Online 3 hours ago About Me Bio Send a message to Alex Email me a copy Submit', )
      db.tablestable0.insert( f0= 'unk_20', f1= 'Details', f2= 'pro.com', f3= '$55', f4= '4,250', f5= 'Jan 21', f6= 'Registered', f7= 'unk_21', )
      db.tablestable0.insert( f0= 'Alex M. Doe Username alexdoe Location Netherlands, Amsterdam Age 38 Joined 2010/06/20 Last Online 3 hours ago About Me Bio Send a message to Alex Email me a copy Submit', )
db.define_table('tablestable1',
   Field( 'f0', 'string',  label= 'Domain', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Price', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Clicks', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'unk_22', default= 'w2p f3' ), 
   Field( 'f4', 'string',  label= 'unk_23', default= 'w2p f4' ), 
   Field( 'f5', 'string',  label= 'unk_24', default= 'w2p f5' ), 
   Field( 'f6', 'string',  label= 'Update', default= 'w2p f6' ), 
   Field( 'f7', 'string',  label= 'unk_25', default= 'w2p f7' ), 
   Field( 'f8', 'string',  label= 'Status', default= 'w2p f8' ), 
      )
if not db(db.tablestable1.id ).count():
      db.tablestable1.insert( f0= '00 tablestable1', f1= '0w2p1 Price', f2= '0w2p2 Clicks', f3= '0w2p3 unk_22', f4= '0w2p4 unk_23', f5= '0w2p5 unk_24', f6= '0w2p6 Update', f7= '0w2p7 unk_25', f8= '0w2p8 Status', )
      db.tablestable1.insert( f0= 'unk_28', f1= 'app.com', f2= '$45', f3= '3,330', f4= 'Feb 12', f5= 'Expiring', f6= 'unk_29', )
      db.tablestable1.insert( f0= 'unk_30', f1= 'base.com', f2= '$35', f3= '2,595', f4= 'Feb 18', f5= 'Registered', f6= 'unk_31', )
      db.tablestable1.insert( f0= 'unk_32', f1= 'max.com', f2= '$60', f3= '4,400', f4= 'Mar 11', f5= 'Expiring', f6= 'unk_33', )
      db.tablestable1.insert( f0= 'unk_34', f1= 'best.com', f2= '$75', f3= '6,500', f4= 'Apr 03', f5= 'Flagged', f6= 'unk_35', )
      db.tablestable1.insert( f0= 'unk_36', f1= 'pro.com', f2= '$55', f3= '4,250', f4= 'Jan 21', f5= 'Registered', f6= 'unk_37', )
      db.tablestable1.insert( f0= 'unk_38', f1= 'team.com', f2= '$40', f3= '3,200', f4= 'Feb 09', f5= 'Flagged', f6= 'unk_39', )
      db.tablestable1.insert( f0= 'unk_40', f1= 'up.com', f2= '$95', f3= '8,520', f4= 'Feb 22', f5= 'Sold', f6= 'unk_41', )
      db.tablestable1.insert( f0= 'unk_42', f1= 'view.com', f2= '$45', f3= '4,100', f4= 'Mar 12', f5= 'Registered', f6= 'unk_43', )
      db.tablestable1.insert( f0= 'unk_44', f1= 'nice.com', f2= '$38', f3= '3,940', f4= 'Feb 12', f5= 'Sold', f6= 'unk_45', )
      db.tablestable1.insert( f0= 'unk_46', f1= 'fine.com', f2= '$25', f3= '2,983', f4= 'Apr 01', f5= 'Expiring', f6= 'unk_47', )
      db.tablestable1.insert( f0= 'unk_48', f1= 'good.com', f2= '$50', f3= '6,500', f4= 'Feb 02', f5= 'Flagged', f6= 'unk_49', )
      db.tablestable1.insert( f0= 'unk_50', f1= 'great.com', f2= '$55', f3= '6,400', f4= 'Feb 24', f5= 'Registered', f6= 'unk_51', )
      db.tablestable1.insert( f0= 'unk_52', f1= 'shine.com', f2= '$25', f3= '2,200', f4= 'Apr 01', f5= 'Flagged', f6= 'unk_53', )
      db.tablestable1.insert( f0= 'unk_54', f1= 'rise.com', f2= '$42', f3= '3,900', f4= 'Feb 01', f5= 'Sold', f6= 'unk_55', )
      db.tablestable1.insert( f0= 'unk_56', f1= 'above.com', f2= '$35', f3= '3,420', f4= 'Mar 12', f5= 'Expiring', f6= 'unk_57', )
      db.tablestable1.insert( f0= 'unk_58', f1= 'share.com', f2= '$30', f3= '3,200', f4= 'Feb 11', f5= 'Sold', f6= 'unk_59', )
      db.tablestable1.insert( f0= 'unk_60', f1= 'fair.com', f2= '$35', f3= '3,900', f4= 'Mar 26', f5= 'Flagged', f6= 'unk_61', )
      db.tablestable1.insert( f0= 'unk_62', f1= 'year.com', f2= '$48', f3= '3,990', f4= 'Feb 15', f5= 'Expiring', f6= 'unk_63', )
      db.tablestable1.insert( f0= 'unk_64', f1= 'day.com', f2= '$55', f3= '5,600', f4= 'Jan 29', f5= 'Sold', f6= 'unk_65', )
      db.tablestable1.insert( f0= 'unk_66', f1= 'light.com', f2= '$40', f3= '3,100', f4= 'Feb 17', f5= 'Registered', f6= 'unk_67', )
      db.tablestable1.insert( f0= 'unk_68', f1= 'sight.com', f2= '$58', f3= '6,100', f4= 'Feb 19', f5= 'Flagged', f6= 'unk_69', )
      db.tablestable1.insert( f0= 'unk_70', f1= 'right.com', f2= '$50', f3= '4,400', f4= 'Apr 01', f5= 'Expiring', f6= 'unk_71', )
      db.tablestable1.insert( f0= 'unk_72', f1= 'once.com', f2= '$20', f3= '1,400', f4= 'Apr 04', f5= 'Sold', f6= 'unk_73', )
db.define_table('tablestable2',
   Field( 'f0', 'string',  label= 'Domain', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Price', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Clicks', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'unk_74', default= 'w2p f3' ), 
   Field( 'f4', 'string',  label= 'unk_75', default= 'w2p f4' ), 
   Field( 'f5', 'string',  label= 'unk_76', default= 'w2p f5' ), 
   Field( 'f6', 'string',  label= 'Update', default= 'w2p f6' ), 
      )
if not db(db.tablestable2.id ).count():
      db.tablestable2.insert( f0= '00 tablestable2', f1= '0w2p1 Price', f2= '0w2p2 Clicks', f3= '0w2p3 unk_74', f4= '0w2p4 unk_75', f5= '0w2p5 unk_76', f6= '0w2p6 Update', )
      db.tablestable2.insert( f0= 'ace.com', f1= '$45', f2= '3,330', f3= 'Feb 12', )
      db.tablestable2.insert( f0= 'base.com', f1= '$35', f2= '2,595', f3= 'Feb 18', )
      db.tablestable2.insert( f0= 'max.com', f1= '$60', f2= '4,400', f3= 'Mar 11', )
      db.tablestable2.insert( f0= 'best.com', f1= '$75', f2= '6,500', f3= 'Apr 03', )
      db.tablestable2.insert( f0= 'pro.com', f1= '$55', f2= '4,250', f3= 'Jan 21', )
db.define_table('indextable0',
   Field( 'f0', 'string',  label= 'name', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'unk_77', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'unk_78', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'unk_79', default= 'w2p f3' ), 
   Field( 'f4', 'string',  label= 'price', default= 'w2p f4' ), 
   Field( 'f5', 'string',  label= 'unk_80', default= 'w2p f5' ), 
   Field( 'f6', 'string',  label= 'unk_81', default= 'w2p f6' ), 
   Field( 'f7', 'string',  label= 'unk_82', default= 'w2p f7' ), 
   Field( 'f8', 'string',  label= 'status', default= 'w2p f8' ), 
      )
if not db(db.indextable0.id ).count():
      db.indextable0.insert( f0= '00 indextable0', f1= '0w2p1 unk_77', f2= '0w2p2 unk_78', f3= '0w2p3 unk_79', f4= '0w2p4 price', f5= '0w2p5 unk_80', f6= '0w2p6 unk_81', f7= '0w2p7 unk_82', f8= '0w2p8 status', )
      db.indextable0.insert( f0= 'internet.com', f1= '$29.99 $19.99', f2= 'on sale', )
      db.indextable0.insert( f0= 'online.com', f1= '$16.45', f2= 'approved', )
      db.indextable0.insert( f0= 'newnet.com', f1= '$15.00', f2= 'pending', )
      db.indextable0.insert( f0= 'web.com', f1= '$24.99 $19.95', f2= 'out of stock', )
      db.indextable0.insert( f0= 'domain.com', f1= '$12.00', f2= 'SOLD', )
db.define_table('invoicetable0',
   Field( 'f0', 'string',  label= '#', default= 'w2p f0' ), 
   Field( 'f1', 'string',  label= 'Product', default= 'w2p f1' ), 
   Field( 'f2', 'string',  label= 'Description', default= 'w2p f2' ), 
   Field( 'f3', 'string',  label= 'Discount', default= 'w2p f3' ), 
   Field( 'f4', 'string',  label= 'Total', default= 'w2p f4' ), 
      )
if not db(db.invoicetable0.id ).count():
      db.invoicetable0.insert( f0= '00 invoicetable0', f1= '0w2p1 Product', f2= '0w2p2 Description', f3= '0w2p3 Discount', f4= '0w2p4 Total', )
      db.invoicetable0.insert( f0= '1', f1= 'google.com', f2= '1 year domain registration', f3= '---', f4= '$10', )
      db.invoicetable0.insert( f0= '2', f1= 'yahoo.com', f2= '5 year domain registration', f3= '5%', f4= '$45', )
      db.invoicetable0.insert( f0= '3', f1= 'Hosting', f2= '1 year basic hosting', f3= '10%', f4= '$90', )
      db.invoicetable0.insert( f0= '4', f1= 'Design', f2= 'Theme customization', f3= '50%', f4= '$250', )