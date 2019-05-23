#
# table for controller: frame
#

from gluon.contrib.populate import populate

db.define_table('dframe', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dframe.id ).count():
    db.dframe.insert( f0= 'hc1538', f1= '(1538)UI elements')
    db.dframe.insert( f0= 'aa1540', f1= '(1540)Buttons')
    db.dframe.insert( f0= 'aa1542', f1= '(1542)Badges')
    db.dframe.insert( f0= 'aa1544', f1= '(1544)Tabs')
    db.dframe.insert( f0= 'aa1546', f1= '(1546)Social Buttons')
    db.dframe.insert( f0= 'aa1548', f1= '(1548)Cards')
    db.dframe.insert( f0= 'aa1550', f1= '(1550)Alerts')
    db.dframe.insert( f0= 'aa1552', f1= '(1552)Progress Bars')
    db.dframe.insert( f0= 'aa1554', f1= '(1554)Modals')
    db.dframe.insert( f0= 'aa1556', f1= '(1556)Switches')
    db.dframe.insert( f0= 'aa1558', f1= '(1558)Grids')
    db.dframe.insert( f0= 'aa1560', f1= '(1560)Typography')
    db.dframe.insert( f0= 'aa1562', f1= '(1562)Basic Table')
    db.dframe.insert( f0= 'aa1564', f1= '(1564)Data Table')
    db.dframe.insert( f0= 'aa1566', f1= '(1566)Basic Form')
    db.dframe.insert( f0= 'aa1568', f1= '(1568)Advanced Form')
    db.dframe.insert( f0= 'hc1569', f1= '(1569)Icons')
    db.dframe.insert( f0= 'aa1571', f1= '(1571)Font Awesome')
    db.dframe.insert( f0= 'aa1573', f1= '(1573)Themefy Icons')
    db.dframe.insert( f0= 'aa1576', f1= '(1576)Chart JS')
    db.dframe.insert( f0= 'aa1578', f1= '(1578)Flot Chart')
    db.dframe.insert( f0= 'aa1580', f1= '(1580)Peity Chart')
    db.dframe.insert( f0= 'aa1582', f1= '(1582)Google Maps')
    db.dframe.insert( f0= 'aa1584', f1= '(1584)Vector Maps')
    db.dframe.insert( f0= 'hc1585', f1= '(1585)Extras')
    db.dframe.insert( f0= 'aa1587', f1= '(1587)Login')
    db.dframe.insert( f0= 'aa1589', f1= '(1589)Register')
    db.dframe.insert( f0= 'aa1591', f1= '(1591)Forget Pass')
    db.dframe.insert( f0= 'pb1592', f1= '(1592)Search ...')
    db.dframe.insert( f0= 'pc1593', f1= '(1593)You have 3 Notification')
    db.dframe.insert( f0= 'pc1594', f1= '(1594)You have 4 Mails')
    db.dframe.insert( f0= 'sx1596', f1= '(1596)Jonathan Smith')
    db.dframe.insert( f0= 'sx1597', f1= '(1597)Just now')
    db.dframe.insert( f0= 'pa1598', f1= '(1598)Hello, this is an example msg')
    db.dframe.insert( f0= 'sx1600', f1= '(1600)Jack Sanders')
    db.dframe.insert( f0= 'sx1601', f1= '(1601)5 minutes ago')
    db.dframe.insert( f0= 'pa1602', f1= '(1602)Lorem ipsum dolor sit amet, consectetur')
    db.dframe.insert( f0= 'sx1604', f1= '(1604)Cheryl Wheeler')
    db.dframe.insert( f0= 'sx1605', f1= '(1605)10 minutes ago')
    db.dframe.insert( f0= 'pa1606', f1= '(1606)Hello, this is an example msg')
    db.dframe.insert( f0= 'sx1608', f1= '(1608)Rachel Santos')
    db.dframe.insert( f0= 'sx1609', f1= '(1609)15 minutes ago')
    db.dframe.insert( f0= 'pa1610', f1= '(1610)Lorem ipsum dolor sit amet, consectetur')
    db.dframe.insert( f0= 'sx1612', f1= '(1612)13')
    db.dframe.insert( f0= 'hh1613', f1= '(1613)Dashboard')
    db.dframe.insert( f0= 'lb1614', f1= '(1614)Dashboard')
    db.commit()
#
