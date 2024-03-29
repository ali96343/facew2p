#
# table for controller: grid
#

from gluon.contrib.populate import populate

db.define_table('dgrid', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dgrid.id ).count():
    db.dgrid.insert( f0= 'aa18', f1= '(18)Dashboard 1')
    db.dgrid.insert( f0= 'aa20', f1= '(20)Dashboard 2')
    db.dgrid.insert( f0= 'aa22', f1= '(22)Dashboard 3')
    db.dgrid.insert( f0= 'aa24', f1= '(24)Dashboard 4')
    db.dgrid.insert( f0= 'aa30', f1= '(30)Login')
    db.dgrid.insert( f0= 'aa32', f1= '(32)Register')
    db.dgrid.insert( f0= 'aa34', f1= '(34)Forget Password')
    db.dgrid.insert( f0= 'aa36', f1= '(36)Button')
    db.dgrid.insert( f0= 'aa38', f1= '(38)Badges')
    db.dgrid.insert( f0= 'aa40', f1= '(40)Tabs')
    db.dgrid.insert( f0= 'aa42', f1= '(42)Cards')
    db.dgrid.insert( f0= 'aa44', f1= '(44)Alerts')
    db.dgrid.insert( f0= 'aa46', f1= '(46)Progress Bars')
    db.dgrid.insert( f0= 'aa48', f1= '(48)Modals')
    db.dgrid.insert( f0= 'aa50', f1= '(50)Switchs')
    db.dgrid.insert( f0= 'aa52', f1= '(52)Grids')
    db.dgrid.insert( f0= 'aa54', f1= '(54)Fontawesome Icon')
    db.dgrid.insert( f0= 'aa56', f1= '(56)Typography')
    db.dgrid.insert( f0= 'aa59', f1= '(59)Dashboard 1')
    db.dgrid.insert( f0= 'aa61', f1= '(61)Dashboard 2')
    db.dgrid.insert( f0= 'aa63', f1= '(63)Dashboard 3')
    db.dgrid.insert( f0= 'aa65', f1= '(65)Dashboard 4')
    db.dgrid.insert( f0= 'aa71', f1= '(71)Login')
    db.dgrid.insert( f0= 'aa73', f1= '(73)Register')
    db.dgrid.insert( f0= 'aa75', f1= '(75)Forget Password')
    db.dgrid.insert( f0= 'aa77', f1= '(77)Button')
    db.dgrid.insert( f0= 'aa79', f1= '(79)Badges')
    db.dgrid.insert( f0= 'aa81', f1= '(81)Tabs')
    db.dgrid.insert( f0= 'aa83', f1= '(83)Cards')
    db.dgrid.insert( f0= 'aa85', f1= '(85)Alerts')
    db.dgrid.insert( f0= 'aa87', f1= '(87)Progress Bars')
    db.dgrid.insert( f0= 'aa89', f1= '(89)Modals')
    db.dgrid.insert( f0= 'aa91', f1= '(91)Switchs')
    db.dgrid.insert( f0= 'aa93', f1= '(93)Grids')
    db.dgrid.insert( f0= 'aa95', f1= '(95)Fontawesome Icon')
    db.dgrid.insert( f0= 'aa97', f1= '(97)Typography')
    db.dgrid.insert( f0= 'pb98', f1= '(98)Search for datas &amp; reports...')
    db.dgrid.insert( f0= 'pa99', f1= '(99)You have 2 news message')
    db.dgrid.insert( f0= 'hh101', f1= '(101)Michelle Moreno')
    db.dgrid.insert( f0= 'pa102', f1= '(102)Have sent a photo')
    db.dgrid.insert( f0= 'sx103', f1= '(103)3 min ago')
    db.dgrid.insert( f0= 'hh105', f1= '(105)Diane Myers')
    db.dgrid.insert( f0= 'pa106', f1= '(106)You are now connected on message')
    db.dgrid.insert( f0= 'sx107', f1= '(107)Yesterday')
    db.dgrid.insert( f0= 'aa108', f1= '(108)View all messages')
    db.dgrid.insert( f0= 'pa109', f1= '(109)You have 3 New Emails')
    db.dgrid.insert( f0= 'pa111', f1= '(111)Meeting about new dashboard...')
    db.dgrid.insert( f0= 'sp112', f1= '(112)Cynthia Harvey, 3 min ago')
    db.dgrid.insert( f0= 'pa114', f1= '(114)Meeting about new dashboard...')
    db.dgrid.insert( f0= 'sp115', f1= '(115)Cynthia Harvey, Yesterday')
    db.dgrid.insert( f0= 'pa117', f1= '(117)Meeting about new dashboard...')
    db.dgrid.insert( f0= 'sp118', f1= '(118)Cynthia Harvey, April 12,,2018')
    db.dgrid.insert( f0= 'aa119', f1= '(119)See all emails')
    db.dgrid.insert( f0= 'pa120', f1= '(120)You have 3 Notifications')
    db.dgrid.insert( f0= 'pa121', f1= '(121)You got a email notification')
    db.dgrid.insert( f0= 'sx122', f1= '(122)April 12, 2018 06:50')
    db.dgrid.insert( f0= 'pa123', f1= '(123)Your account has been blocked')
    db.dgrid.insert( f0= 'sx124', f1= '(124)April 12, 2018 06:50')
    db.dgrid.insert( f0= 'pa125', f1= '(125)You got a new file')
    db.dgrid.insert( f0= 'sx126', f1= '(126)April 12, 2018 06:50')
    db.dgrid.insert( f0= 'aa127', f1= '(127)All notifications')
    db.dgrid.insert( f0= 'aa129', f1= '(129)john doe')
    db.dgrid.insert( f0= 'aa131', f1= '(131)john doe')
    db.dgrid.insert( f0= 'sx132', f1= '(132)johndoe@example.com')
    db.dgrid.insert( f0= 'he133', f1= '(133)Fixed Grid')
    db.dgrid.insert( f0= 'di134', f1= '(134).col')
    db.dgrid.insert( f0= 'di135', f1= '(135).col')
    db.dgrid.insert( f0= 'di136', f1= '(136).col')
    db.dgrid.insert( f0= 'di137', f1= '(137).col')
    db.dgrid.insert( f0= 'di138', f1= '(138).col')
    db.dgrid.insert( f0= 'di139', f1= '(139).col')
    db.dgrid.insert( f0= 'di140', f1= '(140).col')
    db.dgrid.insert( f0= 'di141', f1= '(141).col')
    db.dgrid.insert( f0= 'di142', f1= '(142).col')
    db.dgrid.insert( f0= 'di143', f1= '(143).col')
    db.dgrid.insert( f0= 'di144', f1= '(144).col')
    db.dgrid.insert( f0= 'di145', f1= '(145).col')
    db.dgrid.insert( f0= 'di146', f1= '(146).col')
    db.dgrid.insert( f0= 'di147', f1= '(147).col')
    db.dgrid.insert( f0= 'di148', f1= '(148).col')
    db.dgrid.insert( f0= 'di149', f1= '(149).col')
    db.dgrid.insert( f0= 'di150', f1= '(150).col')
    db.dgrid.insert( f0= 'di151', f1= '(151).col')
    db.dgrid.insert( f0= 'di152', f1= '(152).col')
    db.dgrid.insert( f0= 'di153', f1= '(153).col')
    db.dgrid.insert( f0= 'di154', f1= '(154).col')
    db.dgrid.insert( f0= 'he155', f1= '(155)Desktop Grid')
    db.dgrid.insert( f0= 'di156', f1= '(156)col-lg-12')
    db.dgrid.insert( f0= 'di157', f1= '(157)col-lg-6')
    db.dgrid.insert( f0= 'di158', f1= '(158)col-lg-6')
    db.dgrid.insert( f0= 'di159', f1= '(159)col-lg-4')
    db.dgrid.insert( f0= 'di160', f1= '(160)col-lg-4')
    db.dgrid.insert( f0= 'di161', f1= '(161)col-lg-4')
    db.dgrid.insert( f0= 'di162', f1= '(162)col-lg-3')
    db.dgrid.insert( f0= 'di163', f1= '(163)col-lg-3')
    db.dgrid.insert( f0= 'di164', f1= '(164)col-lg-3')
    db.dgrid.insert( f0= 'di165', f1= '(165)col-lg-3')
    db.dgrid.insert( f0= 'di166', f1= '(166)col-lg-2')
    db.dgrid.insert( f0= 'di167', f1= '(167)col-lg-2')
    db.dgrid.insert( f0= 'di168', f1= '(168)col-lg-2')
    db.dgrid.insert( f0= 'di169', f1= '(169)col-lg-2')
    db.dgrid.insert( f0= 'di170', f1= '(170)col-lg-2')
    db.dgrid.insert( f0= 'di171', f1= '(171)col-lg-2')
    db.dgrid.insert( f0= 'hd172', f1= '(172)Mobile, Tablet, and Desktop')
    db.dgrid.insert( f0= 'di173', f1= '(173)col-2')
    db.dgrid.insert( f0= 'di174', f1= '(174)col-2')
    db.dgrid.insert( f0= 'di175', f1= '(175)col-lg-8')
    db.dgrid.insert( f0= 'di176', f1= '(176)col-sm-3')
    db.dgrid.insert( f0= 'di177', f1= '(177)col-sm-3')
    db.dgrid.insert( f0= 'di178', f1= '(178)col-lg-6')
    db.dgrid.insert( f0= 'di179', f1= '(179)col-md-4')
    db.dgrid.insert( f0= 'di180', f1= '(180)col-md-4')
    db.dgrid.insert( f0= 'di181', f1= '(181)col-lg-4')
    db.dgrid.insert( f0= 'di182', f1= '(182)col-sm-6')
    db.dgrid.insert( f0= 'di183', f1= '(183)col-sm-6')
    db.dgrid.insert( f0= 'he184', f1= '(184)Offset Grid')
    db.dgrid.insert( f0= 'di185', f1= '(185)col-md-6 offset-md-6 col-sm-6')
    db.dgrid.insert( f0= 'di186', f1= '(186).col-md-6 .offset-md-3')
    db.dgrid.insert( f0= 'di187', f1= '(187).col-md-4')
    db.dgrid.insert( f0= 'di188', f1= '(188).col-md-4 .ml-auto')
    db.commit()
#
