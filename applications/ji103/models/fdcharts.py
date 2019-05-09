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
    db.dcharts.insert( f0= 'aa62', f1= '(62)Start Bootstrap')
    db.dcharts.insert( f0= 'pb63', f1= '(63)Search for...')
    db.dcharts.insert( f0= 'sx64', f1= '(64)9+')
    db.dcharts.insert( f0= 'aa65', f1= '(65)Action')
    db.dcharts.insert( f0= 'aa66', f1= '(66)Another action')
    db.dcharts.insert( f0= 'aa67', f1= '(67)Something else here')
    db.dcharts.insert( f0= 'sx68', f1= '(68)7')
    db.dcharts.insert( f0= 'aa69', f1= '(69)Action')
    db.dcharts.insert( f0= 'aa70', f1= '(70)Another action')
    db.dcharts.insert( f0= 'aa71', f1= '(71)Something else here')
    db.dcharts.insert( f0= 'aa72', f1= '(72)Settings')
    db.dcharts.insert( f0= 'aa73', f1= '(73)Activity Log')
    db.dcharts.insert( f0= 'aa74', f1= '(74)Logout')
    db.dcharts.insert( f0= 'sp76', f1= '(76)Dashboard')
    db.dcharts.insert( f0= 'sp77', f1= '(77)Pages')
    db.dcharts.insert( f0= 'hf78', f1= '(78)Login Screens:')
    db.dcharts.insert( f0= 'aa80', f1= '(80)Login')
    db.dcharts.insert( f0= 'aa82', f1= '(82)Register')
    db.dcharts.insert( f0= 'aa84', f1= '(84)Forgot Password')
    db.dcharts.insert( f0= 'hf85', f1= '(85)Other Pages:')
    db.dcharts.insert( f0= 'aa87', f1= '(87)404 Page')
    db.dcharts.insert( f0= 'aa89', f1= '(89)Blank Page')
    db.dcharts.insert( f0= 'sp91', f1= '(91)Charts')
    db.dcharts.insert( f0= 'sp93', f1= '(93)Tables')
    db.dcharts.insert( f0= 'aa94', f1= '(94)Dashboard')
    db.dcharts.insert( f0= 'lb95', f1= '(95)Charts')
    db.dcharts.insert( f0= 'di96', f1= '(96)Updated yesterday at 11:59 PM')
    db.dcharts.insert( f0= 'di97', f1= '(97)Updated yesterday at 11:59 PM')
    db.dcharts.insert( f0= 'di98', f1= '(98)Updated yesterday at 11:59 PM')
    db.dcharts.insert( f0= 'sp99', f1= '(99)Copyright  Your Website 2018')
    db.dcharts.insert( f0= 'he100', f1= '(100)Ready to Leave?')
    db.dcharts.insert( f0= 'sx101', f1= '(101)')
    db.dcharts.insert( f0= 'di102', f1= '(102)Select Logout below if you are ready to end your current session.')
    db.dcharts.insert( f0= 'bu103', f1= '(103)Cancel')
    db.dcharts.insert( f0= 'aa105', f1= '(105)Logout')
    db.commit()
#
