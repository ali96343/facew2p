#
# table for controller: charts
#

from gluon.contrib.populate import populate

db.define_table('dcharts', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dcharts.id ).count():
    db.dcharts.insert( f0= 'sp78', f1= '(78)Dashboard')
    db.dcharts.insert( f0= 'sp79', f1= '(79)Components')
    db.dcharts.insert( f0= 'hf80', f1= '(80)Custom Components:')
    db.dcharts.insert( f0= 'aa82', f1= '(82)Buttons')
    db.dcharts.insert( f0= 'aa84', f1= '(84)Cards')
    db.dcharts.insert( f0= 'sp85', f1= '(85)Utilities')
    db.dcharts.insert( f0= 'hf86', f1= '(86)Custom Utilities:')
    db.dcharts.insert( f0= 'aa88', f1= '(88)Colors')
    db.dcharts.insert( f0= 'aa90', f1= '(90)Borders')
    db.dcharts.insert( f0= 'aa92', f1= '(92)Animations')
    db.dcharts.insert( f0= 'aa94', f1= '(94)Other')
    db.dcharts.insert( f0= 'sp95', f1= '(95)Pages')
    db.dcharts.insert( f0= 'hf96', f1= '(96)Login Screens:')
    db.dcharts.insert( f0= 'aa98', f1= '(98)Login')
    db.dcharts.insert( f0= 'aa100', f1= '(100)Register')
    db.dcharts.insert( f0= 'aa102', f1= '(102)Forgot Password')
    db.dcharts.insert( f0= 'hf103', f1= '(103)Other Pages:')
    db.dcharts.insert( f0= 'aa105', f1= '(105)404 Page')
    db.dcharts.insert( f0= 'aa107', f1= '(107)Blank Page')
    db.dcharts.insert( f0= 'sp109', f1= '(109)Charts')
    db.dcharts.insert( f0= 'sp111', f1= '(111)Tables')
    db.dcharts.insert( f0= 'pb112', f1= '(112)Search for...')
    db.dcharts.insert( f0= 'pb113', f1= '(113)Search for...')
    db.dcharts.insert( f0= 'sx114', f1= '(114)3+')
    db.dcharts.insert( f0= 'di115', f1= '(115)December 12, 2019')
    db.dcharts.insert( f0= 'sx116', f1= '(116)A new monthly report is ready to download!')
    db.dcharts.insert( f0= 'di117', f1= '(117)December 7, 2019')
    db.dcharts.insert( f0= 'di118', f1= '(118)December 2, 2019')
    db.dcharts.insert( f0= 'aa119', f1= '(119)Show All Alerts')
    db.dcharts.insert( f0= 'di120', f1= '(120)Hi there! I am wondering if you can help me with a problem I ve been having.')
    db.dcharts.insert( f0= 'di121', f1= '(121)Emily Fowler  58m')
    db.dcharts.insert( f0= 'di122', f1= '(122)I have the photos that you ordered last month, how would you like them sent to you?')
    db.dcharts.insert( f0= 'di123', f1= '(123)Jae Chun  1d')
    db.dcharts.insert( f0= 'di124', f1= '(124)Last month s report looks great, I am very happy with the progress so far, keep up the good work!')
    db.dcharts.insert( f0= 'di125', f1= '(125)Morgan Alvarez  2d')
    db.dcharts.insert( f0= 'di126', f1= '(126)Am I a good boy? The reason I ask is because someone told me that people say this to all dogs, even if they aren t good...')
    db.dcharts.insert( f0= 'di127', f1= '(127)Chicken the Dog  2w')
    db.dcharts.insert( f0= 'aa128', f1= '(128)Read More Messages')
    db.dcharts.insert( f0= 'sx129', f1= '(129)Valerie Luna')
    db.dcharts.insert( f0= 'ha130', f1= '(130)Charts')
    db.dcharts.insert( f0= 'aa131', f1= '(131)official Chart.js documentation')
    db.dcharts.insert( f0= 'hf132', f1= '(132)Area Chart')
    db.dcharts.insert( f0= 'hf133', f1= '(133)Bar Chart')
    db.dcharts.insert( f0= 'hf134', f1= '(134)Donut Chart')
    db.dcharts.insert( f0= 'sp135', f1= '(135)Copyright &copy; Your Website 2019')
    db.dcharts.insert( f0= 'he136', f1= '(136)Ready to Leave?')
    db.dcharts.insert( f0= 'sx137', f1= '(137)')
    db.dcharts.insert( f0= 'di138', f1= '(138)Select Logout below if you are ready to end your current session.')
    db.dcharts.insert( f0= 'bu139', f1= '(139)Cancel')
    db.dcharts.insert( f0= 'aa141', f1= '(141)Logout')
    db.commit()
#
