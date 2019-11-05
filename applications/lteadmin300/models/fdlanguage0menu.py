#
# table for controller: languageIImenu
#

from gluon.contrib.populate import populate

db.define_table('dlanguage0menu', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dlanguage0menu.id ).count():
    db.dlanguage0menu.insert( f0= 'aa5', f1= '(5)Home')
    db.dlanguage0menu.insert( f0= 'aa6', f1= '(6)Contact')
    db.dlanguage0menu.insert( f0= 'pb7', f1= '(7)Search')
    db.dlanguage0menu.insert( f0= 'sx8', f1= '(8)3')
    db.dlanguage0menu.insert( f0= 'pc10', f1= '(10)Call me whenever you can...')
    db.dlanguage0menu.insert( f0= 'pc11', f1= '(11)4 Hours Ago')
    db.dlanguage0menu.insert( f0= 'pc13', f1= '(13)I got your message bro')
    db.dlanguage0menu.insert( f0= 'pc14', f1= '(14)4 Hours Ago')
    db.dlanguage0menu.insert( f0= 'pc16', f1= '(16)The subject goes here')
    db.dlanguage0menu.insert( f0= 'pc17', f1= '(17)4 Hours Ago')
    db.dlanguage0menu.insert( f0= 'aa18', f1= '(18)See All Messages')
    db.dlanguage0menu.insert( f0= 'sx19', f1= '(19)15 Notifications')
    db.dlanguage0menu.insert( f0= 'sx20', f1= '(20)3 mins')
    db.dlanguage0menu.insert( f0= 'sx21', f1= '(21)12 hours')
    db.dlanguage0menu.insert( f0= 'sx22', f1= '(22)2 days')
    db.dlanguage0menu.insert( f0= 'aa23', f1= '(23)See All Notifications')
    db.dlanguage0menu.insert( f0= 'sx26', f1= '(26)AdminLTE 3')
    db.dlanguage0menu.insert( f0= 'pa28', f1= '(28)Dashboard v1')
    db.dlanguage0menu.insert( f0= 'pa30', f1= '(30)Dashboard v2')
    db.dlanguage0menu.insert( f0= 'pa32', f1= '(32)Dashboard v3')
    db.dlanguage0menu.insert( f0= 'sx34', f1= '(34)New')
    db.dlanguage0menu.insert( f0= 'sx35', f1= '(35)6')
    db.dlanguage0menu.insert( f0= 'pa37', f1= '(37)Top Navigation')
    db.dlanguage0menu.insert( f0= 'pa39', f1= '(39)Boxed')
    db.dlanguage0menu.insert( f0= 'pa41', f1= '(41)Fixed Sidebar')
    db.dlanguage0menu.insert( f0= 'pa43', f1= '(43)Fixed Navbar')
    db.dlanguage0menu.insert( f0= 'pa45', f1= '(45)Fixed Footer')
    db.dlanguage0menu.insert( f0= 'pa47', f1= '(47)Collapsed Sidebar')
    db.dlanguage0menu.insert( f0= 'pa49', f1= '(49)ChartJS')
    db.dlanguage0menu.insert( f0= 'pa51', f1= '(51)Flot')
    db.dlanguage0menu.insert( f0= 'pa53', f1= '(53)Inline')
    db.dlanguage0menu.insert( f0= 'pa55', f1= '(55)General')
    db.dlanguage0menu.insert( f0= 'pa57', f1= '(57)Icons')
    db.dlanguage0menu.insert( f0= 'pa59', f1= '(59)Buttons')
    db.dlanguage0menu.insert( f0= 'pa61', f1= '(61)Sliders')
    db.dlanguage0menu.insert( f0= 'pa63', f1= '(63)Modals & Alerts')
    db.dlanguage0menu.insert( f0= 'pa65', f1= '(65)Navbar & Tabs')
    db.dlanguage0menu.insert( f0= 'pa67', f1= '(67)Timeline')
    db.dlanguage0menu.insert( f0= 'pa69', f1= '(69)Ribbons')
    db.dlanguage0menu.insert( f0= 'pa71', f1= '(71)General Elements')
    db.dlanguage0menu.insert( f0= 'pa73', f1= '(73)Advanced Elements')
    db.dlanguage0menu.insert( f0= 'pa75', f1= '(75)Editors')
    db.dlanguage0menu.insert( f0= 'pa77', f1= '(77)Simple Tables')
    db.dlanguage0menu.insert( f0= 'pa79', f1= '(79)DataTables')
    db.dlanguage0menu.insert( f0= 'pa81', f1= '(81)jsGrid')
    db.dlanguage0menu.insert( f0= 'lb82', f1= '(82)EXAMPLES')
    db.dlanguage0menu.insert( f0= 'sx84', f1= '(84)2')
    db.dlanguage0menu.insert( f0= 'pa87', f1= '(87)Inbox')
    db.dlanguage0menu.insert( f0= 'pa89', f1= '(89)Compose')
    db.dlanguage0menu.insert( f0= 'pa91', f1= '(91)Read')
    db.dlanguage0menu.insert( f0= 'pa93', f1= '(93)Invoice')
    db.dlanguage0menu.insert( f0= 'pa95', f1= '(95)Profile')
    db.dlanguage0menu.insert( f0= 'pa97', f1= '(97)E-commerce')
    db.dlanguage0menu.insert( f0= 'pa99', f1= '(99)Projects')
    db.dlanguage0menu.insert( f0= 'pa101', f1= '(101)Project Add')
    db.dlanguage0menu.insert( f0= 'pa103', f1= '(103)Project Edit')
    db.dlanguage0menu.insert( f0= 'pa105', f1= '(105)Project Detail')
    db.dlanguage0menu.insert( f0= 'pa107', f1= '(107)Contacts')
    db.dlanguage0menu.insert( f0= 'pa109', f1= '(109)Login')
    db.dlanguage0menu.insert( f0= 'pa111', f1= '(111)Register')
    db.dlanguage0menu.insert( f0= 'pa113', f1= '(113)Forgot Password')
    db.dlanguage0menu.insert( f0= 'pa115', f1= '(115)Recover Password')
    db.dlanguage0menu.insert( f0= 'pa117', f1= '(117)Lockscreen')
    db.dlanguage0menu.insert( f0= 'pa119', f1= '(119)Legacy User Menu')
    db.dlanguage0menu.insert( f0= 'pa121', f1= '(121)Language Menu')
    db.dlanguage0menu.insert( f0= 'pa123', f1= '(123)Error 404')
    db.dlanguage0menu.insert( f0= 'pa125', f1= '(125)Error 500')
    db.dlanguage0menu.insert( f0= 'pa127', f1= '(127)Pace')
    db.dlanguage0menu.insert( f0= 'pa129', f1= '(129)Blank Page')
    db.dlanguage0menu.insert( f0= 'pa131', f1= '(131)Starter Page')
    db.dlanguage0menu.insert( f0= 'lb132', f1= '(132)MISCELLANEOUS')
    db.dlanguage0menu.insert( f0= 'pa133', f1= '(133)Documentation')
    db.dlanguage0menu.insert( f0= 'lb134', f1= '(134)MULTI LEVEL EXAMPLE')
    db.dlanguage0menu.insert( f0= 'pa135', f1= '(135)Level 1')
    db.dlanguage0menu.insert( f0= 'pa136', f1= '(136)Level 2')
    db.dlanguage0menu.insert( f0= 'pa137', f1= '(137)Level 3')
    db.dlanguage0menu.insert( f0= 'pa138', f1= '(138)Level 3')
    db.dlanguage0menu.insert( f0= 'pa139', f1= '(139)Level 3')
    db.dlanguage0menu.insert( f0= 'pa140', f1= '(140)Level 2')
    db.dlanguage0menu.insert( f0= 'pa141', f1= '(141)Level 1')
    db.dlanguage0menu.insert( f0= 'lb142', f1= '(142)LABELS')
    db.dlanguage0menu.insert( f0= 'pc143', f1= '(143)Important')
    db.dlanguage0menu.insert( f0= 'pa144', f1= '(144)Warning')
    db.dlanguage0menu.insert( f0= 'pa145', f1= '(145)Informational')
    db.dlanguage0menu.insert( f0= 'hh146', f1= '(146)Language Menu')
    db.dlanguage0menu.insert( f0= 'aa147', f1= '(147)Home')
    db.dlanguage0menu.insert( f0= 'lb148', f1= '(148)Language Menu')
    db.dlanguage0menu.insert( f0= 'hc149', f1= '(149)Title')
    db.dlanguage0menu.insert( f0= 'bb150', f1= '(150)Version')
    db.dlanguage0menu.insert( f0= 'aa151', f1= '(151)AdminLTE.io')
    db.commit()
#
