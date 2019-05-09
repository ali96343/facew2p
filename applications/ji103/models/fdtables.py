#
# table for controller: tables
#

from gluon.contrib.populate import populate

db.define_table('dtables', 
     Field('f0', label='key',  writable = True , length= 1000),
     Field('f1', 'text',  label='data string', length= 1000),
     Field('f2', 'text', label='save data string', length= 1000, default='' ),
     )
#

if not db(db.dtables.id ).count():
    db.dtables.insert( f0= 'aa121', f1= '(121)Start Bootstrap')
    db.dtables.insert( f0= 'pb122', f1= '(122)Search for...')
    db.dtables.insert( f0= 'sx123', f1= '(123)9+')
    db.dtables.insert( f0= 'aa124', f1= '(124)Action')
    db.dtables.insert( f0= 'aa125', f1= '(125)Another action')
    db.dtables.insert( f0= 'aa126', f1= '(126)Something else here')
    db.dtables.insert( f0= 'sx127', f1= '(127)7')
    db.dtables.insert( f0= 'aa128', f1= '(128)Action')
    db.dtables.insert( f0= 'aa129', f1= '(129)Another action')
    db.dtables.insert( f0= 'aa130', f1= '(130)Something else here')
    db.dtables.insert( f0= 'aa131', f1= '(131)Settings')
    db.dtables.insert( f0= 'aa132', f1= '(132)Activity Log')
    db.dtables.insert( f0= 'aa133', f1= '(133)Logout')
    db.dtables.insert( f0= 'sp135', f1= '(135)Dashboard')
    db.dtables.insert( f0= 'sp136', f1= '(136)Pages')
    db.dtables.insert( f0= 'hf137', f1= '(137)Login Screens:')
    db.dtables.insert( f0= 'aa139', f1= '(139)Login')
    db.dtables.insert( f0= 'aa141', f1= '(141)Register')
    db.dtables.insert( f0= 'aa143', f1= '(143)Forgot Password')
    db.dtables.insert( f0= 'hf144', f1= '(144)Other Pages:')
    db.dtables.insert( f0= 'aa146', f1= '(146)404 Page')
    db.dtables.insert( f0= 'aa148', f1= '(148)Blank Page')
    db.dtables.insert( f0= 'sp150', f1= '(150)Charts')
    db.dtables.insert( f0= 'sp152', f1= '(152)Tables')
    db.dtables.insert( f0= 'aa153', f1= '(153)Dashboard')
    db.dtables.insert( f0= 'lb154', f1= '(154)Tables')
    db.dtables.insert( f0= 'di212', f1= '(212)Updated yesterday at 11:59 PM')
    db.dtables.insert( f0= 'sp213', f1= '(213)Copyright  Your Website 2018')
    db.dtables.insert( f0= 'he214', f1= '(214)Ready to Leave?')
    db.dtables.insert( f0= 'sx215', f1= '(215)')
    db.dtables.insert( f0= 'di216', f1= '(216)Select Logout below if you are ready to end your current session.')
    db.dtables.insert( f0= 'bu217', f1= '(217)Cancel')
    db.dtables.insert( f0= 'aa219', f1= '(219)Logout')
    db.commit()
#
