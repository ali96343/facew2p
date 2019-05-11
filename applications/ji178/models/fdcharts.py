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
    db.dcharts.insert( f0= 'sp66', f1= '(66)Dashboard')
    db.dcharts.insert( f0= 'sp67', f1= '(67)Components')
    db.dcharts.insert( f0= 'hf68', f1= '(68)Custom Components:')
    db.dcharts.insert( f0= 'sp71', f1= '(71)Utilities')
    db.dcharts.insert( f0= 'hf72', f1= '(72)Custom Utilities:')
    db.dcharts.insert( f0= 'sp77', f1= '(77)Pages')
    db.dcharts.insert( f0= 'hf78', f1= '(78)Login Screens:')
    db.dcharts.insert( f0= 'hf82', f1= '(82)Other Pages:')
    db.dcharts.insert( f0= 'sp86', f1= '(86)Charts')
    db.dcharts.insert( f0= 'sp88', f1= '(88)Tables')
    db.dcharts.insert( f0= 'pb89', f1= '(89)Search for...')
    db.dcharts.insert( f0= 'pb90', f1= '(90)Search for...')
    db.dcharts.insert( f0= 'sx91', f1= '(91)3+')
    db.dcharts.insert( f0= 'di92', f1= '(92)December 12, 2019')
    db.dcharts.insert( f0= 'sx93', f1= '(93)A new monthly report is ready to download!')
    db.dcharts.insert( f0= 'di94', f1= '(94)December 7, 2019')
    db.dcharts.insert( f0= 'di95', f1= '(95)December 2, 2019')
    db.dcharts.insert( f0= 'aa96', f1= '(96)Show All Alerts')
    db.dcharts.insert( f0= 'sx97', f1= '(97)7')
    db.dcharts.insert( f0= 'di98', f1= '(98)Hi there! I am wondering if you can help me with a problem I ve been having.')
    db.dcharts.insert( f0= 'di99', f1= '(99)Emily Fowler  58m')
    db.dcharts.insert( f0= 'di100', f1= '(100)I have the photos that you ordered last month, how would you like them sent to you?')
    db.dcharts.insert( f0= 'di101', f1= '(101)Jae Chun  1d')
    db.dcharts.insert( f0= 'di102', f1= '(102)Morgan Alvarez  2d')
    db.dcharts.insert( f0= 'di103', f1= '(103)Am I a good boy? The reason I ask is because someone told me that people say this to all dogs, even if they aren t good...')
    db.dcharts.insert( f0= 'di104', f1= '(104)Chicken the Dog  2w')
    db.dcharts.insert( f0= 'aa105', f1= '(105)Read More Messages')
    db.dcharts.insert( f0= 'sx106', f1= '(106)Valerie Luna')
    db.dcharts.insert( f0= 'ha107', f1= '(107)Charts')
    db.dcharts.insert( f0= 'pc108', f1= '(108).')
    db.dcharts.insert( f0= 'aa109', f1= '(109)official Chart.js documentation')
    db.dcharts.insert( f0= 'hf110', f1= '(110)Area Chart')
    db.dcharts.insert( f0= 'hf111', f1= '(111)Bar Chart')
    db.dcharts.insert( f0= 'hf112', f1= '(112)Donut Chart')
    db.dcharts.insert( f0= 'sp113', f1= '(113)Copyright &copy; Your Website 2019')
    db.dcharts.insert( f0= 'he114', f1= '(114)Ready to Leave?')
    db.dcharts.insert( f0= 'sx115', f1= '(115)')
    db.dcharts.insert( f0= 'di116', f1= '(116)Select Logout below if you are ready to end your current session.')
    db.dcharts.insert( f0= 'bu117', f1= '(117)Cancel')
    db.commit()
#
