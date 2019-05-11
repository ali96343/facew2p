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
    db.dcharts.insert( f0= 'pb53', f1= '(53)Search for...')
    db.dcharts.insert( f0= 'sx54', f1= '(54)9+')
    db.dcharts.insert( f0= 'aa55', f1= '(55)Action')
    db.dcharts.insert( f0= 'aa56', f1= '(56)Another action')
    db.dcharts.insert( f0= 'aa57', f1= '(57)Something else here')
    db.dcharts.insert( f0= 'sx58', f1= '(58)7')
    db.dcharts.insert( f0= 'aa59', f1= '(59)Action')
    db.dcharts.insert( f0= 'aa60', f1= '(60)Another action')
    db.dcharts.insert( f0= 'aa61', f1= '(61)Something else here')
    db.dcharts.insert( f0= 'aa62', f1= '(62)Settings')
    db.dcharts.insert( f0= 'aa63', f1= '(63)Activity Log')
    db.dcharts.insert( f0= 'aa64', f1= '(64)Logout')
    db.dcharts.insert( f0= 'sp66', f1= '(66)Dashboard')
    db.dcharts.insert( f0= 'sp67', f1= '(67)Pages')
    db.dcharts.insert( f0= 'hf68', f1= '(68)Login Screens:')
    db.dcharts.insert( f0= 'hf72', f1= '(72)Other Pages:')
    db.dcharts.insert( f0= 'sp76', f1= '(76)Charts')
    db.dcharts.insert( f0= 'sp78', f1= '(78)Tables')
    db.dcharts.insert( f0= 'aa79', f1= '(79)Dashboard')
    db.dcharts.insert( f0= 'lb80', f1= '(80)Charts')
    db.dcharts.insert( f0= 'di81', f1= '(81)Updated yesterday at 11:59 PM')
    db.dcharts.insert( f0= 'di82', f1= '(82)Updated yesterday at 11:59 PM')
    db.dcharts.insert( f0= 'di83', f1= '(83)Updated yesterday at 11:59 PM')
    db.dcharts.insert( f0= 'sp84', f1= '(84)Copyright  Your Website 2019')
    db.dcharts.insert( f0= 'he85', f1= '(85)Ready to Leave?')
    db.dcharts.insert( f0= 'sx86', f1= '(86)')
    db.dcharts.insert( f0= 'di87', f1= '(87)Select Logout below if you are ready to end your current session.')
    db.dcharts.insert( f0= 'bu88', f1= '(88)Cancel')
    db.commit()
#
