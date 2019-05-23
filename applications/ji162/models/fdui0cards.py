#
# table for controller: ui_cards
#

from gluon.contrib.populate import populate

db.define_table('dui0cards', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dui0cards.id ).count():
    db.dui0cards.insert( f0= 'hc1391', f1= '(1391)UI elements')
    db.dui0cards.insert( f0= 'aa1393', f1= '(1393)Buttons')
    db.dui0cards.insert( f0= 'aa1395', f1= '(1395)Badges')
    db.dui0cards.insert( f0= 'aa1397', f1= '(1397)Tabs')
    db.dui0cards.insert( f0= 'aa1399', f1= '(1399)Social Buttons')
    db.dui0cards.insert( f0= 'aa1401', f1= '(1401)Cards')
    db.dui0cards.insert( f0= 'aa1403', f1= '(1403)Alerts')
    db.dui0cards.insert( f0= 'aa1405', f1= '(1405)Progress Bars')
    db.dui0cards.insert( f0= 'aa1407', f1= '(1407)Modals')
    db.dui0cards.insert( f0= 'aa1409', f1= '(1409)Switches')
    db.dui0cards.insert( f0= 'aa1411', f1= '(1411)Grids')
    db.dui0cards.insert( f0= 'aa1413', f1= '(1413)Typography')
    db.dui0cards.insert( f0= 'aa1415', f1= '(1415)Basic Table')
    db.dui0cards.insert( f0= 'aa1417', f1= '(1417)Data Table')
    db.dui0cards.insert( f0= 'aa1419', f1= '(1419)Basic Form')
    db.dui0cards.insert( f0= 'aa1421', f1= '(1421)Advanced Form')
    db.dui0cards.insert( f0= 'hc1422', f1= '(1422)Icons')
    db.dui0cards.insert( f0= 'aa1424', f1= '(1424)Font Awesome')
    db.dui0cards.insert( f0= 'aa1426', f1= '(1426)Themefy Icons')
    db.dui0cards.insert( f0= 'aa1429', f1= '(1429)Chart JS')
    db.dui0cards.insert( f0= 'aa1431', f1= '(1431)Flot Chart')
    db.dui0cards.insert( f0= 'aa1433', f1= '(1433)Peity Chart')
    db.dui0cards.insert( f0= 'aa1435', f1= '(1435)Google Maps')
    db.dui0cards.insert( f0= 'aa1437', f1= '(1437)Vector Maps')
    db.dui0cards.insert( f0= 'hc1438', f1= '(1438)Extras')
    db.dui0cards.insert( f0= 'aa1440', f1= '(1440)Login')
    db.dui0cards.insert( f0= 'aa1442', f1= '(1442)Register')
    db.dui0cards.insert( f0= 'aa1444', f1= '(1444)Forget Pass')
    db.dui0cards.insert( f0= 'pb1445', f1= '(1445)Search ...')
    db.dui0cards.insert( f0= 'pc1446', f1= '(1446)You have 3 Notification')
    db.dui0cards.insert( f0= 'pc1447', f1= '(1447)You have 4 Mails')
    db.dui0cards.insert( f0= 'sx1449', f1= '(1449)Jonathan Smith')
    db.dui0cards.insert( f0= 'sx1450', f1= '(1450)Just now')
    db.dui0cards.insert( f0= 'pa1451', f1= '(1451)Hello, this is an example msg')
    db.dui0cards.insert( f0= 'sx1453', f1= '(1453)Jack Sanders')
    db.dui0cards.insert( f0= 'sx1454', f1= '(1454)5 minutes ago')
    db.dui0cards.insert( f0= 'pa1455', f1= '(1455)Lorem ipsum dolor sit amet, consectetur')
    db.dui0cards.insert( f0= 'sx1457', f1= '(1457)Cheryl Wheeler')
    db.dui0cards.insert( f0= 'sx1458', f1= '(1458)10 minutes ago')
    db.dui0cards.insert( f0= 'pa1459', f1= '(1459)Hello, this is an example msg')
    db.dui0cards.insert( f0= 'sx1461', f1= '(1461)Rachel Santos')
    db.dui0cards.insert( f0= 'sx1462', f1= '(1462)15 minutes ago')
    db.dui0cards.insert( f0= 'pa1463', f1= '(1463)Lorem ipsum dolor sit amet, consectetur')
    db.dui0cards.insert( f0= 'sx1465', f1= '(1465)13')
    db.dui0cards.insert( f0= 'hh1466', f1= '(1466)Dashboard')
    db.dui0cards.insert( f0= 'aa1467', f1= '(1467)Dashboard')
    db.dui0cards.insert( f0= 'aa1468', f1= '(1468)UI Elements')
    db.dui0cards.insert( f0= 'lb1469', f1= '(1469)Cards')
    db.dui0cards.insert( f0= 'he1471', f1= '(1471)Steven Lee')
    db.dui0cards.insert( f0= 'he1473', f1= '(1473)Steven Lee')
    db.dui0cards.insert( f0= 'he1475', f1= '(1475)Steven Lee')
    db.dui0cards.insert( f0= 'hb1477', f1= '(1477)Jim Doe')
    db.dui0cards.insert( f0= 'pa1478', f1= '(1478)Project Manager')
    db.dui0cards.insert( f0= 'sx1479', f1= '(1479)10')
    db.dui0cards.insert( f0= 'sx1480', f1= '(1480)15')
    db.dui0cards.insert( f0= 'sx1481', f1= '(1481)11')
    db.dui0cards.insert( f0= 'sx1482', f1= '(1482)03')
    db.dui0cards.insert( f0= 'hh1484', f1= '(1484)Kanye West')
    db.dui0cards.insert( f0= 'pf1485', f1= '(1485)Just got a pretty neat project via')
    db.dui0cards.insert( f0= 'aa1486', f1= '(1486)@ooomf')
    db.dui0cards.insert( f0= 'hb1488', f1= '(1488)Jim Doe')
    db.dui0cards.insert( f0= 'pc1489', f1= '(1489)Project Manager')
    db.dui0cards.insert( f0= 'hh1490', f1= '(1490)750')
    db.dui0cards.insert( f0= 'hh1491', f1= '(1491)865')
    db.dui0cards.insert( f0= 'hh1492', f1= '(1492)3645')
    db.dui0cards.insert( f0= 'pb1493', f1= '(1493)Write your Tweet and Enter')
    db.dui0cards.insert( f0= 'pc1494', f1= '(1494)Some quick example text to build on the card title and make up the bulk of the card s content.')
    db.dui0cards.insert( f0= 'sx1495', f1= '(1495)Success')
    db.dui0cards.insert( f0= 'pc1496', f1= '(1496)Some quick example text to build on the card title and make up the bulk of the card s content.')
    db.dui0cards.insert( f0= 'sx1497', f1= '(1497)49')
    db.dui0cards.insert( f0= 'pc1498', f1= '(1498)Some quick example text to build on the card title and make up the bulk of the card s content.')
    db.dui0cards.insert( f0= 'pc1499', f1= '(1499)Some quick example text to build on the card title and make up the bulk of the card s content.')
    db.dui0cards.insert( f0= 'pc1500', f1= '(1500)Some quick example text to build on the card title and make up the bulk of the card s content.')
    db.dui0cards.insert( f0= 'pc1501', f1= '(1501)Some quick example text to build on the card title and make up the bulk of the card s content.')
    db.dui0cards.insert( f0= 'pc1502', f1= '(1502)Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.')
    db.dui0cards.insert( f0= 'pc1503', f1= '(1503)Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.')
    db.dui0cards.insert( f0= 'pc1504', f1= '(1504)Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.')
    db.dui0cards.insert( f0= 'pc1505', f1= '(1505)Some quick example text to build on the card title and make up the bulk of the card s content.')
    db.dui0cards.insert( f0= 'pc1506', f1= '(1506)Some quick example text to build on the card title and make up the bulk of the card s content.')
    db.dui0cards.insert( f0= 'pc1507', f1= '(1507)Some quick example text to build on the card title and make up the bulk of the card s content.')
    db.dui0cards.insert( f0= 'hd1509', f1= '(1509)Card Image Title')
    db.dui0cards.insert( f0= 'pc1510', f1= '(1510)Some quick example text to build on the card title and make up the bulk of the card s content.')
    db.dui0cards.insert( f0= 'hd1512', f1= '(1512)Card Image Title')
    db.dui0cards.insert( f0= 'pc1513', f1= '(1513)Some quick example text to build on the card title and make up the bulk of the card s content.')
    db.dui0cards.insert( f0= 'hd1515', f1= '(1515)Card Image Title')
    db.dui0cards.insert( f0= 'pc1516', f1= '(1516)Some quick example text to build on the card title and make up the bulk of the card s content.')
    db.commit()
#
