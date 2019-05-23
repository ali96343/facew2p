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
    db.dcharts.insert( f0= 'aa59', f1= '(59)Start Bootstrap')
    db.dcharts.insert( f0= 'pb60', f1= '(60)Search for...')
    db.dcharts.insert( f0= 'sx61', f1= '(61)9+')
    db.dcharts.insert( f0= 'aa62', f1= '(62)Action')
    db.dcharts.insert( f0= 'aa63', f1= '(63)Another action')
    db.dcharts.insert( f0= 'aa64', f1= '(64)Something else here')
    db.dcharts.insert( f0= 'aa65', f1= '(65)Action')
    db.dcharts.insert( f0= 'aa66', f1= '(66)Another action')
    db.dcharts.insert( f0= 'aa67', f1= '(67)Something else here')
    db.dcharts.insert( f0= 'aa68', f1= '(68)Settings')
    db.dcharts.insert( f0= 'aa69', f1= '(69)Activity Log')
    db.dcharts.insert( f0= 'aa70', f1= '(70)Logout')
    db.dcharts.insert( f0= 'sp72', f1= '(72)Dashboard')
    db.dcharts.insert( f0= 'sp73', f1= '(73)Pages')
    db.dcharts.insert( f0= 'hf74', f1= '(74)Login Screens:')
    db.dcharts.insert( f0= 'aa76', f1= '(76)Login')
    db.dcharts.insert( f0= 'aa78', f1= '(78)Register')
    db.dcharts.insert( f0= 'aa80', f1= '(80)Forgot Password')
    db.dcharts.insert( f0= 'hf81', f1= '(81)Other Pages:')
    db.dcharts.insert( f0= 'aa83', f1= '(83)404 Page')
    db.dcharts.insert( f0= 'aa85', f1= '(85)Blank Page')
    db.dcharts.insert( f0= 'sp87', f1= '(87)Charts')
    db.dcharts.insert( f0= 'sp89', f1= '(89)Tables')
    db.dcharts.insert( f0= 'aa90', f1= '(90)Dashboard')
    db.dcharts.insert( f0= 'lb91', f1= '(91)Charts')
    db.dcharts.insert( f0= 'di92', f1= '(92)Updated yesterday at 11:59 PM')
    db.dcharts.insert( f0= 'di93', f1= '(93)Updated yesterday at 11:59 PM')
    db.dcharts.insert( f0= 'di94', f1= '(94)Updated yesterday at 11:59 PM')
    db.dcharts.insert( f0= 'sp95', f1= '(95)Copyright  Your Website 2019')
    db.dcharts.insert( f0= 'he96', f1= '(96)Ready to Leave?')
    db.dcharts.insert( f0= 'sx97', f1= '(97)')
    db.dcharts.insert( f0= 'di98', f1= '(98)Select Logout below if you are ready to end your current session.')
    db.dcharts.insert( f0= 'bu99', f1= '(99)Cancel')
    db.dcharts.insert( f0= 'aa101', f1= '(101)Logout')
    db.commit()
#
