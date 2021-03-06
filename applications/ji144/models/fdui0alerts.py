#
# table for controller: ui_alerts
#

from gluon.contrib.populate import populate

db.define_table('dui0alerts', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dui0alerts.id ).count():
    db.dui0alerts.insert( f0= 'hc16', f1= '(16)UI elements')
    db.dui0alerts.insert( f0= 'aa18', f1= '(18)Buttons')
    db.dui0alerts.insert( f0= 'aa20', f1= '(20)Badges')
    db.dui0alerts.insert( f0= 'aa22', f1= '(22)Tabs')
    db.dui0alerts.insert( f0= 'aa24', f1= '(24)Social Buttons')
    db.dui0alerts.insert( f0= 'aa26', f1= '(26)Cards')
    db.dui0alerts.insert( f0= 'aa28', f1= '(28)Alerts')
    db.dui0alerts.insert( f0= 'aa30', f1= '(30)Progress Bars')
    db.dui0alerts.insert( f0= 'aa32', f1= '(32)Modals')
    db.dui0alerts.insert( f0= 'aa34', f1= '(34)Switches')
    db.dui0alerts.insert( f0= 'aa36', f1= '(36)Grids')
    db.dui0alerts.insert( f0= 'aa38', f1= '(38)Typography')
    db.dui0alerts.insert( f0= 'aa40', f1= '(40)Basic Table')
    db.dui0alerts.insert( f0= 'aa42', f1= '(42)Data Table')
    db.dui0alerts.insert( f0= 'aa44', f1= '(44)Basic Form')
    db.dui0alerts.insert( f0= 'aa46', f1= '(46)Advanced Form')
    db.dui0alerts.insert( f0= 'hc47', f1= '(47)Icons')
    db.dui0alerts.insert( f0= 'aa49', f1= '(49)Font Awesome')
    db.dui0alerts.insert( f0= 'aa51', f1= '(51)Themefy Icons')
    db.dui0alerts.insert( f0= 'aa54', f1= '(54)Chart JS')
    db.dui0alerts.insert( f0= 'aa56', f1= '(56)Flot Chart')
    db.dui0alerts.insert( f0= 'aa58', f1= '(58)Peity Chart')
    db.dui0alerts.insert( f0= 'aa60', f1= '(60)Google Maps')
    db.dui0alerts.insert( f0= 'aa62', f1= '(62)Vector Maps')
    db.dui0alerts.insert( f0= 'hc63', f1= '(63)Extras')
    db.dui0alerts.insert( f0= 'aa65', f1= '(65)Login')
    db.dui0alerts.insert( f0= 'aa67', f1= '(67)Register')
    db.dui0alerts.insert( f0= 'aa69', f1= '(69)Forget Pass')
    db.dui0alerts.insert( f0= 'pb70', f1= '(70)Search ...')
    db.dui0alerts.insert( f0= 'pc71', f1= '(71)You have 3 Notification')
    db.dui0alerts.insert( f0= 'pc72', f1= '(72)You have 4 Mails')
    db.dui0alerts.insert( f0= 'sx74', f1= '(74)Jonathan Smith')
    db.dui0alerts.insert( f0= 'sx75', f1= '(75)Just now')
    db.dui0alerts.insert( f0= 'pa76', f1= '(76)Hello, this is an example msg')
    db.dui0alerts.insert( f0= 'sx78', f1= '(78)Jack Sanders')
    db.dui0alerts.insert( f0= 'sx79', f1= '(79)5 minutes ago')
    db.dui0alerts.insert( f0= 'pa80', f1= '(80)Lorem ipsum dolor sit amet, consectetur')
    db.dui0alerts.insert( f0= 'sx82', f1= '(82)Cheryl Wheeler')
    db.dui0alerts.insert( f0= 'sx83', f1= '(83)10 minutes ago')
    db.dui0alerts.insert( f0= 'pa84', f1= '(84)Hello, this is an example msg')
    db.dui0alerts.insert( f0= 'sx86', f1= '(86)Rachel Santos')
    db.dui0alerts.insert( f0= 'sx87', f1= '(87)15 minutes ago')
    db.dui0alerts.insert( f0= 'pa88', f1= '(88)Lorem ipsum dolor sit amet, consectetur')
    db.dui0alerts.insert( f0= 'sx90', f1= '(90)13')
    db.dui0alerts.insert( f0= 'hh91', f1= '(91)Dashboard')
    db.dui0alerts.insert( f0= 'aa92', f1= '(92)Dashboard')
    db.dui0alerts.insert( f0= 'aa93', f1= '(93)UI Elements')
    db.dui0alerts.insert( f0= 'lb94', f1= '(94)Alerts')
    db.dui0alerts.insert( f0= 'aa95', f1= '(95)an example link')
    db.dui0alerts.insert( f0= 'aa96', f1= '(96)an example link')
    db.dui0alerts.insert( f0= 'aa97', f1= '(97)an example link')
    db.dui0alerts.insert( f0= 'aa98', f1= '(98)an example link')
    db.dui0alerts.insert( f0= 'aa99', f1= '(99)an example link')
    db.dui0alerts.insert( f0= 'aa100', f1= '(100)an example link')
    db.dui0alerts.insert( f0= 'aa101', f1= '(101)an example link')
    db.dui0alerts.insert( f0= 'aa102', f1= '(102)an example link')
    db.dui0alerts.insert( f0= 'sx103', f1= '(103)Success')
    db.dui0alerts.insert( f0= 'sx104', f1= '(104)&times;')
    db.dui0alerts.insert( f0= 'sx105', f1= '(105)Success')
    db.dui0alerts.insert( f0= 'sx106', f1= '(106)&times;')
    db.dui0alerts.insert( f0= 'sx107', f1= '(107)Success')
    db.dui0alerts.insert( f0= 'sx108', f1= '(108)&times;')
    db.dui0alerts.insert( f0= 'sx109', f1= '(109)Success')
    db.dui0alerts.insert( f0= 'sx110', f1= '(110)&times;')
    db.dui0alerts.insert( f0= 'sx111', f1= '(111)Success')
    db.dui0alerts.insert( f0= 'sx112', f1= '(112)&times;')
    db.dui0alerts.insert( f0= 'sx113', f1= '(113)Success')
    db.dui0alerts.insert( f0= 'sx114', f1= '(114)&times;')
    db.dui0alerts.insert( f0= 'sx115', f1= '(115)Success')
    db.dui0alerts.insert( f0= 'sx116', f1= '(116)&times;')
    db.dui0alerts.insert( f0= 'sx117', f1= '(117)Success')
    db.dui0alerts.insert( f0= 'sx118', f1= '(118)&times;')
    db.dui0alerts.insert( f0= 'hd119', f1= '(119)Well done!')
    db.dui0alerts.insert( f0= 'pa120', f1= '(120)Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.')
    db.dui0alerts.insert( f0= 'pc121', f1= '(121)Whenever you need to, be sure to use margin utilities to keep things nice and tidy.')
    db.dui0alerts.insert( f0= 'hd122', f1= '(122)Well done!')
    db.dui0alerts.insert( f0= 'pa123', f1= '(123)Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.')
    db.dui0alerts.insert( f0= 'pc124', f1= '(124)Whenever you need to, be sure to use margin utilities to keep things nice and tidy.')
    db.dui0alerts.insert( f0= 'hd125', f1= '(125)Well done!')
    db.dui0alerts.insert( f0= 'pa126', f1= '(126)Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.')
    db.dui0alerts.insert( f0= 'pc127', f1= '(127)Whenever you need to, be sure to use margin utilities to keep things nice and tidy.')
    db.commit()
#
