#
# table for controller: index3
#

from gluon.contrib.populate import populate

db.define_table('dindex3', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dindex3.id ).count():
    db.dindex3.insert( f0= 'aa5295', f1= '(5295)Home')
    db.dindex3.insert( f0= 'aa5296', f1= '(5296)Contact')
    db.dindex3.insert( f0= 'pb5297', f1= '(5297)Search')
    db.dindex3.insert( f0= 'sx5298', f1= '(5298)3')
    db.dindex3.insert( f0= 'pc5300', f1= '(5300)Call me whenever you can...')
    db.dindex3.insert( f0= 'pc5301', f1= '(5301)4 Hours Ago')
    db.dindex3.insert( f0= 'pc5303', f1= '(5303)I got your message bro')
    db.dindex3.insert( f0= 'pc5304', f1= '(5304)4 Hours Ago')
    db.dindex3.insert( f0= 'pc5306', f1= '(5306)The subject goes here')
    db.dindex3.insert( f0= 'pc5307', f1= '(5307)4 Hours Ago')
    db.dindex3.insert( f0= 'aa5308', f1= '(5308)See All Messages')
    db.dindex3.insert( f0= 'sx5309', f1= '(5309)15 Notifications')
    db.dindex3.insert( f0= 'sx5310', f1= '(5310)3 mins')
    db.dindex3.insert( f0= 'sx5311', f1= '(5311)12 hours')
    db.dindex3.insert( f0= 'sx5312', f1= '(5312)2 days')
    db.dindex3.insert( f0= 'aa5313', f1= '(5313)See All Notifications')
    db.dindex3.insert( f0= 'sx5316', f1= '(5316)AdminLTE 3')
    db.dindex3.insert( f0= 'aa5318', f1= '(5318)Alexander Pierce')
    db.dindex3.insert( f0= 'pa5320', f1= '(5320)Dashboard v1')
    db.dindex3.insert( f0= 'pa5322', f1= '(5322)Dashboard v2')
    db.dindex3.insert( f0= 'pa5324', f1= '(5324)Dashboard v3')
    db.dindex3.insert( f0= 'sx5326', f1= '(5326)New')
    db.dindex3.insert( f0= 'sx5327', f1= '(5327)6')
    db.dindex3.insert( f0= 'pa5329', f1= '(5329)Top Navigation')
    db.dindex3.insert( f0= 'pa5331', f1= '(5331)Boxed')
    db.dindex3.insert( f0= 'pa5333', f1= '(5333)Fixed Sidebar')
    db.dindex3.insert( f0= 'pa5335', f1= '(5335)Fixed Navbar')
    db.dindex3.insert( f0= 'pa5337', f1= '(5337)Fixed Footer')
    db.dindex3.insert( f0= 'pa5339', f1= '(5339)Collapsed Sidebar')
    db.dindex3.insert( f0= 'pa5341', f1= '(5341)ChartJS')
    db.dindex3.insert( f0= 'pa5343', f1= '(5343)Flot')
    db.dindex3.insert( f0= 'pa5345', f1= '(5345)Inline')
    db.dindex3.insert( f0= 'pa5347', f1= '(5347)General')
    db.dindex3.insert( f0= 'pa5349', f1= '(5349)Icons')
    db.dindex3.insert( f0= 'pa5351', f1= '(5351)Buttons')
    db.dindex3.insert( f0= 'pa5353', f1= '(5353)Sliders')
    db.dindex3.insert( f0= 'pa5355', f1= '(5355)Modals & Alerts')
    db.dindex3.insert( f0= 'pa5357', f1= '(5357)Navbar & Tabs')
    db.dindex3.insert( f0= 'pa5359', f1= '(5359)Timeline')
    db.dindex3.insert( f0= 'pa5361', f1= '(5361)Ribbons')
    db.dindex3.insert( f0= 'pa5363', f1= '(5363)General Elements')
    db.dindex3.insert( f0= 'pa5365', f1= '(5365)Advanced Elements')
    db.dindex3.insert( f0= 'pa5367', f1= '(5367)Editors')
    db.dindex3.insert( f0= 'pa5369', f1= '(5369)Simple Tables')
    db.dindex3.insert( f0= 'pa5371', f1= '(5371)DataTables')
    db.dindex3.insert( f0= 'pa5373', f1= '(5373)jsGrid')
    db.dindex3.insert( f0= 'lb5374', f1= '(5374)EXAMPLES')
    db.dindex3.insert( f0= 'sx5376', f1= '(5376)2')
    db.dindex3.insert( f0= 'pa5379', f1= '(5379)Inbox')
    db.dindex3.insert( f0= 'pa5381', f1= '(5381)Compose')
    db.dindex3.insert( f0= 'pa5383', f1= '(5383)Read')
    db.dindex3.insert( f0= 'pa5385', f1= '(5385)Invoice')
    db.dindex3.insert( f0= 'pa5387', f1= '(5387)Profile')
    db.dindex3.insert( f0= 'pa5389', f1= '(5389)E-commerce')
    db.dindex3.insert( f0= 'pa5391', f1= '(5391)Projects')
    db.dindex3.insert( f0= 'pa5393', f1= '(5393)Project Add')
    db.dindex3.insert( f0= 'pa5395', f1= '(5395)Project Edit')
    db.dindex3.insert( f0= 'pa5397', f1= '(5397)Project Detail')
    db.dindex3.insert( f0= 'pa5399', f1= '(5399)Contacts')
    db.dindex3.insert( f0= 'pa5401', f1= '(5401)Login')
    db.dindex3.insert( f0= 'pa5403', f1= '(5403)Register')
    db.dindex3.insert( f0= 'pa5405', f1= '(5405)Forgot Password')
    db.dindex3.insert( f0= 'pa5407', f1= '(5407)Recover Password')
    db.dindex3.insert( f0= 'pa5409', f1= '(5409)Lockscreen')
    db.dindex3.insert( f0= 'pa5411', f1= '(5411)Legacy User Menu')
    db.dindex3.insert( f0= 'pa5413', f1= '(5413)Language Menu')
    db.dindex3.insert( f0= 'pa5415', f1= '(5415)Error 404')
    db.dindex3.insert( f0= 'pa5417', f1= '(5417)Error 500')
    db.dindex3.insert( f0= 'pa5419', f1= '(5419)Pace')
    db.dindex3.insert( f0= 'pa5421', f1= '(5421)Blank Page')
    db.dindex3.insert( f0= 'pa5423', f1= '(5423)Starter Page')
    db.dindex3.insert( f0= 'lb5424', f1= '(5424)MISCELLANEOUS')
    db.dindex3.insert( f0= 'pa5425', f1= '(5425)Documentation')
    db.dindex3.insert( f0= 'lb5426', f1= '(5426)MULTI LEVEL EXAMPLE')
    db.dindex3.insert( f0= 'pa5427', f1= '(5427)Level 1')
    db.dindex3.insert( f0= 'pa5428', f1= '(5428)Level 2')
    db.dindex3.insert( f0= 'pa5429', f1= '(5429)Level 3')
    db.dindex3.insert( f0= 'pa5430', f1= '(5430)Level 3')
    db.dindex3.insert( f0= 'pa5431', f1= '(5431)Level 3')
    db.dindex3.insert( f0= 'pa5432', f1= '(5432)Level 2')
    db.dindex3.insert( f0= 'pa5433', f1= '(5433)Level 1')
    db.dindex3.insert( f0= 'lb5434', f1= '(5434)LABELS')
    db.dindex3.insert( f0= 'pc5435', f1= '(5435)Important')
    db.dindex3.insert( f0= 'pa5436', f1= '(5436)Warning')
    db.dindex3.insert( f0= 'pa5437', f1= '(5437)Informational')
    db.dindex3.insert( f0= 'ha5438', f1= '(5438)Dashboard v3')
    db.dindex3.insert( f0= 'aa5439', f1= '(5439)Home')
    db.dindex3.insert( f0= 'lb5440', f1= '(5440)Dashboard v3')
    db.dindex3.insert( f0= 'hc5441', f1= '(5441)Online Store Visitors')
    db.dindex3.insert( f0= 'aa5442', f1= '(5442)View Report')
    db.dindex3.insert( f0= 'sp5443', f1= '(5443)Visitors Over Time')
    db.dindex3.insert( f0= 'sx5444', f1= '(5444)Since last week')
    db.dindex3.insert( f0= 'hc5445', f1= '(5445)Products')
    db.dindex3.insert( f0= 'sx5450', f1= '(5450)NEW')
    db.dindex3.insert( f0= 'hc5451', f1= '(5451)Sales')
    db.dindex3.insert( f0= 'aa5452', f1= '(5452)View Report')
    db.dindex3.insert( f0= 'sx5453', f1= '(5453)$18,230.00')
    db.dindex3.insert( f0= 'sp5454', f1= '(5454)Sales Over Time')
    db.dindex3.insert( f0= 'sx5455', f1= '(5455)Since last month')
    db.dindex3.insert( f0= 'hc5456', f1= '(5456)Online Store Overview')
    db.dindex3.insert( f0= 'sx5457', f1= '(5457)CONVERSION RATE')
    db.dindex3.insert( f0= 'sx5458', f1= '(5458)SALES RATE')
    db.dindex3.insert( f0= 'sx5459', f1= '(5459)REGISTRATION RATE')
    db.dindex3.insert( f0= 'aa5460', f1= '(5460)AdminLTE.io')
    db.dindex3.insert( f0= 'bb5461', f1= '(5461)Version')
    db.commit()
#
