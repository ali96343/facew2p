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
    db.dtables.insert( f0= 'pb104', f1= '(104)Search for...')
    db.dtables.insert( f0= 'sx105', f1= '(105)9+')
    db.dtables.insert( f0= 'aa106', f1= '(106)Action')
    db.dtables.insert( f0= 'aa107', f1= '(107)Another action')
    db.dtables.insert( f0= 'aa108', f1= '(108)Something else here')
    db.dtables.insert( f0= 'sx109', f1= '(109)7')
    db.dtables.insert( f0= 'aa110', f1= '(110)Action')
    db.dtables.insert( f0= 'aa111', f1= '(111)Another action')
    db.dtables.insert( f0= 'aa112', f1= '(112)Something else here')
    db.dtables.insert( f0= 'aa113', f1= '(113)Settings')
    db.dtables.insert( f0= 'aa114', f1= '(114)Activity Log')
    db.dtables.insert( f0= 'aa115', f1= '(115)Logout')
    db.dtables.insert( f0= 'sp117', f1= '(117)Dashboard')
    db.dtables.insert( f0= 'sp118', f1= '(118)Pages')
    db.dtables.insert( f0= 'hf119', f1= '(119)Login Screens:')
    db.dtables.insert( f0= 'hf123', f1= '(123)Other Pages:')
    db.dtables.insert( f0= 'sp127', f1= '(127)Charts')
    db.dtables.insert( f0= 'sp129', f1= '(129)Tables')
    db.dtables.insert( f0= 'aa130', f1= '(130)Dashboard')
    db.dtables.insert( f0= 'lb131', f1= '(131)Tables')
    db.dtables.insert( f0= 'di189', f1= '(189)Updated yesterday at 11:59 PM')
    db.dtables.insert( f0= 'sp190', f1= '(190)Copyright  Your Website 2019')
    db.dtables.insert( f0= 'he191', f1= '(191)Ready to Leave?')
    db.dtables.insert( f0= 'sx192', f1= '(192)')
    db.dtables.insert( f0= 'di193', f1= '(193)Select Logout below if you are ready to end your current session.')
    db.dtables.insert( f0= 'bu194', f1= '(194)Cancel')
    db.commit()
#
